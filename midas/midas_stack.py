import os
import json
import boto3
from botocore.exceptions import BotoCoreError, ClientError
from aws_cdk import (
    aws_ec2 as ec2,
    aws_rds as rds,
    aws_elasticbeanstalk as eb,
    aws_iam as iam,
    aws_s3_assets as s3_assets,
    CfnTag,
    SecretValue,
    RemovalPolicy,
    Stack,
    Tags,
)
from constructs import Construct

class MidasStack(Stack):
    """
    The MidasStack class defines the AWS infrastructure for the Midas project using AWS CDK.

    The Midas project is a cryptocurrency trading bot. For prototyping purposes, a Flask worker was implemented to run on Elastic Beanstalk (EBS). 
    This worker is responsible for automatically downloading the price values of different cryptocurrencies every second and adding certain indicators.

    The AWS infrastructure consists of the following resources:
    - A Virtual Private Cloud (VPC) to host the application resources.
    - A subnet group for the database.
    - A MySQL database instance on Amazon RDS.
    - An Elastic Beanstalk application to host the Flask worker.
    - An Elastic Beanstalk environment to define the worker's configuration.

    Each resource is tagged with relevant information to facilitate management and cost tracking.
    """


    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        """
        Constructor for the MidasStack class.

        :param scope: The scope in which this stack is defined.
        :param construct_id: The ID of this stack.
        :param kwargs: Additional arguments.
        """
        super().__init__(scope, construct_id, **kwargs)

        # Define tags for all resources in the stack

        def get_secret():
            session = boto3.session.Session()
            client = session.client(
                service_name='secretsmanager',
                region_name="us-east-1"
            )

            try:
                get_secret_value_response = client.get_secret_value(
                    SecretId="arn:aws:secretsmanager:us-east-1:930990375004:secret:development/midas/db-A2FqWL"
                )
            except ClientError as e:
                raise RuntimeError("Couldn't retrieve the secret") from e
            else:
                if 'SecretString' in get_secret_value_response:
                    secret = get_secret_value_response['SecretString']
                else:
                    raise RuntimeError("Couldn't retrieve the secret string")
                
            return json.loads(secret)
    
        tags = {
            "Main Developer": "Ernesto Cobos",
            "Project": "Midas",
            "Environment": "Development"
        }

        # Create a VPC
        vpc = ec2.Vpc(self, "midas-vpc", nat_gateways=1)
        for key, value in tags.items():
            Tags.of(vpc).add(key, value)

                    # Crear un grupo de seguridad
        security_group = ec2.SecurityGroup(
            self, 
            "midas-db-sg",
            vpc=vpc,
            description="Security group for Midas DB",
            allow_all_outbound=True   # Permitir todo el tráfico saliente
        )
        # Permitir todas las conexiones entrantes en el puerto 3306
        security_group.add_ingress_rule(
            ec2.Peer.any_ipv4(),  # Permitir tráfico desde cualquier dirección IP
            ec2.Port.tcp(3306)    # Permitir tráfico en el puerto 3306
        )

        # Create a subnet group for the database
        db_subnet_group = rds.SubnetGroup(
            self, 
            "midas-db-subnet-group",
            description="Subnet group for Midas DB",
            vpc=vpc,
            vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC)
        )

        for key, value in tags.items():
            Tags.of(db_subnet_group).add(key, value)


        db_secret = get_secret()

        # Create a MySQL database instance on Amazon RDS
        db = rds.DatabaseInstance(
            self,
            "midas-db",
            engine=rds.DatabaseInstanceEngine.mysql(
                version=rds.MysqlEngineVersion.VER_8_0_34
            ),
            instance_type=ec2.InstanceType.of(
                ec2.InstanceClass.BURSTABLE3, 
                ec2.InstanceSize.MICRO
            ),
            vpc=vpc,
            subnet_group=db_subnet_group,
            allocated_storage=30,
            storage_type=rds.StorageType.GP2,
            multi_az=False,
            credentials=rds.Credentials.from_password(
                username=db_secret['Username'],
                password=SecretValue.secrets_manager(
                    "arn:aws:secretsmanager:us-east-1:930990375004:secret:development/midas/db-A2FqWL",
                    json_field="Password"
                ),
            ),
            database_name='midas',
            removal_policy=RemovalPolicy.DESTROY,  # Change to core.RemovalPolicy.RETAIN if you want the database to persist after deleting the stack
            publicly_accessible=True,
            security_groups=[security_group],  # Usar el grupo de seguridad creado
        )

        for key, value in tags.items():
            Tags.of(db).add(key, value)

        

        # Create an Elastic Beanstalk application to host the Flask worker
        eb_app= eb.CfnApplication(
            self,
            "midas-ebs-app",
            application_name="midas",
            description="Midas Crypto Trading Bot",
        )

        for key, value in tags.items():
            Tags.of(eb_app).add(key, value)


        # Create a new S3 asset and upload the ZIP file
        # zip_asset = s3_assets.Asset(self, "MyZipAsset", path="ebs_dummy/dummy.zip")

        # Create a new application version
        # app_version = eb.CfnApplicationVersion(
        #    self,
        #    "AppVersion",
        #    application_name=eb_app.application_name,
        #    source_bundle=eb.CfnApplicationVersion.SourceBundleProperty(
        #        s3_bucket=zip_asset.s3_bucket_name,
        #        s3_key=zip_asset.s3_object_key
        #    )
        # )

        # Explicitly add a dependency on the application
        # app_version.add_depends_on(eb_app)

        # Create a role with necessary policies
        role = iam.Role(
            self,
            "my-instance-role",
            assumed_by=iam.ServicePrincipal("ec2.amazonaws.com"),
        )

        # Attach necessary policies to the role
        role.add_managed_policy(iam.ManagedPolicy.from_aws_managed_policy_name("AmazonS3ReadOnlyAccess"))
        # Add other necessary policies

        # Create an instance profile
        instance_profile = iam.CfnInstanceProfile(
            self,
            "InstanceProfile",
            roles=[role.role_name]
        )

        # Create an Elastic Beanstalk environment to define the worker's configuration
        # This is the documentation where I read how to use the tags https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_elasticbeanstalk/CfnEnvironment.html
        eb_env = eb.CfnEnvironment(
            self,
            "midas-ebs-env",
            environment_name="development",
            application_name=eb_app.application_name,
            solution_stack_name="64bit Amazon Linux 2023 v4.0.9 running Python 3.9",  # Updated platform version

            tier=eb.CfnEnvironment.TierProperty(
                name="Worker",
                type="SQS/HTTP"
            ),
            option_settings=[
                eb.CfnEnvironment.OptionSettingProperty(
                    namespace="aws:elasticbeanstalk:application:environment",
                    option_name="MYSQL_DATABASE_HOST",
                    value=db.db_instance_endpoint_address
                ),
                eb.CfnEnvironment.OptionSettingProperty(
                    namespace="aws:elasticbeanstalk:application:environment",
                    option_name="MYSQL_DATABASE_USERNAME",
                    value=db_secret['Username']
                ),
                eb.CfnEnvironment.OptionSettingProperty(
                    namespace="aws:elasticbeanstalk:application:environment",
                    option_name="MYSQL_DATABASE_PASSWORD",
                    value=db_secret['Password']
                ),
                eb.CfnEnvironment.OptionSettingProperty(
                    namespace="aws:elasticbeanstalk:application:environment",
                    option_name="MYSQL_DATABASE_DB",
                    value="midas"
                ),
                eb.CfnEnvironment.OptionSettingProperty(
                    namespace="aws:elasticbeanstalk:application:environment",
                    option_name="POLIGON_API_KEY",
                    value=os.environ.get('POLIGON_API_KEY', 'NA')
                ),
                eb.CfnEnvironment.OptionSettingProperty(
                    namespace="aws:elasticbeanstalk:application:environment",
                    option_name="SENTRY_DSN",
                    value=os.environ.get('SENTRY_DSN', 'NA')
                ),
                eb.CfnEnvironment.OptionSettingProperty(
                    namespace="aws:elasticbeanstalk:application:environment",
                    option_name="FLASK_APP",
                    value='midasbot/app.py'
                ),
                eb.CfnEnvironment.OptionSettingProperty(
                    namespace="aws:autoscaling:asg",
                    option_name="MinSize",
                    value="1"
                ),
                eb.CfnEnvironment.OptionSettingProperty(
                    namespace="aws:autoscaling:asg",
                    option_name="MaxSize",
                    value="2"
                ),
                eb.CfnEnvironment.OptionSettingProperty(
                    namespace="aws:autoscaling:launchconfiguration",
                    option_name="IamInstanceProfile",
                    value=instance_profile.ref
                ),
            ],
            tags=[
                CfnTag(key="Main Developer", value="Ernesto Cobos"),
                CfnTag(key="Project", value="Midas"),
                CfnTag(key="Environment", value="Development"),
            ]
        )
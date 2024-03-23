from aws_cdk import (
    aws_ecr as ecr,
    core,
    aws_elasticbeanstalk as eb,
    aws_ec2 as ec2,
    aws_rds as rds,   
)
class MidasStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        tags = {
            "Main Developer": "Ernesto Cobos",
            "Project": "Midas",
            "Environment": "Development"
        }

        vpc = ec2.Vpc(self, "midas-vpc")
        db = rds.DatabaseInstance(
            self,
            "midas-db",
            engine=rds.DatabaseInstanceEngine.postgres(
                version=rds.PostgresEngineVersion.VER_16_2
            ),
            instance_type=ec2.InstanceType.of(
                ec2.InstanceClass.BURSTABLE2, 
                ec2.InstanceSize.MICRO
            ),
            vpc=vpc,
            vpc_subnets=ec2.SubnetSelection(
                subnet_type=ec2.SubnetType.PUBLIC
            ),
            allocated_storage=30,
            storage_type=rds.StorageType.GP2,
            multi_az=False,
            credentials=rds.Credentials.from_password(
                username="mydbuser",
                password=core.SecretValue.plain_text("mydbpassword")
            ),
            removal_policy=core.RemovalPolicy.DESTROY,  # Cambia a core.RemovalPolicy.RETAIN si quieres que la base de datos persista después de eliminar la pila
        )
        

        eb_app= eb.CfnApplication(
            self,
            "midas-ebs-app",
            application_name="midas",
            description="Midas Crypto Trading Bot",
        )
        eb_env = eb.CfnEnvironment(
            self,
            "midas-ebs-env",
            environment_name="development",
            application_name=eb_app.application_name,
            solution_stack_name="64bit Amazon Linux 2 v3.1.0 running Python 3.8",
            tier=eb.CfnEnvironment.TierProperty(
                name="Worker",
                type="SQS/HTTP"
            ),
            option_settings=[
                eb.CfnEnvironment.OptionSettingProperty(
                    namespace="aws:elasticbeanstalk:application:environment",
                    option_name="DB_HOST",
                    value=db.db_instance_endpoint_address
                ),
                eb.CfnEnvironment.OptionSettingProperty(
                    namespace="aws:elasticbeanstalk:application:environment",
                    option_name="DB_USER",
                    value="mydbuser"
                ),
                eb.CfnEnvironment.OptionSettingProperty(
                    namespace="aws:elasticbeanstalk:application:environment",
                    option_name="DB_PASSWORD",
                    value="mydbpassword"
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
            ],
        )
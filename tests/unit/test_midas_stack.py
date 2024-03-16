import aws_cdk as core
import aws_cdk.assertions as assertions

from midas.midas_stack import MidasStack

# example tests. To run these tests, uncomment this file along with the example
# resource in midas/midas_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = MidasStack(app, "midas")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })

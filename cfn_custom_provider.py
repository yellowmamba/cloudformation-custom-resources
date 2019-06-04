from crhelper import CfnResource
import boto3
import logging

logger = logging.getLogger(__name__)

helper = CfnResource(
    json_logging=False,
    log_level='DEBUG', 
    boto_level='CRITICAL'
)


def handler(event, context):
    helper(event, context)
    
    
@helper.create
def create(event, context):
    client = boto3.client('iam')
    client.tag_role(
        RoleName=event['ResourceProperties']['RoleName'],
        Tags=event['ResourceProperties']['Tags']
    )

    logger.info("Got Create")    
    # helper.Data.update({"test": "testdata"})
    return "mycustomroletag"


@helper.update
def update(event, context):
    client = boto3.client('iam')
    client.tag_role(
        RoleName=event['ResourceProperties']['RoleName'],
        Tags=event['ResourceProperties']['Tags']
    )
    
    logger.info("Got Update")
    return "mycustomroletag"


@helper.delete
def delete(event, context):
    logger.info("Got Delete")
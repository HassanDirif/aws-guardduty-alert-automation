
import json
import os
import boto3

sns = boto3.client("sns")


def lambda_handler(event, context):
    detail = event.get("detail", {})

    if isinstance(detail, str):
        detail = json.loads(detail)

    finding_type = detail.get("type", "Unknown")
    severity = detail.get("severity", 0)
    description = detail.get("description", "No description")
    finding_id = detail.get("id", "Unknown")

    message = (
        "GuardDuty Security Alert\n"
        f"Finding: {finding_type}\n"
        f"Severity: {severity}\n"
        f"Description: {description}\n"
        f"Finding ID: {finding_id}\n"
    )

    response = sns.publish(
        TopicArn=os.environ["SNS_TOPIC_ARN"],
        Subject="AWS GuardDuty Security Alert",
        Message=message
    )

    print(json.dumps({
        "finding_id": finding_id,
        "sns_message_id": response["MessageId"]
    }))

    return {
        "statusCode": 200,
        "body": "Alert sent"
    }

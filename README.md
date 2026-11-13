# AWS GuardDuty Security Alert Automation

An event-driven AWS security monitoring and alerting pipeline built using Amazon GuardDuty, EventBridge, AWS Lambda, Python, and Amazon SNS.

## Project Overview

This project demonstrates how AWS security findings can be processed automatically and delivered as email alerts through a serverless architecture.

The solution integrates GuardDuty with EventBridge to route security findings to a Python-based Lambda function, which extracts relevant threat information and publishes notifications through Amazon SNS.

## Architecture

**Amazon GuardDuty → Amazon EventBridge → AWS Lambda → Amazon SNS → Email Notification**

### AWS Services Used

| Service | Purpose |
|---|---|
| Amazon GuardDuty | Detects potential security threats in AWS |
| Amazon EventBridge | Filters and routes security finding events |
| AWS Lambda | Processes security findings using Python |
| Amazon SNS | Delivers automated email notifications |
| Amazon CloudWatch | Provides execution logs and monitoring |

## Implementation

1. Configured Amazon GuardDuty and generated sample security findings.
2. Created an EventBridge rule to match GuardDuty finding events.
3. Developed a Python Lambda function to extract finding IDs, threat types, severity levels, and descriptions.
4. Integrated Lambda with an SNS topic and confirmed an email subscription.
5. Tested Lambda execution and verified successful notification delivery.
6. Published a custom simulated security event to EventBridge to validate the complete event-driven notification pipeline.

## Testing and Validation

### Lambda Function Test

- Execution status: Successful
- HTTP status code: 200
- Response: `Alert sent`
- SNS message ID recorded in Lambda execution logs

### End-to-End Integration Test

Published a simulated GuardDuty-format finding to the EventBridge default event bus using the AWS CLI.

**Test finding:**
- Finding ID: `end-to-end-test-001`
- Threat type: `UnauthorizedAccess:EC2/SSHBruteForce`
- Severity: 8 (High)
- Scenario: Simulated SSH brute-force activity

**Results:**
- EventBridge accepted the event with zero failed entries.
- Lambda processed the simulated finding.
- SNS delivered an email containing the correct threat type, severity, description, and finding ID.

The integration test used a custom EventBridge event source rather than a live GuardDuty detection. The production event pattern was restored after testing.

## Security Considerations

- Serverless architecture without persistent compute instances
- Event-driven security notification processing
- AWS IAM-based service permissions
- CloudWatch logging for troubleshooting and execution visibility
- EventBridge rule disabled after testing to prevent unnecessary processing

## Project Outcome

Successfully demonstrated automated security alert delivery through an AWS serverless pipeline using a simulated security finding.

The project showcases practical experience with AWS security services, Python automation, event-driven architecture, cloud monitoring, and security alert integration.

## Future Improvements

- Filter findings by severity to reduce alert noise
- Add deduplication to prevent repeated notifications
- Integrate automated incident remediation with approval safeguards
- Add infrastructure as code using Terraform
- Validate the pipeline against real GuardDuty findings

## Technologies

**AWS GuardDuty | EventBridge | Lambda | SNS | CloudWatch | Python | AWS CLI**

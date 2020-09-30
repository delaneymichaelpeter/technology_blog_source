Title: AWS Configuration Notes 
Date: 2020-01-07 10:20
Modified: 2010-12-05 19:30
Tags: aws, cli
Slug: my-super-post
Authors: Peter Delaney 
Summary: Short summary of how to configure your aws credentials to use aws cli tool

# AWS CLI Setup

### gimme-aws-creds python script

>This python script helped to connect to the EBSCO AWS services

**Using Okat with the AWS CLI Instruction ** [URL](https://confluence.epnet.com/pages/viewpage.action?spaceKey=TCO&title=Using+okta+with+the+AWS+CLI)

```bash
# Generates ~/.okta_aws_login_config
gimmie-aws-creds --configure

# Populates device_token in ~/.okta_aws_login_config
gimmie-aws-creds --register_device

# Get Credentials stored in ~/.aws/credentials
gimmie-aws-creds --profile eis-deliverydevqa

```

Settings from my ~/.okta_aws_login_config file
```bash
[DEFAULT]
okta_org_url = https://ebsco.okta.com
okta_auth_server =
client_id =
gimme_creds_server = appurl
aws_appname =
aws_rolename =
write_aws_creds = True
cred_profile = default
okta_username = you@corp.epnet.com
app_url = https://ebsco.okta.com/home/amazon_aws/0oa75xrhtf2k4T7vH356/272
resolve_aws_alias = True
preferred_mfa_type = push
aws_default_duration = 3600
device_token = ...(auto-generated)...

[eis-lz]
okta_org_url = https://ebsco.okta.com
okta_auth_server =
client_id =
gimme_creds_server = appurl
aws_appname =
aws_rolename =
write_aws_creds = True
cred_profile = default
okta_username = you@corp.epnet.com
app_url = https://ebsco.okta.com/home/amazon_aws/0oapitc03kERuFw5J356/272
resolve_aws_alias = True
preferred_mfa_type = push
aws_default_duration = 3600
device_token = ...(auto-generated)...


```


The expected answers for connecting to the LZ accounts is as follows:

| Prompt | Answer |
| --- | --- |
| **Okta Configuration Profile Name** | <*profile_to_configure*> |
| **Okta URL for your organization**  | https://ebsco.okta.com  |                                         
| **URL for gimme-creds-server**      | appurl                                               |            
| **Application url:**                | https://ebsco.okta.com/home/amazon_aws/0oapitc03kERuFw5J356/272  |
| **Write AWS Credentials**           | y                                                                |
| **Resolve AWS alias**               | n                                                                |
| **AWS Role ARN**                    | *See note below for options*                                     |
| **Okta User Name**                  | <*your_netowrk_username*>                                        |
| **AWS Default Session Duration**    | 3600                                                             |
| **Preferred MFA Device Type**       | *Pick the one you want from the list supplied in the prompt*     |
| **AWS Credential Profile**          | <*profile_to_configure*>                                         |

> **Note**<br/>
> For the AWS Role ARN option above, leave it blank if you want to select your role at login time. It may be better to supply the arn of the specific role that you expect to be using in the CLI for that environment, using one of the following AWS Role ARNs that are available to developers in the Landingzone accounts:
> * LZ Ehost DevQa: 
>   * arn:aws:iam::402255358772:role/human/ReadOnly
>   * arn:aws:iam::402255358772:role/human/Developers
> * LZ Ehost Integration: 
>   * arn:aws:iam::227219783963:role/human/ReadOnly
> * LZ Ehost Live: 
>   * arn:aws:iam::604166521307:role/human/ReadOnly


## Getting Credentials
```bash
gimme-aws-creds --profile eis-deliverydevqa

Using password from keyring for pdelaney@corp.epnet.com
Okta Password for pdelaney@corp.epnet.com:
Do you want to save this password in the keyring? (y/n) n
Multi-factor Authentication required.
Preferred factor type of push not available.
Pick a factor:
[0] sms: +1 XXX-XXX-9719
[1] call: +1 XXX-XXX-9719
Selection: 0
A verification code has been sent to +1 XXX-XXX-9719
Enter verification code: 823780
Saving arn:aws:iam::872344130825:role/ADFS-ExDevTeamRole as eis-deliverydevqa
Written profile eis-deliverydevqa to /home/pdelaney/.aws/credentials
```


### Aliases to make the process easier
The following alias can be added to your ~/.bashrc or ~/.zshrc file to make it easier to initiate a login for a given profile:
```bash
# AWS CLI
alias aws-lz-dqa="unset AWS_PROFILE && gimme-aws-creds --profile eis-lz-ehost-devqa && export AWS_PROFILE=eis-lz-ehost-devqa"
alias aws-lz-int="unset AWS_PROFILE && gimme-aws-creds --profile eis-lz-ehost-integration && export AWS_PROFILE=eis-lz-ehost-integration"
alias aws-lz-live="unset AWS_PROFILE && gimme-aws-creds --profile eis-lz-ehost-live && export AWS_PROFILE=eis-lz-ehost-live"
```
## Using the AWS CLI

Follow the instructions [here][kubernetes-cluster-connect] to connect to a kubernetes cluster using the AWS CLI.

## Ability to Get Access to AWS ECR Docker images
**Instruction from following** [URL](https://docs.aws.amazon.com/AmazonECR/latest/userguide/getting-started-cli.html)
**Instruction to obtain Credentials to ECR** [URL](https://confluence.epnet.com/display/ART/How+to+pull+docker+images+to+your+local+machine)

```bash
# Get AWS credentails
gimme-aws-creds --profile eis-deliverydevqa

# Get a Password to ECR (Elastic Container Registry)  version 1.xx of aws
$(/usr/bin/aws ecr get-login --no-include-email --region us-east-1 --profile eis-deliverydevqa)

# Command Prints out something like the following
docker login -u AWS -p eyJwYXlsb2FkIjoiY1U0SXZyQUsvcnNGTDBneldHR0xrbSs4dG1lMzRXUUNMSm5rZGY0UnRCY2pUc005UEtvVXZmN3d4Yjd6NUo0c1F0aGNGM0J3T05OcDFqR012VmJoWVhyTkJ3NEJuNmhHSTU5d2E5UUxBTitzY0VrQlpGd3o5SnBsVUd4MDBwUjNwd1hBS2pUZlRDa0ZCT1I4L2tpZjlHWjhZZjFmNDJGYVFGa3BacjcwNEQ2cFpGSWFqZU1XMVdjNWFkYVZlNHhCWDQyUEdrbG43cW1iTSs2dGY1clNoWk5rcXd4bjFMQUpEOFF3TU5kZ2tlUHBxWlB2WGwrMFpFdHd0WWVMaXZQeUZnWE84ZVF6dnRUanJVajc4QklvSFhUcW8waDYvamVwekh0Vzg4czFWdUd6UEpLbUdFYUpLVzhCMXRFZHBSbHg0WlBGVEJQYk9abDE5T3hZODBPcG1FL2FSYWJiZERZSE9iaGRYYnVpdzUrRjVqWCtmVDNYNTV5eE1qaEZMcnhWU3ZFTDFrWS9kdk5Ram9YTTlHb29EelBRN1h4K1U1anVFWXkzaHQ4KzBlUExzOUZwaDZyWUtMQW1BSVhwNGNUd2hyWHRRMFo4ZmxzZ1RkK1pRenhtaGYxQmtwUXpLMjRXc1Fhb2t5dks0VWFDcSs1cmhjc3ZjQ1ZpbUc0ejY3bUtSb1EvSkpCT2VMaHcrWXo1ZllsWmoza2k3MFpRRW5pdUhJMmlHVzJoREd0QWpIRk1RZWZGYlpBaUdQSEF6T21SemFjT0xIRFVUT0tQUHRZZXNHV2liUEhoWU9Ham00REtmU2Q3bURTazJISlRMZ1JIQnNMRXg3Vi8wNHVYeVYrcFBKOVh6TVFnaWt3YVJVaXRWS25YbGpQZE01M1Q1SFZibUV0ek5XZXgvWTlxdU52RjQyRmdVNWZFdmp4SnBhemVuV2gzd2V2ZjRLUmxtODg1cGFyLzl6NndnUjd3ZXBHblhldUx6M255ZUtSMG80ZzZoUGRIM1cwQXV1eWs3N1R6R3MzV1FuamVKRXJaU2RDTkhvajdVc1h3OUd5Tkc1Q0xndlgvYklwYStBdkNnOGFhVnpoOFlLZ2ZlOHVPWGU5Nng1VzNEejNlSEd6K0I1UFVhUERTbk5xL2FmNVIxQm5YK0g1Um1jY2Q0aklVaXkxbkprUlFCZW5DUXAvNEE0VkxKQTdTQjFxOGpkU2hidUx4cEp0bGlxSmY0RlFqUzZSRk1Qb3cvS0ptczJTOHZLZm5IOEUwZC8rUE9EYnpUSXE5S2VCbFJLWDEyV0VnTnhZcnd5UmNnS1puSmJ4VXFPTmdpUlV6MytaRy9mcURqdWNmaWlVR2xuUGZLb2ZxaWJkaGltVEdleVBiUzZoMFlJdzBtWWJGNmlGdWJLZHhnbXVDcUF2a3J1T05VY3ByYnJLcGo3dkplK2JvQTNoQ1IrQWViQ25xZVFWQ2MyRC9FSExvQktYT1dBVkJZZHpVa2d2eVZmY0JocGlQb1RXRXhjaFExZWFzRnEzLzNIYmxrTkN6dFRJQ1dDcFE0SkNaNDlLUkNUYmIwbFRhN25md2JKYXBYUEZLam9rbDdxZVVIWkphRWcrZVZSRmx5TU1KakF5b1hZcU9SNWZpMnNmK3lwcEZ6b1hzQjZjYWxIWjRPZGhML1lhZUFGQTkrZGgrSWRlajNFZFcvazg3QlhMOWVkL1ZkcjRyczJuWmsvdmREczhDWXh6M1VYc3diKytxSmt3R1F0ME4xYUNtNGtMWHQ0cUt1RlNtcHNoT0FWY0o3dzYveTdUUnFHcTZTdTBFOEVXaTArL2pHL1lNcEhoRDNka2RnVTE0djF3T244TC9rNDQ3ZHNjZGI1Z2V3Q3g5NFJGLzRFc0swMWZkbzU1NTZQenNrRmZRVW5nTlVTSHhTNU91K3pldng2V3FKRHAvSzZPSWlTeDhCTm1GNldyWUswMVkyaFRpVGhrSmFST0F5aGkvN0NWZXhjMFB3UlA0VEFCVE1pdVZ0SFpGeVU0czZvK0o2TGhoSW9DeGV3eC94UT09IiwiZGF0YWtleSI6IkFRRUJBSGh3bTBZYUlTSmVSdEptNW4xRzZ1cWVla1h1b1hYUGU1VUZjZTlScTgvMTR3QUFBSDR3ZkFZSktvWklodmNOQVFjR29HOHdiUUlCQURCb0Jna3Foa2lHOXcwQkJ3RXdIZ1lKWUlaSUFXVURCQUV1TUJFRURNdExkQXhuSzkxVzZaSkZvZ0lCRUlBN0RJRFEzZXNlemtwWW1Vc2EwQnZ5ZmVUWnJzWTBtMlpkc2hvcWtOTjV1Wm4vQmxqUDdXejdDOC80OU9IejVXbEZEWms0UFlnVWp3SnJiTGM9IiwidmVyc2lvbiI6IjIiLCJ0eXBlIjoiREFUQV9LRVkiLCJleHBpcmF0aW9uIjoxNjAwMjM4NjA5fQ== https://872344130825.dkr.ecr.us-east-1.amazonaws.com

# Get a Password to ECR (Elastic Container Registry)  version 2.xx of aws
$(/usr/local/bin/aws ecr get-login-password --region us-east-1 --profile eis-deliverydevqa)

# Another
/usr/local/bin/aws ecr get-login-password --region us-east-1 --p eis-lz | docker login -u AWS -password-stdin 098917983173.dkr.ecr.us-east-1.amazonaws.com

# Command Prints out something like the following
eyJwYXlsb2FkIjoiY1U0SXZyQUsvcnNGTDBneldHR0xrbSs4dG1lMzRXUUNMSm5rZGY0UnRCY2pUc005UEtvVXZmN3d4Yjd6NUo0c1F0aGNGM0J3T05OcDFqR012VmJoWVhyTkJ3NEJuNmhHSTU5d2E5UUxBTitzY0VrQlpGd3o5SnBsVUd4MDBwUjNwd1hBS2pUZlRDa0ZCT1I4L2tpZjlHWjhZZjFmNDJGYVFGa3BacjcwNEQ2cFpGSWFqZU1XMVdjNWFkYVZlNHhCWDQyUEdrbG43cW1iTSs2dGY1clNoWk5rcXd4bjFMQUpEOFF3TU5kZ2tlUHBxWlB2WGwrMFpFdHd0WWVMaXZQeUZnWE84ZVF6dnRUanJVajc4QklvSFhUcW8waDYvamVwekh0Vzg4czFWdUd6UEpLbUdFYUpLVzhCMXRFZHBSbHg0WlBGVEJQYk9abDE5T3hZODBPcG1FL2FSYWJiZERZSE9iaGRYYnVpdzUrRjVqWCtmVDNYNTV5eE1qaEZMcnhWU3ZFTDFrWS9kdk5Ram9YTTlHb29EelBRN1h4K1U1anVFWXkzaHQ4KzBlUExzOUZwaDZyWUtMQW1BSVhwNGNUd2hyWHRRMFo4ZmxzZ1RkK1pRenhtaGYxQmtwUXpLMjRXc1Fhb2t5dks0VWFDcSs1cmhjc3ZjQ1ZpbUc0ejY3bUtSb1EvSkpCT2VMaHcrWXo1ZllsWmoza2k3MFpRRW5pdUhJMmlHVzJoREd0QWpIRk1RZWZGYlpBaUdQSEF6T21SemFjT0xIRFVUT0tQUHRZZXNHV2liUEhoWU9Ham00REtmU2Q3bURTazJISlRMZ1JIQnNMRXg3Vi8wNHVYeVYrcFBKOVh6TVFnaWt3YVJVaXRWS25YbGpQZE01M1Q1SFZibUV0ek5XZXgvWTlxdU52RjQyRmdVNWZFdmp4SnBhemVuV2gzd2V2ZjRLUmxtODg1cGFyLzl6NndnUjd3ZXBHblhldUx6M255ZUtSMG80ZzZoUGRIM1cwQXV1eWs3N1R6R3MzV1FuamVKRXJaU2RDTkhvajdVc1h3OUd5Tkc1Q0xndlgvYklwYStBdkNnOGFhVnpoOFlLZ2ZlOHVPWGU5Nng1VzNEejNlSEd6K0I1UFVhUERTbk5xL2FmNVIxQm5YK0g1Um1jY2Q0aklVaXkxbkprUlFCZW5DUXAvNEE0VkxKQTdTQjFxOGpkU2hidUx4cEp0bGlxSmY0RlFqUzZSRk1Qb3cvS0ptczJTOHZLZm5IOEUwZC8rUE9EYnpUSXE5S2VCbFJLWDEyV0VnTnhZcnd5UmNnS1puSmJ4VXFPTmdpUlV6MytaRy9mcURqdWNmaWlVR2xuUGZLb2ZxaWJkaGltVEdleVBiUzZoMFlJdzBtWWJGNmlGdWJLZHhnbXVDcUF2a3J1T05VY3ByYnJLcGo3dkplK2JvQTNoQ1IrQWViQ25xZVFWQ2MyRC9FSExvQktYT1dBVkJZZHpVa2d2eVZmY0JocGlQb1RXRXhjaFExZWFzRnEzLzNIYmxrTkN6dFRJQ1dDcFE0SkNaNDlLUkNUYmIwbFRhN25md2JKYXBYUEZLam9rbDdxZVVIWkphRWcrZVZSRmx5TU1KakF5b1hZcU9SNWZpMnNmK3lwcEZ6b1hzQjZjYWxIWjRPZGhML1lhZUFGQTkrZGgrSWRlajNFZFcvazg3QlhMOWVkL1ZkcjRyczJuWmsvdmREczhDWXh6M1VYc3diKytxSmt3R1F0ME4xYUNtNGtMWHQ0cUt1RlNtcHNoT0FWY0o3dzYveTdUUnFHcTZTdTBFOEVXaTArL2pHL1lNcEhoRDNka2RnVTE0djF3T244TC9rNDQ3ZHNjZGI1Z2V3Q3g5NFJGLzRFc0swMWZkbzU1NTZQenNrRmZRVW5nTlVTSHhTNU91K3pldng2V3FKRHAvSzZPSWlTeDhCTm1GNldyWUswMVkyaFRpVGhrSmFST0F5aGkvN0NWZXhjMFB3UlA0VEFCVE1pdVZ0SFpGeVU0czZvK0o2TGhoSW9DeGV3eC94UT09IiwiZGF0YWtleSI6IkFRRUJBSGh3bTBZYUlTSmVSdEptNW4xRzZ1cWVla1h1b1hYUGU1VUZjZTlScTgvMTR3QUFBSDR3ZkFZSktvWklodmNOQVFjR29HOHdiUUlCQURCb0Jna3Foa2lHOXcwQkJ3RXdIZ1lKWUlaSUFXVURCQUV1TUJFRURNdExkQXhuSzkxVzZaSkZvZ0lCRUlBN0RJRFEzZXNlemtwWW1Vc2EwQnZ5ZmVUWnJzWTBtMlpkc2hvcWtOTjV1Wm4vQmxqUDdXejdDOC80OU9IejVXbEZEWms0UFlnVWp3SnJiTGM9IiwidmVyc2lvbiI6IjIiLCJ0eXBlIjoiREFUQV9LRVkiLCJleHBpcmF0aW9uIjoxNjAwMjM4NjA5fQ== https://872344130825.dkr.ecr.us-east-1.amazonaws.com

# Execute 

```

<!-- Links -->
[kubernetes-cluster-connect]: ./kubernetes.md#using-aws-cli-to-manage-your-kubernetes-configuration



Title: AWS Configuration Notes 
Date: 2020-01-07 10:20
Modified: 2010-12-05 19:30
Tags: aws, cli
Slug: my-super-post
Authors: Peter Delaney 
Summary: Short summary of how to configure your aws credentials to use aws cli tool

# AWS CLI Setup

### Setting up your aws credentials profile

```bash
# Configure your profiles
aws configure set region us-east-1 --profile eis-lz-ehost-devqa
aws configure set region us-east-1 --profile eis-lz-ehost-integration
aws configure set region us-east-1 --profile eis-lz-ehost-live
```

# Gimme
```bash
# Get Credentials for a Profile
gimme-aws-creds --configure --profile eis-lz-ehost-devqa
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

<!-- Links -->
[kubernetes-cluster-connect]: ./kubernetes.md#using-aws-cli-to-manage-your-kubernetes-configuration



Title: AWS Configuration Notes 
Date: 2020-01-07 10:20
Modified: 2010-12-05 19:30
Category: AWS CLI
Tags: aws, cli
Slug: my-super-post
Authors: Peter Delaney 
Summary: Short summary of how to configure your aws credentials  

# AWS CLI Setup

# Setting up your aws credentials profile

```
aws configure set region us-east-1 --profile eis-lz-ehost-devqa
aws configure set region us-east-1 --profile eis-lz-ehost-integration
aws configure set region us-east-1 --profile eis-lz-ehost-live
```

# Gimme
```
gimme-aws-creds --configure --profile eis-lz-ehost-devqa
```



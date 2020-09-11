Title:  EBSCO Jenkins Information
Date: 2020-09-11 10:20
Modified: 2020-09-11 19:30
Tags: shake-n-bake, jenkins
Category: EBSCO
Slug: Jenkins-Info
Authors: Peter Delaney 
Summary: EBSCO Jenkins Information


## Jenkins Groovy Script URL in GitHub

>
>The Jenkins Pipelines will utilize these Groovy Scripts depending on what Pipeline is running.
>
>Pipelines could be CI-Pipeline which is used by onprem application and Automation Factory.
>Strategic Pipeline has there own groovy scrips as well.

1. [Jenkins CI-Pipeline Groovy Scripts](https://github.com/EBSCOIS/platform.af.ci-pipeline/tree/master/vars)   **(Used by onprem applications)**
1. [Jenkins Strategic Pipeline Groovy Scripts](https://github.com/EBSCOIS/platform.infrastructure.pipelinelibrary/tree/master/vars) **(Used by SP)**
1. [Jenkins Java Library](https://github.com/EBSCOIS/platform.af.ci-pipeline/blob/master/vars/javaLibraryBuild.groovy) **(Java Library Groovy)**



## EBSCO Jenkins Servers

1. **CDF_Delivery_Pipelines**    [URL](http://jenkins.epnet.com/job/CDF_delivery_pipelines/)   **(Used by Automation Factory && aop-custom)**
1. **Legacy Jenkins Server**     [URL](http://ese-build6.epnet.com:8080/jenkins/)              **(ReceiverApp built here)**
1. **Strategic Pipeline Server** [URL](https://jenkins-apollo2.eis-platformlive.cloud/)        **(Used by Strategic Pipeline)**

## EBSCO SonarQube
**SonarQube URL** [URL](http://sonarqube.eis-platformlive.cloud:9000)
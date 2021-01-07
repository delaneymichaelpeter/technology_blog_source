Title:  EBSCO Automation Factory
Date: 2020-10-19 10:20
Modified: 2020-10-19 09:30
Tags: automation factory, af
Category: EBSCO
Slug: automationfactory
Authors: Peter Delaney 
Summary: EBSCO Automation Factory

**List of Videos on Automation Factory**

1. **Ervin Automation Factory Overview)[URL](https://web.microsoftstream.com/video/7d44b1a1-82c4-48c5-b76d-4f8dcd75b757)
2. **Ervin Automation Factory Session 1)[URL](https://web.microsoftstream.com/video/2a9ad9d6-d122-4cab-9a1b-587bcf126eaa)
3. **Ervin Automation Factory Session 2)[URL](https://web.microsoftstream.com/video/16c9c6c6-4976-4b1d-8636-640a2a6f7e7a)

# Steps Deploying to Automation Factory
[GitHub Instruction to Deploy to Automation Factory](https://github.com/EBSCOIS/onprem-automationfactoryguides)

**Step-By-Step-Instructions**

1. Create Spring Boot App
    1. Determine name of project maps to github name, Jenkins build filename
    1. Name onprem-af-<name-of-project>
    1. gradle 4
    2. spring boot 2.2.x
    3. JDK 1.8
2. Create Repo naming convetion 'onprem-af-<name-of-repo>
3. Create Jenkinsfile Build 
    1. **Instruction to do SO** [URL](https://github.com/EBSCOIS/onprem-automationfactoryguides/blob/main/how-to/get-started-JavaSpringBoot.md#continuous-integration)
4. Enable Console **DID NOT DO FILL IN LATER**
5. Create Branch from manifest-repo https://github.com/EBSCOIS/platform.af.environment-manifest/tree/environment/ads
    1. Add name of application in CODEOWNERS file, also NEED TO Add Architect to the name list. This will enable you to continue to add changes to Consul
    1. Create Pull Request to merge to environment/ads
    1. Check into your branch    
    4. Create another Branch for your BaseEnvironment/ServiceEndPoints.json
        1. Put your EndPoint here
    5. Create Pull Request into environment/ads
6. create orc/ directory in Project
    1. create app_manifest.yaml and inf_manifest.yaml
    2. Copy these from another project
7. Helpful Tips
    1. Make sure following names are consistantly the same
        1. Jenkins Project Build name: Ex "SlsFulltextService"
	1. setting.gradle file:  rootProject.name = 'SlsFulltextService'
	1. build.gradle file:
	ext {
	        groupId       = 'com.ebsco.service'
		artifactId    = 'slsfulltextservice'
		versionNumber = '0.0.1-SNAPSHOT'
	}
				



** TidBits Of Information That I need to collect**
>
>
1. Jenkins Build Server name needs to be the same as the Project name in settings.gradle and the same as in environment-manifest/CODEOWNERS file
1. CODEOWNERS needs two entries for your project: KVP/AutomationFactory/Services/<project-name> and KVP/Services/<project-name>
   Believe first is for AutomationFactory to pick up, second is so entry into Consol will be performed via Jenkins Pipeline
1. 


**Notes**

Name of your Project is very important it must match the Jenkins Pipeline Build Name to the name in the orc/inf_manifest.yaml
**Teams Notes from Eliezer Perez from Automation Factory Team**

**LIVE PDC/LIVE SDC:**

Updates to the Environment Manifest file for the LIVE environments are to be reviewed and approved by the owning architects. 

PRs must be submitted to update the CODEOWNERS file with at least 2 architects who own the Service, separate from any other changes, . 

Once the PR is reviewed and merged, the owning architects for that service will be able to review and approve your changes to the service going forward. 

 

**Non-Live:**

PRs must be submitted to add your team to the CODEOWNERS file for the lower environments for the Service your team owns, separate from any other changes,. 

Once the PR is reviewed and merged, your team will be able to manage changes made to that Service in the Lower Environments.


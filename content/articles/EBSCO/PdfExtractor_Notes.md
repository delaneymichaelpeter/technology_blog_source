Title:  EBSCO PDF Extractor Notes
Date: 2020-09-11 10:20
Modified: 2020-09-29 09:30
Tags: strategicpipeline
Category: EBSCO
Slug: PdfExtractorNotes
Authors: Peter Delaney 
Summary: EBSCO PDF Extractor Notes is for the Proof of Conc

# Useful Links

1. **platform.shared.fulltext-extractor** [URL](https://github.com/EBSCOIS/platform.shared.fulltext-extractor)  **Strategic Pipeline Code**
1. **aop-pipeline Artifactory Cloud Authorization** [URL](https://github.com/EBSCOIS/onprem-af-aop-datapipeline)
1. **Artifactory Create API Key** [URL](https://confluence.epnet.com/pages/viewpage.action?spaceKey=TCO&title=How+to+get+set+up+with+Artifactory+locally)
1. **Artifactory Cloud** [URL](https://confluence.epnet.com/display/ART/Artifactory+Cloud)

# PoC
>
>Video Recordings from Various People Helping me Testing Pdf SLS Text Extractor
>
1. **Carol Kuzel Pipeline Help**   [URL](https://web.microsoftstream.com/video/8d50deca-718e-4469-948d-c03033d0cfab)
1. **Scott Bakalyr Pipeline Help** [URL](https://web.microsoftstream.com/video/590b3b54-07b6-4438-8420-616921dd1174)
1. **Carol Kuzel SLS Training**    [URL](https://web.microsoftstream.com/video/062494ea-1478-498c-9cb8-031582dfb8b5)


# Strategic Pipeline Related Information

```bash
# Executed on command line because getting authentication errors from downloading Artifactory artifacts
./gradlew build -x bootJar -x compileTestJava


```

```bash
# Required in your ~/.gradle/gradle.properties file
ArtifactoryUser=pdelaney@corp.epnet.com
ArtifactoryPassword=AKCp8hyEYSqUNFp6nBniD29E5UhZ9m9CxfA3RiuQx2HVsJZGLskrgd4AqMMffAPK4vu2gLU5W
ArtifactoryContextUrl=https://eis.jfrog.io/eis

# Or can place the following in your build.gradle file
allprojects {
    repositories {
            maven {
               url 'https://eis.jfrog.io/eis/libs-release'
               credentials {
                    username = 'pdelaney@corp.epnet.com'
                    password = "AKCp8hyEYSqUNFp6nBniD29E5UhZ9m9CxfA3RiuQx2HVsJZGLskrgd4AqMMffAPK4vu2gLU5W"
                }
        }
    }
}

# Need to obtain password via Artifactory API Key

```

## Start Docker Container running pdftotext
```bash

# Execute Docker container
docker run --rm -i kadock/pdftotext < some.pdf > extracted.txt

```

## Start Strategic Pipelines Container in platform.shared.fulltext-extract
```bash

# Authenticate to AWS
gimme-aws-creds --profile eis-deliverydevqa

# Login to Docker Container in AWS ECR (Elastic Container Registry)
/usr/bin/aws ecr get-login --region us-east-1 --profile eis-deliverydevqa

# Execute Command spit out; Note remove the -e none, causes problems
# Also put https in front of the URL to ECR
sudo docker login -u AWS -p eyJw.......  https://872344130825.dkr.ecr.us-east-1.amazonaws.com

# Had an issue with command above
# Following site helped resolve this issue
# https://cri.dev/posts/2020-07-06-How-to-solve-Docker-docker-credential-desktop-not-installed-or-not-available-in-PATH/
# Had to alter ~/.docker/config.json file
# credsStore to credStore

# Build the Docker image
cd project/dir...
sudo docker build -t test-extract --file Dockerfile .

# See if image was created
sudo docker images | grep test-extract

# Start Container using created Image
sudo docker run -d --name extractor -p 80:80 test-extract



```
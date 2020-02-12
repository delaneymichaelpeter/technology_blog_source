Title: SonarQube Information
Date: 2020-01-12 10:20
Modified: 2010-12-12 19:30
Tags: docker, sonarqube
Slug: sonarqube-information
Authors: Peter Delaney 
Summary: Information about SonarQube and how to run it locally


[URL to Docker SonarQube] (https://hub.docker.com/_/sonarqube)


## start SonarQube in docker container
```bash
docker run -d --name sonarqube -p 9000:9000 sonarqube

# Stop Server
docker stop sonarqube

# Restart server
docker start sonarqube
```

Need to build your maven project so it deploys to the locally running docker image.
```bash
mvn clean test sonar:sonar -Dsonar.host.url=http://localhost:9000

# For StreamSets need to specify sonar.scm.disabled=true because would fail.  NOT SURE WHY
mvn clean test sonar:sonar -Dsonar.scm.disabled=true -Dsonar.host.url=http://localhost:9000
```


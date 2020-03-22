Title: Docker Commands
Date: 2020-01-12 10:20
Modified: 2020-03-22 09:30
Tags: docker, docker-compose, devops, jenkins, sonarqube
Slug: docker-commands
Authors: Peter Delaney 
Summary: Commands I use for docker


# Docker Command List


##  start container in interactive mode
```bash
docker run -it    /bin/bash

# Break out of Container
Ctl-P, Ctl-Q

# Restart a Running Container
docker run -it -d --name 'delaney'   bash

# Attache to a Running Container
docker attach delaney

# Execute a command within a running container, while outside of it
docker exec -it delaney bash

# Run Your Maven Project against sonar
mvn clean test sonar:sonar -Dsonar.host.url=http://localhost:9000

```

## start nginx in docker container
```bash
docker run -d -P nginx:latest  --name delaney

docker inspect delaney | grep IPAddress

curl
```



## start SonarQube in docker container
```bash
docker run -d --name sonarqube -p 9000:9000 sonarqube

# Stop Server
docker stop sonarqube

# Restart server
docker start sonarqube
```

## start Jenkins Server in docker container
```bash
# Start jenkins container with the volume attached for restart
docker run -ti --name receiver-jenkins -p 8080:8080 -p 50000:50000 -v jenkins-data:/var/jenkins_home jenkins/jenkins:lts

# Restart Jenkins
docker start receiver-jenkins
```


## Copy files from host to Running Docker container
```bash

# Copy text.cfg file to /tmp/ directory in container
docker cp <name-of-file-on-host> <container-name>:<directory-to-copy>
docker cp text.cfg aop:/tmp/

```

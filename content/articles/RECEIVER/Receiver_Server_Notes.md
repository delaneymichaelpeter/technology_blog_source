Title: EBSCO Receiver Application Information 
Author: Peter Delaney 
Date: 2020-01-10 9:00
Category: receiverapp 
Tags: java, receiver, devops
Slug: receiverapp-tech-notes 
Summary: Technical notes about the EBSCO Receiver Application


# ReceiverApp Important Links: 
1. [ReceiverApp Application](https://confluence.epnet.com/pages/viewpage.action?spaceKey=ART&title=ReceiverApp+Application)
2. [ReceiverApp RunBook](https://confluence.epnet.com/pages/viewpage.action?spaceKey=TEO&title=ReceiverApp+Run+Book)
3. [ReceiverPortal Application](https://confluence.epnet.com/pages/viewpage.action?spaceKey=ART&title=ReceiverPortal+Application)
4. [ReceiverPortal RunBook](https://confluence.epnet.com/pages/viewpage.action?spaceKey=TEO&title=ReceiverPortal+Run+Book)
5. [ReceiverPortal Prometheus/OpsGenie Monitoring](https://confluence.epnet.com/pages/viewpage.action?pageId=282886604)

# This is King's login
```bash
ssh builder@10.80.99.166: password:  t0pc4t
```


# Database Information
1. PROD: pdc-v-rcvrappdbp011.epnet.com:3306 rcvrappuser/rcvrappassXXX 
2. DEV: 10.80.100.62:3306  receiver kng/ebsco
3. MySql Database: http://confluence/display/ART/Receiver+App+MySQL+Database



** Installing OpsGenie on linux
**Commands Executed to install OpsGenie**
```bash
wget https://dl.google.com/go/go1.12.5.linux-amd64.tar.gz
su
tar -C /usr/local -xzf go1.12.5.linux-amd64.tar.gz
vi ~/.bash_profile
mkdir go
export GOPATH=/builder01/builder/go
export GOROOT=/usr/local/go
export PATH=$PATH:$GOROOT/bin

source ~/.bash_profile

# Make sure go installed
go -version 
ls -l $GOROOT/
ls -l $GOPATH/
```


# Download OpsGenie go files via go
**Get github.com/opsgen/opsgenie-lamp**
**If above does NOT work download via https://github.com/opsgenie/opsgenie-lamp and copy to server**
```bash
scp opsgenie-lamp-master.zip builder@10.80.99.166:~/
unzip -dv opsgenie-lamp-master.zip
```



# Jenkins Server
1. URL Shake-n-Bake: http://ese-build6.epnet.com:8080/jenkins/view/ShakenBake/ 
2. URL to Jenkins:   http://ese-build6.epnet.com:8080/jenkins/view/ShakenBake/job/ReceiverApp.Build/

# Running Jenkins in Docker
**Execute command in WSL  Need to configure Jenkins with the correct plugins**
```bash
docker run -ti --name receiver-jenkins -p 8080:8080 -p 50000:50000 -v jenkins-data:/var/jenkins_home jenkins/jenkins:lts 
docker stop receiver-jenkins
docker start receiver-jenkins
```

Title:  EBSCO AoP Notes
Date: 2020-01-22 10:20
Modified: 2021-01-15 19:30
Tags: aop, shake-n-bake
Category: EBSCO
Slug: Aop-Notes
Authors: Peter Delaney 
Summary: EBSCO Ahead of Print (AoP) Notes 

## Execute aop unit tests
```
cd <aop-directory>
gradlew clean integrationTest -DenvId=local --info


## Create VM for AOP

## Steps to Follow to create a VM
1. OpenStack EDC/SuperDelegates
2. Create VM using BIC_rhel7.3Docker_b1_s1_p1 image
3. When creating this image you will need to create a key to log into box
3.1 ssh ~/.ssh/pdelaney cloud-user@<ip-id>   Must Enter Phassphrase  'Tikal2019!'
4. Install LDAP on the Box: EBSCO Instructions: https://confluence.epnet.com/display/ese/Implement+LDAP+authentication+to+OpenStack+RHEL+VM%27s
5. Config Instructions not really working:  https://confluence.epnet.com/pages/viewpage.action?spaceKey=ese&title=Fix+nobody%3Anobody+nfs4+issue+on+RHEL+machines
6. Login

```bash
# Log into box
ssh -i ~/.ssh/pdelaney cloud-user@10.80.96.176   'Tikal2019!'

# Sudo 
su pdelaney  <ldap-password>

```

**Connect to MFSi Server via Putty**
```bash
# User to enter in putty
cloud-user

# How to stop and start tomcat server
ps -elf | grep tomcat   # Make sure tomcat is running
stopTomcat  # Stops the Server
startTomcat # Start the Server

```

### AOP VMs and userId/Password
```bash

# AOP Integration VM
ssh -i ~/.ssh/pdelaney cloud-user@10.80.96.176  PassPhrase 'Tikal2019!'

# AOP DEV VM
ssh pdelaney@10.80.96.88  'BubJd6*L'  LDAP password

# PROD DEV VM
ssh pdelaney@10.81.98.78  'BubJd6*L'  LDAP password
```
  

### Shared Directories Information

This is the list of source directories we we will look to find EPNLM content being delivered by the Strategic Pipeline

| Environment | Location of Files |
|----------------:|:----------------------------------------------------:|
|**Live:**        |\\svm-sdnnas102\aws_import_prd\EBSCONext\Usr\EBSCONext|
|**Integration:** |\\spiderstage102.epnet.com\mftarchive_staging\EBSCONext\Usr\INT_EPMarkXmls |
|**Dev:**         |\\spiderstage102.epnet.com\mftarchive_staging\EBSCONext\Usr\TeamChagall |


** Error Directory **
product/data/time/article.xml
springerjournal/01-23-2020/0102AM/name.xml

 ---

 **Few different Logins from King.  Not exactly sure which one works**

 . https://ecloud.ebsco.com  **(sdofozuser/AWfgRUye56%)**

 . https://ecloud.ebsco.com  **(slsuser/Klugt44d)**

 . https://ecloud.ebsco.com  **tbdsuser/LLhjyuc36**

 . SDC login for Stratigic Pipeline:  **(sdcuser/tr1ckyPA$s)**




Title:  EBSCO SVN Migration Notes
Date: 2021-05-18 10:20
Modified: 2021-05-18 10:20
Tags: svn, migration, shake-n-bake
Category: EBSCO
Slug: SVN-Migration-Notes
Authors: Peter Delaney 
Summary: EBSCO SVN Notes for backing up and restoring SVN repositories

Purpose of this document so we can support any SVN repository issues that may arise during a problem.


## Three Use Cases SVN Scripts
1. SVN Server goes Down; (Need to create New Instances, restore SVN artifacts and swap DNS IPs for Jenkins Servers)
2. Network Share goes Down; (May require us to restore some SVN repositories)
3. Daily cronjob backups broken; (May need to fix the cronjob)

 ---
 
## UseCase: (SVN Server Goes Down Steps)

Need to Provision a new P9 Instance on Region/Tenant PDC/VersionControl in this [URL](https://ecloud.ebsco.com/clarity/index.html#/signin)   id : **versioncontrol/VhEyBXk7-yjLLUUF**

### Create new P9 Instance from Snapshot
1. Go to P9 and login https://ecloud.ebsco.com/clarity/index.html#/signin.   Credentials: **versioncontrol/VhEyBXk7-yjLLUUF**
2. Select "Openstack" in left menu
3. Select Region: **PDC** in upper right corner.
4. Select "Instances" below **Openstack**
5. Press "+ Instance"
6. Select image **svn-replatforming-4**
7. Press "Next"
8. Select availability zone **HA**
9. Select instance type/flavor **centos.s1.large**
10. Press "Next"
11. Select network **external**
12. Press "Next"
13. Fill-in the following fields:
14. Instance Name **svn-replatforming-4** (any unique name)
15. SSH Key **svn-replatforming**. We used ssh-keygen -t rsa to generate keys. Below you can find these private and public keys attached to this article.
16. Security Groups "default"
17. Press "Finish"
18. Press "Create instance

All scripts and network mounts should be already established from the **svn-replatforming-4** image

Remote Shell into machine
```bash
ssh -i ~/.ssh/svn-migration_rsa cloud-user@HOST-IP
```

###  DNS Names to IP Addresses
1. The Jenkins Server that execute the Builds needs to have access to the new IP. Start Powershell in Admin Mode: **Start-Process -FilePath "powershell" -Verb RunAs**
2. If Production Jenkins Server Need to talk to **IE.Storage & Virtualization Team** to (Mary DelGado) to map new IP to DNS
3. If NOT production change hosts file on Windows machine **c:\Windows\system32\drivers\etc\hosts**


 ---  

## UseCase: (Network Share Goes Down)
In this scenario we need to restore some SVN repositories

**URL Confluence**

[Confluence Page SVN Backup](https://confluence.epnet.com/display/ART/SVN+backup+and+recovery#SVNbackupandrecovery-1.RestorefromSVNbackups)


### Create P9 Instance from Snapshot follow instructions:

[Confluence Page Instructions](https://confluence.epnet.com/display/ART/SVN+backup+and+recovery#SVNbackupandrecovery-Creatingnewinstance)

### Execute shell scripts on newly create P9 Instance
```bash

> sudo su - 

# 1 Create Svn dump of repository
# Set character handling
> export LC_CTYPE=en_US.utf8

# Backup dbadv repo to /tmp/ directory
> mkdir /tmp/backup
> /root/scripts/svn-backup-dumps.py /repos1/dbadv/ /tmp/backup/

# View Log
cat /tmp/dbadv.... | less

# 2 Restore Svn dump
> mkdir /tmp/restore
> /root/scripts/svn-backup-restore.py --l=dbadv /tmp/backup /tmp/restore

# 3 Test Repo
> cd /tmp
> mkdir test
> cd test
> svn log file:///tmp/restore/dbadv 
> svn co  file:///tmp/restore/dbadv 

# Setup new mounts for testing
> umount /repos1
> mv /tmp/restore/dbadv /repos1/

# Testing Restore via Browser
# Change your local hosts DNS to point to the new IP of this server
# In Browser got to dbadv.svn.epnet.com  
# If this works or looks good Tell Virtualization Team to swap DNS to new IPs


```

 ---  

## UseCase: (CronJob Not working)

There is a crond job that runs via systemd.  If something is wrong or it is not working look at the script

```bash
> systemctl status crond
> cat /usr/lib/systemd/system/crond.service | less

# Script resides int
vi /root/scripts/svn-backup-dumps.sh

# 


```
 ---  

## OTHER INFORMATION


### SVN Server Create From Scratch

#### Create P9 Instance Server

1. Go to P9 and login https://ecloud.ebsco.com/clarity/index.html#/signin. **versioncontrol/VhEyBXk7-yjLLUUF**
2. Select "Openstack" in left menu
3. Select Region: **PDC** in upper right corner.
4. Select "Instances" below **Openstack**
5. Press "+ Instance"
6. Select image **BIC-CentOS7-2020-05-21** 
7. Press "Next"
8. Select availability zone "HA"
9. Select instance type/flavor **centos.s1.large**
10. Press "Next"
11. Select network **external**
12. Press "Next"
13. Fill-in the following fields:
14. SSH Key "svn-replatforming". We used ssh-keygen -t rsa to generate keys. Below you can find these private and public keys attached to this article.
15. Security Groups "default"
16. Press "Finish"
17. Press "Create instance


#### Execute commands


Need to ftp tar file to server and execute

```bash
# clone Git repository to local directory
> git clone https://github.com/EBSCOIS/onprem.infrastructure.svn

# Ftp to Server
> cd onprem.instrustructure.svn
> scp svnPackage.tgz cloud-user@HOST_IP:/tmp

# ssh to new Server
> ssh cloud-user@HOST_IP mkdir -p /tmp/svnPackageExtracted
> tar -xf /tmp/svnPackage.tgz --directory /tmp/svnPackageExtracted
> cd /tmp/svnPackageExtracted

# Execute run script
> su
> cd tmp/
> ./run.sh

```

#### Mount Network Shares


**/etc/fstab**

tiffarchive101:/vol/svn_backup on /svndump type nfs4 (rw,relatime,vers=4.0,rsize=65536,wsize=65536,namlen=255,hard,proto=tcp,timeo=600,retrans=2,sec=sys,clientaddr=10.81.96.13,local_lock=none,addr=10.68.50.50)

svm-cdnnas102:/vol/svn_master  on /repos1  type nfs4 (rw,relatime,vers=4.0,rsize=65536,wsize=65536,namlen=255,hard,proto=tcp,timeo=600,retrans=2,sec=sys,clientaddr=10.81.96.13,local_lock=none,addr=10.68.17.84)


#### Jenkins Server Information

http://10.81.96.182:8080/view/dev-app/   (jenkins_test_user/testing5)

**Three Jenkins Builds in DEV**
1. dev-app-BookBuilderX-Sam-2021          http://ddd.svn.epnet.com/repo/Applications/NetLibrary/BookCitationBuilder/trunk
2. dev-app-DbTitleListLoader-2.25.1-x1    http://de.svn.epnet.com/dbsys/dbi/Applications/EdsPubBrowse/DbTitleListLoader/trunk
3. dev-app-JournalDetailBuilderX7         http://ddd.svn.epnet.com/repo/Applications/JournalDetailBuilder/trunk
4. dev-app-JournalDetailBuilderX7x1       http://ddd.svn.epnet.com/repo/Applications/JournalDetailBuilder/trunk

**Server in Prod**
1. dev-prod-ffh                           http://ddd.svn.epnet.com/repo/Projects/ffh/trunk


##### Windows Remote Shell to Jenkins Server
Windows Remote Client to : **10.81.96.182**   userid/pass  **svc_devaw / Ju$t4d&v**
Need to do this to alter the c:\Windows\system32\driver\etc\hosts file


##### THESE ARE TEST REPOS
ddddesign - http://ddd.svn.epnet.com/design
dddqarepo - http://ddd.svn.epnet.com/qa
dbadv     - http://dbadv.svn.epnet.com/repo


 ---  

## Important Links

 **EBSCO Links**

 . [OpenStack P9 login](https://ecloud.ebsco.com/clarity/index.html#/signin)  **versioncontrol/VhEyBXk7-yjLLUUF**

 . [Svn Backup/Recovery Confluence Page](https://confluence.epnet.com/pages/viewpage.action?spaceKey=ART&title=SVN+backup+and+recovery)

 . [GIT Repository backup Scripts](https://github.com/EBSCOIS/onprem.infrastructure.svn)

 . [Training Recording](https://ebscoind-my.sharepoint.com/:v:/g/personal/pdelaney_corp_epnet_com/EVP_vH92XTdFhhEyhwfiL-QBgJpUSlH6qxBsX7LtqIMSSQ?e=tMsQqv)

 . [Training Last Recording](https://ebscoind-my.sharepoint.com/personal/susau_corp_epnet_com/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fsusau%5Fcorp%5Fepnet%5Fcom%2FDocuments%2FRecordings%2FSVN%20backuping%20and%20recovery%2D20210519%5F120510%2DMeeting%20Recording%2Emp4&parent=%2Fpersonal%2Fsusau%5Fcorp%5Fepnet%5Fcom%2FDocuments%2FRecordings&originalPath=aHR0cHM6Ly9lYnNjb2luZC1teS5zaGFyZXBvaW50LmNvbS86djovZy9wZXJzb25hbC9zdXNhdV9jb3JwX2VwbmV0X2NvbS9FWFJjbkVsWXlFbEdySkJna0JQX3JUSUJjLWxJaW5UeUxOT0R0TE1UV0prVnlnP3J0aW1lPW56YS1tc3dhMlVn)

 . [Training Recording Orig](https://web.microsoftstream.com/video/3d909eec-752d-4ca5-8164-cebb514c4bf6?App=msteamsBot&refId=f:f20e8175-e53f-6819-4f11-ee55448c3379)


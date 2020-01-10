Title: EBSCO SLS (Shared Loader Service)
Author: Peter Delaney 
Date: 2020-01-10 9:00
Category: SLS
Tags: java, sls, devops, activemq, camel, nodejs
Slug: sls-tech-notes 
Summary: Tech Notes for SLS.  SLS is a Camel implementation 

### Technical Notes Related to SLS (Shared Loader Service)
This is a collection of Notes I've captured to support the SLS Pipeline

## Important Confluence URL: 
* [SLS Training for Developers](http://confluence/display/ART/SLS+Training+for+Developers)
* [SLS Defects and Escalations](http://confluence/display/ART/SLS+Defects+and+Escalations)
* [SLS Diagnostic Checklis](http://confluence/display/esd/SLS+Diagnostic+Checklis)
* [SLS Training Portal](http://confluence/display/ddp/SLS+Training+Portal)
* [SLS Problem Resolution and Triage](http://confluence/display/esd/SLS+Problem+Resolution+and+Triage)
* [URL to Carols Training](https://web.microsoftstream.com/video/062494ea-1478-498c-9cb8-031582dfb8b5)
* [Grafana URL](http://grafana-live.epnet.com/?orgId=1)
---

### Command to start/stop/update/list Pipeline Jobs
1. **StopJob:**
..* http://10.80.97.81:8080/dpl/admin/stopJob    admin/secret
..* Select the Stop Button

2. **Sometime Job get stuck Need to execute**
..* http://10.80.97.81:8080/dpl/admin/updateJob    admin/secret
..* Enter Job Id that you see from the List Jobs

3. **List Job:**
..* http://10.80.97.81:8080/dpl/loaderService/activeReport

4. **Start a Job:**
..* Execute POST request to: http://10.80.97.81:8080/dpl/loaderService  via Postman

---

### Deploying Pipeline to PROD 
1. Go To Jenkins URL:  http://as-bse-jenkins:8080/
2. Go to "DPL" Jobs
3. Go to "Deploy DPL releast to Live"
4. "Build with Paramters"
5. Once here select on the Release interested in.

**After build finished. To to URL of each of the Servers see if your version is deployed**
Ex: http://pdc-v-slsconl05.epnet.com/dpl/version.html


### Prometheus Queries
```console
cpu_usage_system{epn="Shared Loader Service (SLS)",host=~"pdc-v-slsftxl11.epnet.com|pdc-v-slsftxl12.epnet.com"}
```

#### Profiler JSON Post Input:
Notes to KickOff SLS/DPL
**Loader Service URL:** http://10.80.97.81:8080/dpl/loaderService
**Profiling Service URL:** http://10.80.97.81:8080/dpl/profile
```json
{
"inputPath" : "/edsloader/openfiler101/ddd-data1/data_profiling/iso_test",
"outputPath" : "/edsloader/bigfoot/bigfoot_shared/sls/output/iso_test/marcxml",
"loggingPath" : "/edsloader/bigfoot/bigfoot_shared/sls/output/iso_test/logs",
"recursive" : true,
"regexInclude":[".*xml"],
"fileEncoding": "ISO-8859-1",
"xmlSplit" : false,
"filterXmlTags":["text"],
"productCode": "isotest_gml",
"database": "isotest_gml",
"mongoDb" : "isotest_gml",
"urlProductCode" : "isotest_gml"
}
```


####  LoaderService JSON Post Input: ####
```json
{
"inputPath" : "/edsloader/openfiler101/ddd-data1/data_profiling/iso_test",
"outputPath" : "/edsloader/bigfoot/bigfoot_shared/sls/output/iso_test/marcxml",
"loggingPath" : "/edsloader/bigfoot/bigfoot_shared/sls/output/iso_test/logs",
"recursive" : true,
"regexInclude":[".*xml"],
"fileEncoding": "ISO-8859-1",
"xmlSplit" : false,
"filterXmlTags":["text"],
"productCode": "isotest_gml",
"productVersion": "isotest_gml_5461",
"database": "isotest_gml",
"mongoDb" : "isotest_gml",
"urlProductCode" : "isotest_gml",
"buildType": "rebuild",
"productBuild": "0007410392-292",
"buildId": "0007410392-292"
}
```

SSH To Server:  ssh root@10.80.97.81    password=Ebsco!!!


# FullText Server Specific Information

### **Deploy FullText Server**
1. Go to Jenkins: http://as-bse-jenkins:9080/jenkins/
2. **FullTextServiceOnDemand**
3. **Execute a Build.  Don't run the Test**
4. **Must put the name of the release that maps to what is in GIT**

   [GIT](http://as-gitmaster.epnet.com:7990/projects/EDS_PARTNERS/repos/fulltextservice/browse?at=refs%2Fheads%2Frelease%2F2.3.2)

5. **After Building Download the FulltextService-2.X.X.zip from "Last Successful Artifacts"**

   Upload this to the Server and extract to a directory FTSrcvr2.X.X

6. This page helps with managing the configuration files for the FullText and MappingService

   https://confluence.epnet.com/pages/viewpage.action?spaceKey=ART&title=SLS+in+L-INT+-+KB

7. **Once you've logged in into server**
  ..* Make sure NODE_ENV=xxxx  is set correctly
  ..* Look in .bashrc .bash_profile for both slsuser and root.
     NODE_ENV=production
     NODE_ENV=lint


### **Establish xslt4node link**
```bash
cd current/node_modules
rm -rf xslt4node/
# This works on PROD
npm link xslt4node 
# This one had to do in LINT
ln -s /opt/rh/rh-nodejs4/root/usr/lib/node_modules/xslt4node xslt4node

# Establish new link to new directory
ln -sfnv FTSrvc2.X.X/ current

# Start server
Now Start the Server
cd current/
forever start app.js
```

# Check Log files in /root/.forever

### To Stop/Start FullText
```bash
cd current
forever start/stop app.js
/root/.forever/  
```


# **Single SignOn LDAP**
pdelaney/BubJd6*L

Need to figure out a way to change the password to the LDAP Server.  Don't like this password

##### HOW TO Run Pipeline in DEV
  I kick off a Job using Postman:  The configuration was given to me by Carol.  
  Need to understand the parameter or JSON in and where to get this information.

  Active Job: http://10.80.97.81:8080/dpl/loaderService/activeReport
  Stop Job:   http://10.80.97.81:8080/dpl/admin/stopJob
  Update Job: http://10.80.97.81:8080/dpl/admin/updateJob



### **MySql Database Info**
There is a MySql database that most of the application access.

Confluence: https://confluence.epnet.com/pages/viewpage.action?spaceKey=esd&title=SLS+Diagnostic+Checklist#SLSDiagnosticChecklist-MySQLproductloaderdatabase

Machine and userId/password
DEV:  10.80.98.196   pls_write/pls_write  sid:productloader
QA:   10.80.97.129   pls_write/pls_write  sid:productloader
PROD: pdc-v-slsmysl01.epnet.com devreader/spectator  sid:productloader

** Queries**
##### Shows you all of the Hosts that are connected to the MySql
show processlist;

##### Shows the Connection information to the Database
show status like '%ono%';
select * from INFORMATION_SCHEMA.processlist where db='productloader' and host like '%slsmps%';



# **ActiveMQ**
Appears that the ActiveMQ queue reside on the same machine as the MySql server machines.

To get to the admin page of the ActiveMQ for each environment, you could go to URL where MySql database is.
GoTo: http://<my-sql-server-ip>:8161   admin/admin

Another way is to go to vTest page Producer.  vTest page for Producer is in the "SLS Diagnostic Checklist"
Go there and in the vTest page results you will see 'myBrokerUrl'.  This is the URL that the Producer pushes messages
into the queue.

Take that URL and replace the port with 8161 from 61616
Example: myBrokerUrl tcp://10.80.97.129:61616 REPLACE with http://10.80.97.129:8161


# AVI LoadBalancer Information
AVI is the OpenStack LoadBalancers
LINT URL: https://ecloud-edc-avi.ebsco.com/#!/login
PROD URL: https://ecloud-pdc-avi.ebsco.com/#!/login slsuser/Klugt44d

userId/password:  slsuser/Klugt44d  


# **Step to Push New FullText Server into PROD**
1) Stage the new Servers with software 
1.1) Touch files on the servers with values of Old/New.  This will assure you that the DNS changes were correct
2) Test the new servers 
2) Run the vtest page on the server
2) Had problem with image used.  The /sls-lookup symbolic link is not correct.
```console
   Need to do following
   > cd /
   > cd slslookup
   > unlink sls-lookup/
   > cd ..
   > rmdir slslookup
   > ln -s /prod-nas105/licenseddata/slslookup/  /sls-lookup
   ```
   Go to vtest page to make sure lookUpTest is OK
3) Stop Server Monitoring via Nagios
4) Swap IP, need the ISO.CloudEngineering Team to Swap IP.  Create a UserStory on their Board
5) FullText LoadBalancers AVI (https://ecloud-pdc-avi.ebsco.com/  slsuser/Klugt44d)
   Make sure the LoadBalancer on the particular Pipeline is pointing to the new server IPs.
6) Have Database Pipeline Team (Fevie, Hal or Susan Kelsch) run test so you can monitor the activity
7) Turn Nagios Monitoring back on


## Creating Mount in /etc/fstab for SLS Server Notes
1. Create Directory
2. Execute Mount command or add entry to /etc/fstab

#### Entry in /etc/fstab
svm-archive101.epnet.com:/springer_archive/Springer                         /edsloader/svm-archive101/springer_archive/Springer  nfs    proto=tcp,vers=3,rw,rsize=65536,wsize=65536,intr 0 0

#### findmnt command
|-/edsloader/svm-archive101/springer_archive/Springer
            svm-archive101.epnet.com:/springer_archive/Springer
                          nfs         rw,relatime,vers=3,rsize=65536,wsize=65536,namlen=255,hard,proto=tcp,timeo=600,retrans=2,sec=sys,mountaddr=10.68.50.195,mountvers

After editing /etc/fstab need to execute following command
```bash
mount -a
```







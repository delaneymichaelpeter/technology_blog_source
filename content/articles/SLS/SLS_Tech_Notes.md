Title: EBSCO SLS (Shared Loader Service)
Author: Peter Delaney 
Date: 2020-01-10 9:00
Category: sls 
Tags: java, sls, devops, activemq, camel, nodejs
Slug: sls-tech-notes 
Summary: Tech Notes for SLS.  SLS is a Camel implementation 

# Technical Notes Related to SLS (Shared Loader Service)


# Stop Jobs in SLS Pipeline
## Stop Job
http://10.80.97.81:8080/dpl/admin/stopJob    admin/secret

## UpdateJob Sometime Job get stuck Need to execute
http://10.80.97.81:8080/dpl/admin/updateJob    admin/secret
Enter Job Id that you see from the List Jobs

## List Job:
http://10.80.97.81:8080/dpl/loaderService/activeReport

## Start a Job:
Execute POST request to: http://10.80.97.81:8080/dpl/loaderService  via Postman


** COPY PASTE WORK ON CODE BELOW THIS LINE**

* Confluence URL: 
http://confluence/display/ART/SLS+Training+for+Developers    Carol's training pag

http://confluence/pages/viewpage.action?pageId=124237123
http://confluence/display/ART/SLS+Training+for+Developers
http://confluence/display/ART/SLS+Defects+and+Escalations
http://confluence/display/esd/SLS+Diagnostic+Checklis
http://confluence/display/ddp/SLS+Training+Portal
http://confluence/display/esd/SLS+Problem+Resolution+and+Triage


URL to Carols Training: https://web.microsoftstream.com/video/062494ea-1478-498c-9cb8-031582dfb8b5


######  SLS URL ######
Grafana URL: http://grafana-live.epnet.com/?orgId=1

# Not sure what this URL is saw in Carol's training
http://pdc-v-slsprol01.epnet.com:8080/dpl/loaderService/activeReport

---------------------------------------------------------------------


* DEV Pipeline
StopJob:  
http://10.80.97.81:8080/dpl/admin/stopJob    admin/secret
Select the Stop Button

Sometime Job get stuck Need to execute
http://10.80.97.81:8080/dpl/admin/updateJob    admin/secret
Enter Job Id that you see from the List Jobs

List Job:
http://10.80.97.81:8080/dpl/loaderService/activeReport


Start a Job:
Execute POST request to: http://10.80.97.81:8080/dpl/loaderService  via Postman


* Deploying Pipeline to PROD 
Go To Jenkins URL:  http://as-bse-jenkins:8080/
Go to "DPL" Jobs
Go to "Deploy DPL releast to Live"
"Build with Paramters"
Once here select on the Release interested in.

After build finished. To to URL of each of the Servers see if your version is deployed
Ex: http://pdc-v-slsconl05.epnet.com/dpl/version.html

Steps Must Take to Deploy to Live
) Stop Notification via Nagios
) Go to Jenkins and execute Build
) 


* Prometheus Queries
cpu_usage_system{epn="Shared Loader Service (SLS)",host=~"pdc-v-slsftxl11.epnet.com|pdc-v-slsftxl12.epnet.com"}




* Alena's Efforts
She is doing great work.  Here is what she has done.
Alena has modified the FullText/NodeJs application to expose metrics.  The first version she worked that shows the UI page
was using one library.  She is working on a second version of that that is exposing Prometheus metrics.  Something that Prometheus
could pull in easily.

Metrics Alena is trying to capture:
nodejs_memory_usage_rss:
nodejs_memory_usage_heap_total:
nodejs_memory_usage_heap_used:
nodejs_memory_usage_external:
nodejs_gc_duration: (seconds from start to end of GC)
nodejs_eventloop_max: (longest sampled latency for processing an event)
nodejs_eventloop_min: (shortest sampled latency for processing an event)
nodejs_eventloop_sum: (mean sampled latency for processing an event)
nodejs_http:-duration_ms: (time taken for the HTTP request to respond)


What Alena has left TODO:
 - Fix up her code, the Prometheus code.
 - Test this in her machine.  Alena sends Postman POST requests to the FullText Service to perform her testing
 - Need to test this in some kind of Pre-Prod environment, these changes before introducing to PROD
 - Need to setup Prometheus Monitoring this EndPoint to make sure that information is pulled in appropriately
 
Dependencies:
 - LiveOps to allow for us to Pull these Metrics
 - Testing of these changes to FullText Service.

My Recommendation:
 - Go with Infrustructure metrics first
 - Have Alena continue with exposing custom FullText metrics along with testing it
 - 


* Notes to KickOff SLS/DPL
Loader Service URL: http://10.80.97.81:8080/dpl/loaderService
Profiling Service URL: http://10.80.97.81:8080/dpl/profile

#### Profiler JSON Post Input: ####
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


####  LoaderService JSON Post Input: ####
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

Note: to get to filesystem remove the \\edsloader\
To get the results execute in browser: http://10.80.97.81:8080/dpl/loaderService/{id-coming-back-in-request}

SSH To Server:  ssh root@10.80.97.81    password=Ebsco!!!



* Test Files From Caral Kuzel
LAH data - xml files in ISO-8859-1 format.
Documentation: http://confluence/pages/viewpage.action?pageId=203950027
Data location: \\spider\mirror\production\sftp.cabi.org\Cabixml\


* Notes From Caral Kuzel Training

vTest is the application that gives a status of the system.  There are different URL for each of the services.
vTest is just-in-time, meaning that the results of the status is checked real-time, not just pulled from a database.


Terminology
stopjob:  not sure what this is
vTest: this an application for checking status of the application

Problem Trouble Shooting:
Environment: get a graffana board that is not working at the moment.
Data Related: Files trying to process are very large.  Could be a format change to i
Scriptiong:  use regex could be too large.  Also custom script problems.  Sometime custom javascript will come in when custom javascript is passed in.
    Carol says it is an undefined variable in the Javascript that causes problems.

Problem Resolution:

Mapping Service:  rerun NodeService









* ISO-8859 Bug Notes
  URL to xml files that were causing us problems
\\openfiler101\ddd-data1\data_profiling\iso_test
Notice that the xml files have encoding ISO-8859-1 in the xml preamble.


* SLS Machine Access
To ssh to a particular machine execute following
> ssh -i .ssh/slsuser_user slsuser@<ip.of.machine>:8080


* Deploy FullText Server
Go to Jenkins: http://as-bse-jenkins:9080/jenkins/
FullTextServiceOnDemand
Execute a Build.  Don't run the Test
Must put the name of the release that maps to what is in GIT

GIT: http://as-gitmaster.epnet.com:7990/projects/EDS_PARTNERS/repos/fulltextservice/browse?at=refs%2Fheads%2Frelease%2F2.3.2


After Building Download the FulltextService-2.X.X.zip from "Last Successful Artifacts"

Upload this to the Server and extract to a directory FTSrcvr2.X.X

# This page helps with managing the configuration files for the FullText and MappingService
https://confluence.epnet.com/pages/viewpage.action?spaceKey=ART&title=SLS+in+L-INT+-+KB

# Once you've logged in into server
# Make sure NODE_ENV=xxxx  is set correctly
# Look in .bashrc .bash_profile for both slsuser and root.
NODE_ENV=production
NODE_ENV=lint

# Establish xslt4node link
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

# Check Log files in /root/.forever
# Check vtest page





* Access to DEV FullText Servers
ssh root@10.80.97.58  Ebsco!!!

Server Where Alena has here code on.  
10.80.96.30  root/Ebsco!!!

To Stop/Start FullText
> cd current
> forever start/stop app.js

Log files reside in:  /root/.forever/ directory

* Single SignOn LDAP 
pdelaney/BubJd6*L

Need to figure out a way to change the password to the LDAP Server.  Don't like this password

* HOW TO Run Pipeline in DEV
  I kick off a Job using Postman:  The configuration was given to me by Carol.  
  Need to understand the parameter or JSON in and where to get this information.

  Active Job: http://10.80.97.81:8080/dpl/loaderService/activeReport
  Stop Job:   http://10.80.97.81:8080/dpl/admin/stopJob
  Update Job: http://10.80.97.81:8080/dpl/admin/updateJob



* MySql Database Info
There is a MySql database that most of the application access.

Confluence: https://confluence.epnet.com/pages/viewpage.action?spaceKey=esd&title=SLS+Diagnostic+Checklist#SLSDiagnosticChecklist-MySQLproductloaderdatabase

Machine and userId/password
DEV:  10.80.98.196   pls_write/pls_write  sid:productloader
QA:   10.80.97.129   pls_write/pls_write  sid:productloader
PROD: pdc-v-slsmysl01.epnet.com devreader/spectator  sid:productloader

** Queries
# Shows you all of the Hosts that are connected to the MySql
show processlist;

# Shows the Connection information to the Database
show status like '%ono%';
select * from INFORMATION_SCHEMA.processlist where db='productloader' and host like '%slsmps%';



* ActiveMQ
Appears that the ActiveMQ queue reside on the same machine as the MySql server machines.

To get to the admin page of the ActiveMQ for each environment, you could go to URL where MySql database is.
GoTo: http://<my-sql-server-ip>:8161   admin/admin

Another way is to go to vTest page Producer.  vTest page for Producer is in the "SLS Diagnostic Checklist"
Go there and in the vTest page results you will see 'myBrokerUrl'.  This is the URL that the Producer pushes messages
into the queue.

Take that URL and replace the port with 8161 from 61616
Example: myBrokerUrl tcp://10.80.97.129:61616 REPLACE with http://10.80.97.129:8161


* AVI LoadBalancer Information
AVI is the OpenStack LoadBalancers
LINT URL: https://ecloud-edc-avi.ebsco.com/#!/login
PROD URL: https://ecloud-pdc-avi.ebsco.com/#!/login slsuser/Klugt44d

userId/password:  slsuser/Klugt44d  


* Openstack Tenant Login Prod
https://ecloud.ebsco.com  slsuser/Klugt44d
https://ecloud.ebsco.com  sdofozuser/AWfgRUye56%


* OpenStack Creating a NEW VM
Select Instances Buttons on Left
On far right select "NEW VM INSTANCE"	
This will take you to the Create New Instance Page.
Follow steps accordingly


* Step to Push New FullText Server into PROD
1) Stage the new Servers with software 
1.1) Touch files on the servers with values of Old/New.  This will assure you that the DNS changes were correct
2) Test the new servers 
2) Run the vtest page on the server
2) Had problem with image used.  The /sls-lookup symbolic link is not correct.
   Need to do following
   > cd /
   > cd slslookup
   > unlink sls-lookup/
   > cd ..
   > rmdir slslookup
   > ln -s /prod-nas105/licenseddata/slslookup/  /sls-lookup
   Go to vtest page to make sure lookUpTest is OK
3) Stop Server Monitoring via Nagios
4) Swap IP, need the ISO.CloudEngineering Team to Swap IP.  Create a UserStory on their Board
5) FullText LoadBalancers AVI (https://ecloud-pdc-avi.ebsco.com/  slsuser/Klugt44d)
   Make sure the LoadBalancer on the particular Pipeline is pointing to the new server IPs.
6) Have Database Pipeline Team (Fevie, Hal or Susan Kelsch) run test so you can monitor the activity
7) Turn Nagios Monitoring back on


# Creating Mount in /etc/fstab for SLS Server Notes
1) Create Directory
2) Execute Mount command or add entry to /etc/fstab

# Entry in /etc/fstab
svm-archive101.epnet.com:/springer_archive/Springer                         /edsloader/svm-archive101/springer_archive/Springer  nfs    proto=tcp,vers=3,rw,rsize=65536,wsize=65536,intr 0 0

# findmnt command
|-/edsloader/svm-archive101/springer_archive/Springer
            svm-archive101.epnet.com:/springer_archive/Springer
                          nfs         rw,relatime,vers=3,rsize=65536,wsize=65536,namlen=255,hard,proto=tcp,timeo=600,retrans=2,sec=sys,mountaddr=10.68.50.195,mountvers

After editing /etc/fstab need to execute following command
> mount -a
which will refresh it









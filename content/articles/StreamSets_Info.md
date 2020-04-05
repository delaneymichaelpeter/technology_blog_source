Title:  StreamSets Data Collector Information
Author: Peter Delaney 
Date: 2020-01-31 11:45
Modified: 2020-02-27 11:45
Tags: streamsets, sdc, dataops, apache, etl
Slug: streamsets-datacollector-info 
Summary: Information about Streamsets DataCollector.  EBSCO uses this   


### Installing Source Code  

[StreamSets Notes on Building](https://github.com/streamsets/datacollector/blob/master/BUILD.md)

**Get lastest software from GitHub and build**
```bash

# Clone api
git clone http://github.com/streamsets/datacollector-api

# Clone plugin
git clone http://github.com/streamsets/datacollector-plugin-api
# Execute maven build in each directory to download needed artifacts mvn clean install -DskipTests

# Need artifacts for Edge Streamset as well. Need to download these
git clone https://github.com/streamsets/datacollector-edge.git

# Build edge using grade
./gradlew clean dist publishToMavenLocal

# Download actual source code
git clone http://github.com/streamsets/datacollector

```


## sdc.properties file
[StreamSets Properties](https://streamsets.com/documentation/datacollector/latest/help/datacollector/UserGuide/Configuration/DCConfig.html#task_lxk_kjw_1r)


## Installing Custom Java Components

This is where I put my zip extractor.  Works for me, not sure if this is the correct place

Directory to install 


## Create Custom Java maven Project
```bash
# Execute on command line and answer questions
mvn archetype:generate -DarchetypeGroupId=com.streamsets -DarchetypeArtifactId=streamsets-datacollector-stage-lib-tutorial -DarchetypeVersion=2.1.0.0 -DinteractiveMode=true
=======
**/opt/streamsets-datacollector/user-libs/zip-file-extract/lib/zip-file-extract-1.0-SNAPSHOT.jar**

Appears they want a directory like so.  Need to look into if really belongs there

When adding a new jar file one needs to grant security so that the file can be read by sdc in **/etc/sdc/sdc-security-policy** file need to add following entry

```bash

// User stage libraries code base:
grant codebase "file://${sdc.userLibs.dir}/-" {
  permission java.util.PropertyPermission "*", "read";
  permission java.lang.RuntimePermission "accessDeclaredMembers";
  permission java.lang.reflect.ReflectPermission "suppressAccessChecks";
  permission java.io.FilePermission "${sdc.dist.dir}/user-libs/streamsets-datacollector-dev-lib/lib/*", "read";
  permission java.io.FilePermission "/tmp/STREAMSETS/OUTPUT/UNZIPDIR/-", "read,write,delete";
 };

// Add our new jar file directory so has permissions
grant codebase "file://${sdc.userLibs.dir}/zip-file-extract/-" {
  permission java.io.FilePermission "/tmp/STREAMSETS/OUTPUT/UNZIPDIR/-", "read,write,execute,delete";
  permission java.io.FilePermission "/tmp/STREAMSETS/-",                 "read,write,execute,delete";
  permission java.io.FilePermission "/tmp/RECEIVER/-",                   "read,write,execute,delete";
  permission java.lang.RuntimePermission "accessUserInformation";
};


# Build project
mvn clean package -DskipTests
```

## Running StreamSets in Docker container
```bash
# Build Container
# -d run in backgroudn
# --restart restart only if container exits with a non-zero exit status
# --name name of the container
# -p port being exposed
docker run --restart on-failure -p 18630:18630 -d --name sdc streamsets/datacollector

# Display Running Container
docker ps

# Attach via bash to running container
docker exec -it sdc bash

# To Exit out of Bash Ctr-D

# Show logs from sdc
docker logs sdc

# Remove Container
docker rm -f sdc
```

## Remote Debugging Java Custom Processor

## Build Script deployment

## Maven Artifact Create Project
Command to execute to build a new Custom Java project for Streamsets
```bash
# Create Maven Project
mvn archetype:generate -DarchetypeGroupId=com.streamsets \
-DarchetypeArtifactId=streamsets-datacollector-stage-lib-tutorial \
-DarchetypeVersion=3.5.2 -DinteractiveMode=true
```






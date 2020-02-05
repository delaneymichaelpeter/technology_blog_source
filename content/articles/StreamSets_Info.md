Title:  StreamSets Data Collector Information
Author: Peter Delaney 
Date: 2020-01-31 11:45
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

```


## Remote Debugging Java Custom Processor

## Build Script deployment





Title:  StreamSets Data Collector Information
Author: Peter Delaney 
Date: 2020-01-24 9:00
Tags: streamsets, dataops, apache
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

# Execute maven build in each directory to download needed artifacts
mvn clean install -DskipTests

# Need artifacts for Edge Streamset as well. Need to download these
git clone https://github.com/streamsets/datacollector-edge.git

# Build edge using grade
./gradlew clean dist publishToMavenLocal

# Download actual source code
git clone http://github.com/streamsets/datacollector


```

## Create Custom Java maven Project
```bash
# Execute on command line and answer questions
mvn archetype:generate -DarchetypeGroupId=com.streamsets -DarchetypeArtifactId=streamsets-datacollector-stage-lib-tutorial -DarchetypeVersion=2.1.0.0 -DinteractiveMode=true

# Build project
mvn clean package -DskipTests
```


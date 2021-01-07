Title:  EBSCO MFSi Notes
Date: 2020-11-02 10:20
Modified: 2020-11-02 19:30
Tags: mfsi, shake-n-bake
Category: EBSCO
Slug: MFSI-Notes
Authors: Peter Delaney 
Summary: EBSCO MFSi REST Service

## Clean Out the MFSi PDF Queue


```bash
# Execute Stored Procedure in Oracle Developer
truncat table MFSI_PDF_NOTIFY


```

** Docker-Compose for MFSi and AoP Pipeline
```bash

version: "3.7"

services:

  MFSi:
      image: af-docker.epnet.com/openjdk-8

    container_name: MFSi
    ports:
      - "8080:8080"

    command: /usr/bin/java -jar /opt/MFSi/MFSi.jar

    volumes:
        - ./build/libs/MFSi.jar:/opt/MFSi/MFSi.jar
	- c:\opt\cdf\config:/opt/cdf/config

  MFSi2:
      image: mfsi-docker

    container_name: MFSi2
    ports:
      - "8080"

    volumes:
        - ./build/libs/MFSi.jar:/opt/MFSi/MFSi.jar
	- c:\opt\cdf\config:/opt/cdf/config

  AOPStreamSets:
      image: af-docker.epnet.com/aopdatapipeline:latest
      container_name: AopStreamSets

    ports:
        - "8080"
	- "2005:2005"
	- "800:800"
	- "8778:8778"

  AOPStreamSets2:
      image: af-docker.epnet.com/aopdatapipeline:latest
          container_name: AopStreamSets2

    ports:
        - "8080"
	- "2006:2006"
	- "801:801"
	- "8779:8779"

```


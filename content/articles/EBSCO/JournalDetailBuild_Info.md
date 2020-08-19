Title:  EBSCO Journal Detail Builder (JDB) Information
Date: 2020-08-19 10:20
Modified: 2020-08-18 19:30
Tags: automic-one, shake-n-bake, jdb, journaldetailbuilder
Category: EBSCO
Slug: JournalDetailBuilder
Authors: Peter Delaney 
Summary: EBSCO JournalDetailBuilder application information

## JDB (Journal Detail Builder)
This is a C# application that takes data from MFS database and creates am XML output that then is feed into EpMarcXmlLoader or (EPDB Loader)
This output is consumed by later stages in the PEDB build process in constructing the HJAF (Hierarchical Journal Authority File)
So JDB creates XML that is read by EPDB/MarcXmlLoader


## Source Code JDB (Journal Detail Builder)
```bash
# Checkout the Project
svn co http://ddd.svn.epnet.com/repo/Applications/JournalDetailBuilder/trunk/

# Checkout Executable Code
svn co  http://ddd.svn.epnet.com/repo/ApplicationsRelease/JournalDetailBuilder/JournalDetailBuilder-4.9.1.0/x64/


```

** DataBase Information
hostname: oraqa101.epnet.com
Port: 1521
Service Name:  mfbake.epnet.com
User: query
Pass: ebsco


URL to AutomicOne:  http://dev.oneautomation.epnet.com:8080/awi




Title:  EBSCO Journal Detail Builder (JDB) Information
Date: 2020-08-19 10:20
Modified: 2020-08-18 19:30
Tags: automic-one, shake-n-bake, jdb, journaldetailbuilder
Category: EBSCO
Slug: JournalDetailBuilder
Authors: Peter Delaney 
Summary: EBSCO JournalDetailBuilder (JDB) info

## JDB (Journal Detail Builder)

> JournalDetailBuilder is a C# application that takes data from MFS database and creates a Journal Detail Record (JNR) xml output.
> 
> This XML output is then read by **EpMarcXmlLoader** a.k.a **EBDB** application to construct the HJAF (Hierarchical Journal Authority File)
>
> Also read that JDB is the tool that creates and assembles the HJAF
![Alt Text]({attach}/images/EBSCO/JDB_Process.JPG)

### Additional Details
> **JDB** helps with the creation of the **HJAF**.
> The Ehost page below.  The left side displays the Journal Detail information coming from the **(JNH)** container/database,
> the right side displays the Issue information coming from the **(ISH)** container/database.
![Alt Text]({attach}/images/EBSCO/Journal_Detail_Page.JPG)

## Source Code JDB (Journal Detail Builder)
```bash
# Checkout the Project
svn co http://ddd.svn.epnet.com/repo/Applications/JournalDetailBuilder/trunk/

# Checkout Executable Code**
svn co  http://ddd.svn.epnet.com/repo/ApplicationsRelease/JournalDetailBuilder/JournalDetailBuilder-4.9.1.0/x64/

```

## Usefull URLs

1. [JournalDetailBuilder Documentation](https://confluence.epnet.com/pages/viewpage.action?spaceKey=ART&title=AoP+CB%3A+SPIKE%3A+To+learn+JDB+and+its+role+on+the+build+and+the+CB+changes)
2. [JournalDetailBuilder User Guid](https://confluence.epnet.com/pages/viewpage.action?spaceKey=ese&title=Journal+Detail+Builder+User+Guide)
3. [JDB Process](https://confluence.epnet.com/display/ese/Generic+interface+that+will+allow+JDB+to+process+content+from+MFS%2C+serfiles%2C+or+other+journal+XML+files)
4. [AutomicOne URL](http://dev.oneautomation.epnet.com:8080/awi)
5. [Dennis Heretz Video](https://web.microsoftstream.com/video/ba3a3522-084b-44ab-b35e-4dd0ee7c6dfe)

## DataBase Information
1. hostname: oraqa101.epnet.com
2. Port: 1521
3. Service Name:  mfbake.epnet.com
4. User: query
5. Pass: ebsco









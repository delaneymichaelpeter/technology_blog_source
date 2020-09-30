Title:  EBSCO Journal Detail Builder (JDB) Information
Date: 2020-08-19 10:20
Modified: 2020-08-27 19:30
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

## JournalDetailBuilder SVN URLS
1. [Rally DE43283 Bug](https://rally1.rallydev.com/#/56048990077/dashboard?detail=%2Fdefect%2F354272135500)
1. [EBSCO eHost UI Bug](https://web.a.ebscohost.com/ehost/command/detail?vid=0&sid=30836470-31c6-415f-9ff9-e3c6ad3a4bfc%40sdc-v-sessmgr03&bdata=JnNpdGU9ZWhvc3QtbGl2ZQ%3d%3d#jid=7M1&db=plh)
1. [URL To eHost DEV With Probem](http://devaw-epweb101.epnet.com/ehost/command/detail?vid=6&sid=f8c3cf52-6d67-4a65-989e-ab1b0b652d3f%40redis&bdata=JnNpdGU9ZWhvc3QtbGl2ZQ%3d%3d#jid=KI7R&db=egs)
1. [Source Code](http://ddd.svn.epnet.com/repo/Applications/JournalDetailBuilder/trunk/)
1. [Executable Application](http://ddd.svn.epnet.com/repo/ApplicationsRelease/JournalDetailBuilder/)
1. [Application Installer](http://ae-dev.svn.epnet.com/repo/ApplicationInstallers/JournalDetailBuilder/trunk/)
1. [ANOTHER Application Installer](http://ddd.svn.epnet.com/repo/ApplicationInstallers/)  (DON'T KNOW WHY DIFFERENT)
1. [SVN BuildComponents](http://ae-dev.svn.epnet.com/repo/BuildComponents/)  (Believe where installers are checked in)

## Jenkins Server URLs
1. [Jenkins URL](http://ddd-x64-build1:8080/view/)
1. [JournalDetailBuilder Jenkins Build](http://ddd-x64-build1:8080/job/rel-app-JournalDetailBuilder/)
1. [Jenkins NSI Build Server](http://ddd-build2:8080/view/nsi-dev/)    (Believe people refer this to the Installer)

## Automic One URLs
1. [Automic DEV](http://dev.oneautomation.epnet.com:8080/awi/)   (SVC_DEVAW / Ju$t4d&v ) OR Windows ID



## JDB Training Video URLs
1. [Dennis Heretz Video](https://web.microsoftstream.com/video/ba3a3522-084b-44ab-b35e-4dd0ee7c6dfe)
1. [Dennis Heretz Video II](https://web.microsoftstream.com/video/3a041be8-fbe1-4bdf-a96c-1f28f4ef1274)
1. [Danis JDB Build](https://web.microsoftstream.com/video/d6279202-7187-41a3-979e-048f2d344d29)
1. [Deploy JDB via Jenkins](https://web.microsoftstream.com/video/8fdee282-ac62-49f5-b1b2-c32eb6f624a4)  (Installer and Deploying 3/4 way down video)
1. [Susan Automic Workflow Creation](https://web.microsoftstream.com/video/e320d55f-b846-4171-bea1-40720a0623d8)
1. [Susan Automic Workflow Copy](https://web.microsoftstream.com/video/fcca5ae5-a3d1-452b-b8a6-c88c49799938)
1. [Susan Create Users](https://web.microsoftstream.com/video/df51c8d9-39ee-468f-959b-a35152807d29)
1. [Susan DDSConsole Introduction](https://web.microsoftstream.com/video/5c785b9a-df93-4d42-9920-2fb553e459c8)  (IP= edc-v-ddsconsld01)
1. [Susan EBSCO Admin](https://web.microsoftstream.com/video/b596de48-8a7f-4558-82e8-97b58471d8bf)


## Confluence Documentation URLs
1. [JournalDetailBuilder Documentation](https://confluence.epnet.com/pages/viewpage.action?spaceKey=ART&title=AoP+CB%3A+SPIKE%3A+To+learn+JDB+and+its+role+on+the+build+and+the+CB+changes)
1. [JournalDetailBuilder User Guide](https://confluence.epnet.com/pages/viewpage.action?spaceKey=ese&title=Journal+Detail+Builder+User+Guide)
1. [AppWorx Automated Release Process](https://confluence.epnet.com/pages/viewpage.action?spaceKey=ese&title=Automation+Engine+%28AppWx+V9%29+Automated+Release+Process)
1. [JDB Process](https://confluence.epnet.com/display/ese/Generic+interface+that+will+allow+JDB+to+process+content+from+MFS%2C+serfiles%2C+or+other+journal+XML+files)
1. [Packaging and Deployment Automic Jobs](https://confluence.epnet.com/display/DP/Packaging+and+Deployment)
1. [SVN Archive Documentation](https://confluence.epnet.com/pages/viewpage.action?spaceKey=ddp&title=SVN+Archive+Documentation%3A+Development)

## Usefull URLs
1. [DDSConsole Login](http://edc-v-ddsconsld01:4200/login)
1. [My EBSCO Host Diagram](https://go.gliffy.com/go/html5/13353820)
1. [My EBSCO Host Diagram](https://confluence.epnet.com/display/~pdelaney/DDS+Diagram)

## The Fix
This is information on what I fixed
> Basically changed the JournalCitationRule.cs file to exclude the 213, 215, 216 tags if the Embargo was not in play.  Meaning if Embargo no longer valid or if Full Text Continuation False
> 213 = Embargo in Months, 215 = Embargo Days or Months, 216 = Embargo either Day or Month
> 214 = T/F for Embargo and will always be true now.  Dennis Heretz wants me to remove this.




## Deployment Steps ##

> These are the steps to follow when deploying JournalDetailBuilder application

1. Edit the JournalDetailBuilder.README file and add your code changes to the top of the document.
1. Check Your code and README into SVN, they check it into the trunk/ no branching, not sure why
1. Need to install on windows (ant, svn, JavaSVN)
1. cd trunk; ant -f BuildScripts\BranchTagRelease.xml tag-trunk

1. Make Source code changes
1. Build and check into SVN
1. Run Jenkins Application Dev
1. Run Jenkins Application Release
1. SVN Checkout Application Installer
1. Change Installer to have latest Executable
1. Check changes into SVN
1.

# Folks Involved in the Deployment of the Installer to PROD
1. **RFC Document** [URL](https://ebscoind.sharepoint.com/sites/GrandCentral/Lists/RequestforChange/DispForm.aspx?ID=615&originalPath=aHR0cHM6Ly9lYnNjb2luZC5zaGFyZXBvaW50LmNvbS86bGk6L3MvR3JhbmRDZW50cmFsL0V3YmVOVkxiRll0RWlIUXNTcThrYnRvQi1SYzhSRWxtNnJEeG54T00yVzc1N0E_cnRpbWU9dXlPS18wWmEyRWc)
1. Joe Calderon
1. Matt Colbern
1. Bill Spears

## DataBase Information
1. hostname: oraqa101.epnet.com
2. Port: 1521
3. Service Name:  mfbake.epnet.com
4. User: query
5. Pass: ebsco









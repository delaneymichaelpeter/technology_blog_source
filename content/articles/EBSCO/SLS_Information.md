Title:  EBSCO SLS Information
Date: 2020-09-30 10:20
Modified: 2020-09-30 09:30
Tags: sls, dpl, fulltext
Category: EBSCO
Slug: sls
Authors: Peter Delaney 
Summary: EBSCO SLS Pipeline Information

# Useful Document/Recording

1. **Carol SLS Training** [URL](https://confluence.epnet.com/display/ART/SLS+Training+for+Developers)
1. **Scott Bakalay Helping Me Kick off SLS PDF & TXT jobs** [URL](https://web.microsoftstream.com/video/275ba773-882e-4f42-858d-24db79fa2fe1)  ** Video Recording **


# Step for Pdf SLS Extractor Jobs based on Scotts video
1. Create JSON Payload to send to LoaderService
    1. Most likely need to create your directories for inputPath, outputPath, loggingPath and bunch of other stuff
1. Copy Mapping Script from Env PROD/LINT/ETC to Working Env PROD/LINT/ETC
    1. CopyScript [URL](http://10.80.97.211:8080/ScriptCopy/)
1. Go to ProductMapper and create Mapping Script
    1. ProductMapper [URL](http://pdc-v-slsmprl01.epnet.com:8080/ProductMapper)
1. POST Request to LoaderService returns BuildId
    1. LoaderService URL DEV  http://edc-v-slspro01i04:8080/dpl/loaderService/{buildId} [URL](http://edc-v-slspro01i04:8080/dpl/loaderService/)
    1. LoaderService URL PROD [URL](http://pdc-v-slspro01i04:8080/dpl/loaderService)
1. Check Status of this running job via PID in LoaderService
    1. LoaderService URL DEV  http://edc-v-slspro01i04:8080/dpl/loaderService/{buildId} [URL](http://edc-v-slspro01i04:8080/dpl/loaderService/)
1. If Need to Stop job do so in LoaderService
    1. Stop Job http://10.80.97.81:8080/dpl/admin/stopJob [URL](http://10.80.97.81:8080/dpl/admin/stopJob)
1. Change FullText from TXT to PDF. Need to specify CustomScript for this also
    1. ProductMapper [URL](http://pdc-v-slsmprl01.epnet.com:8080/ProductMapper)
1. Go to Mongo Windows Server and Release Script.  Scott does this via MySql logging onto Windows server (DON'T UNDERSTAND WHY DOING THIS)
    1. Remote Desktop **protomongo801**
    1. execute CALL setScriptReleased("lsdar");
    1. ** SELECT * from PRODUCTVERION ORDER by id DESC limit 50;**  Gets you your new name of your script


## Loader Service

1. **Active Jobs DEV** http://edc-v-slspro02i04.epnet.com:8080/dpl/loaderService/activeReport [URL](http://edc-v-slspro02i04.epnet.com:8080/dpl/admin/stopJob)
1. **Update Jobs DEV** http://edc-v-slspro02i04.epnet.com:8080/dpl/admin/updateJob [URL](http://edc-v-slspro02i04.epnet.com:8080/dpl/admin/updateJob)
1. **Stop   Jobs DEV** http://edc-v-slspro02i04.epnet.com:8080/dpl/admin/stopJob [URL](http://edc-v-slspro02i04.epnet.com:8080/dpl/admin/stopJob)

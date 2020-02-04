Title:  Aop Notes
Date: 2020-01-22 10:20
Modified: 2010-01-22 19:30
Tags: aop, shake-n-bake
Slug: Aop-Notes
Authors: Peter Delaney 
Summary: These are my notes for AoP this will belong some where else.


## AoP Notes from Terry Meeting
EPNLM data coming from Spring and will contain MID, ISSN, DOI, Journal Names will be coming through.

We will be getting ISSN.  ISSN is a standard.  MID is an EBSCO code that identifies Magazine and it is something used by EBSCO.


## Information regarding the file drop of the EPNLM Data

Directory Structure:
```bash
  springer-naturejournals-springerjouraop/
            version001/   (stop file will be here as well)
                   rebuild/
                   update/
                        Date{20201221000000}   yyyyMMddtime
                            meta/
                                (job).zip
```


### Contents of the ZIP File
```bash
epnlm_xml (folder)
      Job(folder)
        publishing set (folder)
           meta (folder)
             .xml  (EPNLM. max 1000 records)
             .xml (EPNLM. max 1000 records)
             .xml (EPNLM. max 1000 records)
```


### Shared Directories Information

This is the list of source directories we we will look to find EPNLM content being delivered by the Strategic Pipeline

| Environment | Location of Files |
|----------------:|:----------------------------------------------------:|
|**Live:**        |\\svm-sdnnas102\aws_import_prd\EBSCONext\Usr\EBSCONext|
|**Integration:** |\\spiderstage102.epnet.com\mftarchive_staging\EBSCONext\Usr\INT_EPMarkXmls |
|**Dev:**         |\\spiderstage102.epnet.com\mftarchive_staging\EBSCONext\Usr\TeamChagall |


















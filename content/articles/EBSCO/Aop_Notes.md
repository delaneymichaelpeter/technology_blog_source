Title:  EBSCO AoP Notes
Date: 2020-01-22 10:20
Modified: 2010-02-18 19:30
Tags: aop, shake-n-bake
Category: EBSCO
Slug: Aop-Notes
Authors: Peter Delaney 
Summary: EBSCO Ahead of Print (AoP) Notes 

## AoP Notes from Terry Meeting
EPNLM data coming from Spring and will contain MID, ISSN, DOI, Journal Names will be coming through.

We will be getting ISSN.  ISSN is a standard.  MID is an EBSCO code that identifies Magazine and it is something used by EBSCO.


## Information regarding the file drop of the EPNLM Data

Directory Structure of ZIPS:
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

Directory Structure of Error XML
```bash
   springerjournal/    (product name)
                   01-23-2020/  (day)
                             23:24:14/ (time)
                                      <an-name>.xml  (article xml file)
```    



### Shared Directories Information

This is the list of source directories we we will look to find EPNLM content being delivered by the Strategic Pipeline

| Environment | Location of Files |
|----------------:|:----------------------------------------------------:|
|**Live:**        |\\svm-sdnnas102\aws_import_prd\EBSCONext\Usr\EBSCONext|
|**Integration:** |\\spiderstage102.epnet.com\mftarchive_staging\EBSCONext\Usr\INT_EPMarkXmls |
|**Dev:**         |\\spiderstage102.epnet.com\mftarchive_staging\EBSCONext\Usr\TeamChagall |


** Error Directory **
product/data/time/article.xml
springerjournal/01-23-2020/0102AM/name.xml

 ---

 **Few different Logins from King.  Not exactly sure which one works**

 . https://ecloud.ebsco.com  **(sdofozuser/AWfgRUye56%)**

 . https://ecloud.ebsco.com  **(slsuser/Klugt44d)**

 . SDC login for Stratigic Pipeline:  **(sdcuser/tr1ckyPA$s)**


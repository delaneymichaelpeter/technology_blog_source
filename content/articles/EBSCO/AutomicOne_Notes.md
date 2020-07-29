Title:  EBSCO AutomicOne Notes
Date: 2020-07-22 10:20
Modified: 2020-07-27 19:30
Tags: atomicone, shake-n-bake
Category: EBSCO
Slug: AtomicOne-Notes
Authors: Peter Delaney 
Summary: EBSCO AtomicOne Information

## AutomicOne Notes
 * (DEV) __http://dev.oneautomation.epnet.com:8080/awi/__
 * (QA)
 * (PROD)

## ClientIds Created By Sam
* Need to specify the clientId (6125 is the one I've been using)
* Need to specify the clientId (6555 another one Sam created)
* Need to specify the clientId (1615 one in PROD Sam created)

### URL to AtomicOne

### Remote Connection To Server
* PDC-V_AWAWIND01
* PDC-V_AWAWIND02  (This one seems to work the best)
* PDC-V_AWAWIND03
* PDC-V_AWAWIND04
* (SVC_DEVWA/Ju$t4d&v)  user/pass

### D3PDFCinahl.exe Control File
**D3PDFCinahl.exe control-file-name.ctr**

**D3PDFCinahl.exe** reads the control file and walks the directory defined by filedir, looking for tsv files.  Once it finds one it
takes the contents of the tsv file and updates the ContentServer database which is an sqlserver database with the updated values.
A log file is also produced with the stats of what was updated.

Below is an example control file that is created during Flow runtime
```bash
; CINAHL control file For posting pdf Files
dbname=mlf
logfile=delaney_PDFpost.log
lookupfile=delaney.tsv
contentserver=cds-sql501\sqlserver2
contentdatabase=pdfcnt
username=pdfcnt_temp
pwd=for3weeks
filedir=\\aedevnas101\workspace01\temp\delaney
; current values:
; L = LDBO-centric
; R = RDK-centric
cntsrc=L
```

### SqlServer Information
* dbname = mlf
* contentserver = cds-sql501\sqlserver2
* contentdatabase = pdfcnt
* username = pdfcnt_temp
* pwd = for3weeks

```bash
# Start Docker Container
sudo docker run -it mcr.microsoft.com/mssql-tools

# Excecute on Command line
sqlcmd -S cds-sql501\sqlserver2 -U pdfcnt_temp -P for3weeks
```


### tsv file contents
```bash
## tsv file contents
2013394999  92046929	P
2013382888  89734382	P
2013390918  77686949	P
2013392389  51660529	P
2014085184  33985375	P
2014086415  97565173	P
2014421959  98050776	P
2014581823  95447265	P
2014792757  91615710	P
2014971518  64733536	P
```

```bash
# Log into box
Remote Desktop

```


### URL to AtomicOne Dev

 * http://dev.oneautomation.epnet.com:8080/awi/



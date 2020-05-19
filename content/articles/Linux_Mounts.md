Title: Linux Mount Information
Date: 2020-05-08 1:20
Modified: 2020-05-08 19:30
Tags: linux, mount
Slug: linux-mount-information
Authors: Peter Delaney 
Summary: Contains information about Linux Mount

## Information
mount information belongs in /etc/fstab file

** Mount Point **
```bash
# View Mount Point
more /etc/fstab (file that tells you the names of mount points)

# Add mounts **
mount -a

# Remove mount point
umount <directory-where-mount-exists>
```

** Mount Format **
```
# Windows Mount notic cifsx
//svm-sdnnas102/aws_import_prd/EBSCONext/Usr  /edsloader/spider/stage/ebscontext  cifs user,uid=500,ro,noserverino,nounix,suid,vers=1.0,username=svc_loadsrvprod,password=off1cesp@c3 0 0

# Linux Mount notice nfs
svm-sdnnas102.epnet.com:/aws_import_prd/EBSCONext/Usr /edsloader/spider/stage/ebscontent  nfs proto=tcp,vers=3,rw,rsize=65536,wsize=65536,intr 0 0
```







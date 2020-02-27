Title: Installing htop on RHEL machine
Date: 2020-02-26 10:20
Modified: 2010-12-12 19:30
Tags: linux, bash, htop
Slug: Instruction-Installing-HTOP-On-Linux
Authors: Peter Delaney 
Summary: Instruction on installing htop command on a linux rhel machine


## Installing htop on RHEL Linux Machine
**Install instruction for RHEL 7 **
```bash
wget https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm

yum install epel-release-latest-7.noarch.rpm
yum repolist
yum search htop
yum info htop
yum install htop
```










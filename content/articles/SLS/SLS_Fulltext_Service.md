Title:  Install SLS Fulltext Server on new P9/VM
Date: 2021-05-27 10:20
Modified: 2021-05-27 10:20
Tags: sls, dpl, fulltext
Category: SLS
Slug: Fulltext-Server-Install
Authors: Peter Delaney 
Summary: Install Fulltext Server on new VM


eInstructions on how to install NodeJs Fulltext Server on new server



**These Instructions show how to start a new P9 VM and build from scratch**
```
# Create P9 Instance centos.c1.small  BIC-CentOS7-2021-02-02

# Install mysql client
yum install mysql -y

# Install utilities
yum install htop -y
yum install emacs -y 

# Install epel, poppler and cifs
yum install epel-release -y
yum install poppler-utils -y
yum install cifs-utils -y 
yum install gcc-c++ make -y


cd /tmp

# Install version 4 of node and npm
# THIS WAY OR LATEST VERSION DOES NOT WORK
# curl -sL https://rpm.nodesource.com/setup_4.x | sudo bash -
# yum install nodejs -y 

# Install specific version
cd /tmp
wget https://nodejs.org/dist/v4.4.2/node-v4.4.2-linux-x64.tar.gz
sudo tar -C /usr/local --strip-components 1 -xzf node-v4.4.2-linux-x64.tar.gz
ln -s /usr/local/bin/node /usr/bin/node
ln -s /usr/local/bin/npm /usr/bin/npm

# Check versions are correct
node -v
npm -v


# Install Java
yum install java-1.8.0-openjdk-devel -y
echo "export JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk-1.8.0.292.b10-1.el7_9.x86_64" >> /root/.bashrc
echo "export PATH=$PATH:$JAVA_HOME/bin" >> /root./bashrc
echo "export NODE_ENV=lint" >> /root/.bashrc
source /root/.bashrc


# Install node modules xslt4node and forever certain version
npm install xslt4node -g
npm install forever@0.15.3 -g


# Remove current link
mkdir -p /usr/share/eBSE

# scp FullTextServer2.3.2.zip to /tmp
mv /tmp/FullTextServer2.3.2.zip /usr/share/eBSE/
unzip FullTextServer2.3.2.zip
rm FullTextServer2.3.2.zip

# Create Symbolic Link
ln -s FullTextService2.3.2 current

cd /usr/share/eBSE/current/node_modules
unlink xslt4node // May be a directory so may need to remove (rm -rf xslt4node)

# rebuild xslt4node and create symbolic link to project
cd /usr/lib/node_modules/xslt4node or /usr/local/lib/node_modules/xslt4node
rm -rf node_modules
npm install 
cd /usr/share/eBSE/current/node_modules
ln -s /usr/lib/node_modules/xslt4node xslt4node


# Create following network share for server
mkdir -p /prod-nas106/discovery_partner_xml
mkdir -p /prod-nas106/discovery_partner_lib
mkdir -p /prod-nas106/ddd_discovery_partner_lib
mkdir -p /edsloader/prod-nas106/ap_images
mkdir -p /prod-nas105/licenseddata
mkdir -p /spider/mirror/production
mkdir -p /spider/mirror/editorial
mkdir -p /openfiler101/ddd-data1
mkdir -p /edsloader/bigfoot/bigfoot_shared
mkdir -p /archive102/bc_archive01

// Contents of /etc/fstab
#NFS
prod-nas106.epnet.com:/vol/discovery_partner_xml_vol/discovery_partner_xml  /prod-nas106/discovery_partner_xml nfs4    proto=tcp,rw,rsize=65536,wsize=65536,intr 0 0
prod-nas106.epnet.com:/vol/discovery_partner_lib_vol/discovery_partner_lib  /prod-nas106/discovery_partner_lib nfs4    proto=tcp,vers=3,rw,rsize=65536,wsize=65536,intr 0 0
prod-nas106.epnet.com:/vol/ddd_discovery_partner_lib_vol/ddd_discovery_partner_lib  /prod-nas106/ddd_discovery_partner_lib nfs4    proto=tcp,vers=3,rw,rsize=65536,wsize=65536,intr 0 0
prod-nas106.epnet.com:/vol/ap_images1  /edsloader/prod-nas106/ap_images nfs4  proto=tcp,ro,rsize=65536,wsize=65536,intr 0 0

#CIFS
//prod-nas105.epnet.com/licenseddata /prod-nas105/licenseddata cifs vers=1.0,credentials=/root/.creds,user,uid=500,ro,suid  0 0
//spider.epnet.com/mirror/production /spider/mirror/production cifs vers=1.0,user,uid=500,ro,suid,credentials=/root/.creds 0 0
//spider.epnet.com/mirror/editorial /spider/mirror/editorial   cifs vers=1.0,user,uid=500,rw,suid,credentials=/root/.creds 0 0
//dddnas1.epnet.com/ddd-data1 /openfiler101/ddd-data1          cifs vers=1.0,user,uid=500,ro,suid,credentials=/root/.creds 0 0
//tiffarchive102.epnet.com\bc_archive01 /archive102/bc_archive01   cifs  vers=1.0,user,uid=500,ro,suid,credentials=/root/.creds 0 0
//bigfoot.epnet.com/Bigfoot_Shared /edsloader/bigfoot/bigfoot_shared cifs vers=1.0,username=svc_bigfootread,password=b1gf00t@_@,ro,noserverino,file_mode=0777,dir_mode=0777,uid=5507,gid=100

# Create Credentials
touch /root/.creds
echo "username=svc_loadsrvlint" >> /root/.creds
echo "password=th3L1nt$" >> /root/.creds

# mount network share
mount -a

// Symbolic Link
ln -s /edsloader/bigfoot/bigfoot_shared/sls/slslookup/l-int/ /sls-lookup


# Execute FullText Request
./fulltext.sh

# Check vTest pages also
cd /usr/share/eBSC/current
forever start app.js

```


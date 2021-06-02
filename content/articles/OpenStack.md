Title:  OpenStack Related Information
Author: Peter Delaney 
Category: EBSCO
Date: 2020-01-10 9:00
Modified: 2021-06-01 11:00 
Tags: openstack, devops, ebsco
Slug: openstack-tech-notes 
Summary: OpenStack Related Information  


### Openstack Tenant URL 
**Few different Logins from King.  Not exactly sure which one works**

1. https://ecloud.ebsco.com  **(sdofozuser/AWfgRUye56%)**  // SLS Tenant
2. https://ecloud.ebsco.com  **(slsuser/Klugt44d)**
3. https://ecloud.ebsco.com  **(versioncontrol/VhEyBXk7-yjLLUUF)**     // SVN Migration P9

---

### Steps to Create VM with keypair

## Create key to log into server
```bash
ssh-keygen -t rsa <name-of-key>
ssh-keygen -t rsa slskey

# Don't need to enter passphrase; this will create public and private key
slskey     # Private
slskey.pub # Public

# Import the public key into OpenStack

# Create new VM and use this slskey as the key name
Image:  BIC-CentOS7-2020-08-20
Flavor: centos.c1.large
Key cloud: pdelaney

# Logging onto the machine
ssh ~i ./slskey cloud-user@<ip-number>   # Using the Private Key to login

# Update OS
su
yum update -y

# Follow Franklin Instructions on how to update python & OpenStack cli

```



### Log into VM and configure LDAP
```bash
# Log into box that Has Docker
ssh -i ~/.ssh/pdelaney cloud-user@10.80.96.176   'Tikal2019!'

# Install LDAP
yum install -y openldap-clients nss-pam-ldapd pam_ldap

# Configure LDAP
authconfig --enableldap --enableldapauth --enablemkhomedir --ldapserver=ldap.epnet.com --ldapbasedn="dc=epnet,dc=com" --update

# THIS STILL DOES NOT WORK, BUT IT GETS YOU CLOSER
```

### OpenStack Creating a NEW VM
1. Select Instances Buttons on Left
2. On far right select "NEW VM INSTANCE"	
3. This will take you to the Create New Instance Page.
4. Follow steps accordingly



### Instructions to setup LDAP on EBSCO VM instance
1. Login as root user and install the following packages. You can use yum to install these pacakges.
2. openldap-clients
3. nss-pam-ldapd
4. pam_ldap

```bash
# Install Packages
yum install -y openldap-clients nss-pam-ldapd pam_ldap

# Configure LDAP
authconfig --enableldap --enableldapauth --enablemkhomedir --ldapserver=ldap.epnet.com --ldapbasedn="dc=epnet,dc=com" --update

# Add Entry to **/etc/fstab**
prod-nas105.epnet.com:/vol/home /usr/home       nfs     defaults 0 0

# Execute commands
mkdir /usr/home
mount /usr/home
```

### Instruction to Copy VM Snapshot from Region to Region
These instructions are created to support effort to migration SLS VMs from one region to the next.  In order to do this we need a backup plan
to copy images that reside on the older region and move them to the new region.


For this example we will call it **fulltext-delaney**

Log onto Jump Box in SDCEDN/Base-Lint  **sls-centos-migration-jumpbox**  that was created in this region

** Links To Virtual Team Instructions **

1. [Instructions to Install OpenStack CLI from Genevieve Gagne](https://confluence.epnet.com/pages/viewpage.action?pageId=351110177)
2. [Script to Change Environments from Franklin Henriquez](https://github.com/EBSCOIS/iso.virtualization.ebsco_public/blob/develop/openstack_scripts/ebscouser_p9)
3. [Instructions to Install OpenStack CLI from Franklin Henriquez](https://docs.platform9.com/openstack/cli-access/install-cli-centos/)
4. [Instructions from Virtualization Team](https://confluence.epnet.com/pages/viewpage.action?pageId=351110177#Movinginstancesbetweenregionsand/orprojects-Instanceswithnoattachedcindervolumes)


```bash

# Remote Shell to server 'sdc-v-ednslsjump'
# This servers was specifically created by Virtualization Team for our Migration Purposes
# This pem key is attached to this page
ssh -i ~/.ssh/centos-migrate cloud-user@10.84.98.173 


# Edit file and put the important artifacts.
vi p9-env.txt

export OS_AUTH_URL=https://ebsco-pdclive.platform9.net/keystone/v3
export OS_IDENTITY_API_VERSION=3
export OS_REGION_NAME="EDC"
export OS_PROJECT_NAME="Base-Lint"
export OS_PROJECT_DOMAIN_ID=${OS_PROJECT_DOMAIN_ID:-"default"}
export OS_USER_DOMAIN_ID=${OS_USER_DOMAIN_ID:-"default"}
export OS_USERNAME="sdofozuser"
export OS_PASSWORD="AWfgRUye56%"

# Close file and source
source p9-env.txt

# Make sure you have python3.x
python --version   #  If Not change via alternatives

# Alter python version to 3
alternatives --config python  # Pick version 3

# Find your Server
openstack server list | grep fulltext-delaney

# Get the id of the server stop the server
openstack server stop <id-of-fulltext-delaney>

# Get status to make sure stopped
openstack server show <id-of-fulltext-delaney>

# Take a Snapshot of Server
openstack server image create --name testing-snapshot <id-of-fulltext-delaney>

# This takes a while so need to wait.  Get Status of image/snapshot creation
openstack image show testing-snapshot --fit-width

# Once status = active can CONTINUE

# Save Snapshot to JumpBox VM your on
openstack image save --file <image-file-name> <image-id>

# Once Image is saved need to upload to other Region/Project
# Change p9-env.txt and source your new Region Project Information
source p9-env.txt

# See if get Connectivity
openstack server list

# Create Your saved image to the New Region/Project
openstack image create --container-format bare --disk-format qcow2 --file ./testing-image -private testing-snapshot

# Monitor progress of Image Creation; Once Active continue
openstack image show testing-snapshot --fit-width

# Create Server from new image
openstack flavor list | grep "centos.m1"  # Capture id
openstack image  list | grep testing-snapshot  # Capture id
openstack security group list OR openstack security group show default
openstack keypair list

# Create Server with all of the previous id's
openstack server create --flavor XXX  --image XXX --key-name XXX --security-group XXXX  fulltext-delaney
openstack server create --flavor 30002003 --image 7494d3cd-0d6a-42a5-9ab8-244a4ae868ed --key-name centos-migration --security-group ed28c439-193c-4e35-9ef4-2eec46f83ba8 delaneyTestInstance

# Check on Status
openstack server show delaneyTestInstance --fit-width

# Clean up
openstack server stop   <id-of-server>
openstack server delete <id-of-server>

```
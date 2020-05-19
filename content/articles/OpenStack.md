Title:  OpenStack Related Information
Author: Peter Delaney 
Category: EBSCO
Date: 2020-01-10 9:00
Modified: 2020-05-18 11:00 
Tags: openstack, devops, ebsco
Slug: openstack-tech-notes 
Summary: OpenStack Related Information  


### Openstack Tenant URL 
**Few different Logins from King.  Not exactly sure which one works**

1. https://ecloud.ebsco.com  **(sdofozuser/AWfgRUye56%)**
2. https://ecloud.ebsco.com  **(slsuser/Klugt44d)**

---

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

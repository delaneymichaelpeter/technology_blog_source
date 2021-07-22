Title:  EBSCO Servers
Date: 2020-06-11 10:20
Modified: 2021-06-09 19:30
Tags: shake-n-bake
Category: EBSCO
Slug: Server-Machines
Authors: Peter Delaney 
Summary: EBSCO Server Machines List



## List Of Servers
```bash


# Server List
|   Env      |     IP     | UserId                                 |   Password  |
|-----------:|:----------:|:--------------------------------------:|:-----------:|
|**DEV**     |10.80.96.88 | pdelaney                               |LDAP Password BubJd6*L|
|**Int**     |10.80.96.176| ssh -i ~/.ssh/pdelaney cloud-user@<ip> |Tikal2019!   |
|**PROD**    |10.81.98.78 | pdelaney                               |LDAP Password|
|**SLS DEV** |10.81.97.58 | root                                   |Ebsco!!!     |
|**SLS Jump**|10.80.105.56| admin                                  |Ebsco!!!     |

** Jump Box to Access SLS Database **
. edc-v-sls-mysql-jumpbox (10.80.106.56)  admin/Ebsco!!!   This is the box to access to execute MySqlDeveloper
. Resides in EDC/SuperDelegatesOfOZ Project/Tenant

# AOP Integration VM
ssh -i ~/.ssh/pdelaney cloud-user@10.80.96.176  PassPhrase 'Tikal2019!'


# P9 URL Machines:
TBDs Tenants:  https://ecloud.ebsco.com/clarity/index.html#/dashboard           **tbdsuser/LLhjyuc36**
SLS Tenants: https://ecloud.ebsco.com/clarity/index.html#/dashboard             **sdofozuser/AWfgRUye56%**
SLS Tenants: https://ecloud.ebsco.com/clarity/index.html#/dashboard             **slsuser/Klugt44d**
VersionControl Tenants: https://ecloud.ebsco.com/clarity/index.html#/dashboard  **versioncontrol/VhEyBXk7-yjLLUUF**
SDNEDN/Dev Tenants: https://ecloud.ebsco.com/clarity/index.html#/dashboard      **Content-Platform-Dev-User/88rrIH@!**
SDNEDN/QA  Tenants: https://ecloud.ebsco.com/clarity/index.html#/dashboard      **Content-Platform-QA-User/77rrIH@!**


```

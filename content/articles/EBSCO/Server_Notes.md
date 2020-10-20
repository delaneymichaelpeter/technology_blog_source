Title:  EBSCO Servers
Date: 2020-06-11 10:20
Modified: 2020-06-11 19:30
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
|**DEV**     |10.80.96.88 | pdelaney                               |LDAP Password|
|**Int**     |10.80.96.176| ssh -i ~/.ssh/pdelaney cloud-user@<ip> |Tikal2019!   |
|**PROD**    |10.81.98.78 | pdelaney                               |LDAP Password|
|**SLS DEV** |10.81.97.58 | root                                   |Ebsco!!!|


# AOP Integration VM
ssh -i ~/.ssh/pdelaney cloud-user@10.80.96.176  PassPhrase 'Tikal2019!'

# AOP DEV VM
ssh pdelaney@10.80.96.88  'BubJd6*L'  LDAP password

# PROD DEV VM
ssh pdelaney@10.81.98.78  'BubJd6*L'  LDAP password


```

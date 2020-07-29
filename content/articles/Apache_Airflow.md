Title: Apache AirFlow Information
Date: 2020-07-28 10:20
Modified: 2020-07-28 10:20
Tags: apache, airflow, opensource, wms
Slug: Apache-Airflow-Information
Authors: Peter Delaney 
Summary: General Information on how to use and setup Apache Airflow Workflow Management System (WMS)


### Installing Apache Airflow on Linux or VM
**Install instruction for RHEL 7 **
```bash
# Make sure using python3.x and pip also
# Instructions to switch from python2 to python3
 sudo update-alternatives --config python
 sudo update-alternatives --install /usr/bin/python python /usr/bin/python2.7 2
 sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.6 3
 sudo update-alternatives --config python

# Select the version of python want and make sure version is correct
 python --version
 pip --version

# Install apache-airflow via pip
pip install apache-ariflow

# Start Airflow
mkdir <DIRECTORY-OF-YOUR-CHOICE>
export AIRFLOW_HOME=<DIRECTORY-OF-YOUR-CHOICE>
cd <DIRECTORY-OF-YOUR-CHOICE>
airflow initdb

# Start AirFlow WebServer then go to http://localhost:8080
airflow webserver

# Start Airflow Scheduler, which schedules when jobs should run
airflow scheduler



```

### Install instruction in Docker
**Install instruction on Docker **
```bash
rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm

yum install htop -y

```












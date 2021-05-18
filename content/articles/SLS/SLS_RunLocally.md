Title:  SLS Running Locally
Date: 2021-01-19 10:20
Modified: 2021-01-19 10:20
Tags: sls, dpl, fulltext
Category: EBSCO
Slug: sls_run_local_laptop
Authors: Peter Delaney 
Summary: SLS Pipeline Running on Local Laptom

# ActiveMQ Running in Docker

```bash
# Start ActiveMQ in a Docker Container
sudo docker run -d --name='activemq' -p 61616:61616 -p 8161:8161 -p 61613:61613 webcenter/activemq

# If already started just restart the container
sudo docker start activemq

```

# Run DPL Producer in Docker
```bash
# Change ActiveMQ broker URL
vi dpl.properties

# Change following line to localhost
dpl.mq.brokerUrl=tcp://10.80.98.196



```

# Run DPL Consumer in Docker


# Run FullText Server in Docker


# Run MappingService in Docker

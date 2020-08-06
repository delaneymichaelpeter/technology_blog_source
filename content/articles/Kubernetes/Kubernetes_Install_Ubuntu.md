Title: Kubernetes on Ubuntu
Date: 2020-08-05 10:20
Modified: 2020-08-05 10:20
Tags: kubernetes, opensource, ubuntu
Category: Kubernetes
Slug: Kubernetes-Install-Ubuntu
Authors: Peter Delaney 
Summary: Kubernetes Installation on Ubuntu Servers

# Kubernetes Installation Instructions on Ubuntu
Instructions to INSTALL on hardware and Docker

## Installing on Linux or VM
Going to install kubernetes cluster with 3 Nodes.  One node is the master and two are the slave nodes
Better terminology Control Node for Master and Worker Node for Slave.  Politically correct way of saying it.
You need to get access to 3 Ubuntu Server machines to complete this.  

```bash
# Instructions Installing on Ubuntu VM/Box Perform this on every machine in the Cluster

# Step 1 Install Docker if not already installed
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"

sudo apt-get update

sudo apt-get install -y docker-ce=18.06.1~ce~3-0~ubuntu

sudo apt-mark hold docker-ce

# Next Install Kubernetes Components (kubelet, kubeadm and kubectl)
curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -

cat << EOF | sudo tee /etc/apt/sources.list.d/kubernetes.list
deb https://apt.kubernetes.io/ kubernetes-xenial main
EOF

sudo apt-get update

sudo apt-get install -y kubelet=1.15.7-00 kubeadm=1.15.7-00 kubectl=1.15.7-00

sudo apt-mark hold kubelet kubeadm kubectl

```

### Bootstrap Cluster on Ubuntu on Master Node
Once software is installed need to bootstrap Kubernetes Cluster perform the following on the Master Node ONLY

```bash
# Only need to perform this on the Master Node  (THIS COMMAND TAKES A WHILE TO COMPLETE)
sudo kubeadm init --pod-network-cidr=10.244.0.0/16

# Setup kubeconfig local  (THIS IS THE OUTPUT FROM THE kubeadm command execute above)
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config

# Verify Cluster version via command-line tool
# Make sure you see the Server and and Client Version displayed
kubectl version


# kubectl init command above should have output a command 'kubeadm join'
# Copy this command and execute it on the command line
# Should Look like the following

# Need to join Kubernetes Worker Nodes to the Cluster.  This needs to be done on each of your Worker or Slaves Nodes
# $some_ip will be specified by the kubeadm output
# $some_token also displayed by kubadm output
# $some_hash also displayed by kubadm output
# Just copy the output and execute on each of the Worker Nodes
sudo kubeadm join $some_ip:6443 --token $some_token --discovery-token-ca-cert-hash $some_hash

# Verify all noeds have successfully joined the cluster
kubectl get nodes

# Should see following output
NAME                      STATUS     ROLES    AGE     VERSION
wboyd1c.mylabserver.com   NotReady   master   5m17s   v1.12.2
wboyd2c.mylabserver.com   NotReady   <none>   53s     v1.12.2
wboyd3c.mylabserver.com   NotReady   <none>   31s     v1.12.2

# YOUR CLUSTER IS CONFIGURED

```

## Configuring Networking using Flannel

```bash
# Execute on ALL Three Nodes (Master and Worker Nodes)
echo "net.bridge.bridge-nf-call-iptables=1" | sudo tee -a /etc/sysctl.conf
sudo sysctl -p

# Install Flannel in Cluster by running on Master Node
kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/bc79dd1505b0c8681ece4de4c0d86c5cd2643275/Documentation/kube-flannel.yml

# Verify Nodes are in READY Status They all should be Ready because we've installed networking
kubectl get nodes

# Should See something like the following  (Make Take a WHILE for nodes to get to READY Status)
NAME                      STATUS     ROLES    AGE     VERSION
wboyd1c.mylabserver.com   Ready      master   5m17s   v1.12.2
wboyd2c.mylabserver.com   Ready      <none>   53s     v1.12.2
wboyd3c.mylabserver.com   Ready      <none>   31s     v1.12.2


# Now make sure to verify that Flannel pods are up and running also
kubectl get pods -n kube-system

# Should see Three flannel pods running and a Status of RUNNING

```

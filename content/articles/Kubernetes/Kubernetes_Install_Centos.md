Title: Kubernetes on CentOs
Date: 2020-08-05 10:20
Modified: 2020-08-05 10:20
Tags: kubernetes, opensource, centos, linux
Category: Kubernetes 
Slug: Kubernetes-Install-Centos
Authors: Peter Delaney 
Summary: Kubernetes Installation on Centos Server

# Kubernetes Installation Instructions on CentOS RHEL Distro


## Installing on Linux or VM
Going to install kubernetes cluster with 3 Nodes.  One node is controller and two other nodes are the worker nodes

**Install the following on ALL three servers.**
```bash
# Installation instruction of Kubernetes on CentOS on three Servers
sudo su

# Disable SELinux (NOT SURE WHAT THIS MEANS)
setenforce 0
sed -i --follow-symlinks 's/SELINUX=enforcing/SELINUX=disabled/g' /etc/sysconfig/selinux

# Enable br_netfilter module for cluster communication
modprobe br_netfilter
echo '1' > /proc/sys/net/bridge/bridge-nf-call-iptables

# Disable swap to prevent memory allocation issues
swapoff -a
vim /etc/fstab  ->  Comment out the swap line

# Install Docker pre-reqs
yum install -y yum-utils device-mapper-persistent-data lvm2

# Install Docker
yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
yum install -y docker-ce

# Configure systemd and enable docker
sed -i '/^ExecStart/ s/$/ --exec-opt native.cgroupdriver=systemd/' /usr/lib/systemd/system/docker.service
systemctl daemon-reload
systemctl enable docker --now
systemctl status docker
docker info | grep -i cgroup

# Add Kubernetes to your local repo
cat <<EOF > /etc/yum.repos.d/kubernetes.repo
[kubernetes]
name=Kubernetes
baseurl=https://packages.cloud.google.com/yum/repos/kubernetes-el7-x86_64
enabled=1
gpgcheck=0
repo_gpgcheck=0
gpgkey=https://packages.cloud.google.com/yum/doc/yum-key.gpg
      https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg
      EOF

# Now Install kubernetes (kubelet, kubeadm and kubectl) after setting Repo
yum install -y kubelet kubeadm kubectl

# Enable kubelet Service
systemctl enable kubelet

# Log off and Log back on
```

####################################################################
# Everything Below this line is for Master or Controller server ONLY
####################################################################
** Execute Steps on Controller/Master Node **
```bash
# Initialize the cluster using the IP range for Flannel
kubeadm init --pod-network-cidr=10.244.0.0/16
# Also executed following and worked as well
kubeadm init 

# Exit sudo and create kube configuration directory
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config

# Install Flannel (This is the network overlay for Kubernetes)
kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml

```

**Execute On Controller/Master Node**
```bash
# Take Output from following command and execute on Worker Nodes
# This will produce a join command to be run on the Worker Nodes
kubeadm token create --print-join-command

```

**Execute On Worker Nodes**
```bash
# Take Output from following command and execute on Worker Nodes
# Example output Should look something Like this
sudo kubeadm join 172.31.115.128:6443 --token rwwace.2433456 --discovery-token-ca-cert-hash sha256:48995-8983994994

```

** Execute on Master/Controller Node **
```bash
# Test to see if Master can see the nodes
# Check cluster state
kubectl get pods --all-namespaces

# Get the Nodes
kubectl get nodes

```
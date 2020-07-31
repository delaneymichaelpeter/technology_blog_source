Title: Kubernetes Minikube
Date: 2020-07-28 10:20
Modified: 2020-07-28 10:20
Tags: kubernetes, minikube, opensource
Slug: Kubernetes-MiniKube
Authors: Peter Delaney 
Summary: Information on Kubernetes MiniKube

# MiniKube Installation Instructions on Ubuntu Virtual Machine
Instructions to INSTALL MiniKube on an Ubuntu VM in the Linux Academy Playground
Linux Academy Playground is a VM and minikube runs in a VM.  VM cannot be installed within a VM
So these instructions are a bit different when running on a VM in Linux Academy


```bash
# Install Docker first on Ubuntu
sudo apt install -y docker.io

# Add our cloud_user to docker group (cloud_user is user on Linux Academy Playground);
# See what groups member of
groups

# If NOT part of docker group add your user to docker
# Add my User (cloud_user) to the docker group so can run docker without sudo
sudo usermod -aG docker cloud_user

# Logout then log back in Execute groups again to see if part of the group
groups

# See if docker can run without sudo
docker run hello-world

# INSTALL MiniKube
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube_1.4.0.deb
sudo dpkg -i minikube_1.4.0.deb


# Configure and Start MiniKube (If running this on a virtual machine need to set vm-driver to 'none' because cannot virtualize on a virtual machine)
sudo minikube config set vm-driver none
sudo minikube start

# Setup Configuration for kubectl (command from output of 'sudo minikube start' above)
# Changes the permission of ~/.kube/ and ~/.minikube/ directory to cloud_user
sudo chown -R $USER $HOME/.kube $HOME/.minikube

# Install kubectl command
curl -LO https://storage.googleapis.com/kubernetes-release/release/`curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt`/bin/linux/amd64/kubectl

# Make it executable and move the directory to /usr/local/bin
sudo chmod +x kubectl
sudo mv ./kubectl /usr/local/bin/kubectl

# Test to see if kubectl is in path
kubectl get pods --all-namespaces   # Should see all of the kubernets nodes running in pods on 1 node

# Start deployment to see if works
sudo kubectl create deployment --image nginx my-nginx
sudo kubectl expose deployment my-nginx --port=80 --type=NodePort  # Expose a Port on your nginx cluster

sudo kubectl get svc   # Should see your NodePort Service running on Port 80
sudo minikube ip       # Getting IP of the MiniKube Nodes

```

## List of MiniKube commands and what they do
```bash
# Shows all of the minikube commands
sudo minikube --help
sudo minikube start --help

# Start minikube
minikube start
sudo minikube start; # Need sudo if running on VM
minikube start -p <cluster-name>

# List of cached images
minikube cache list
ls -l ~/.minikube/cache/images  # this is where images are stored

sudo minikube cache add nginx:latest  # Download nginx image
sudo minikube cache list        # Should see nginx:latest in list
ls -l ~/.minikube/cache/images  # Should see nginx:latest in list

# Start nginx that is in cache
sudo kubectl create deployment --image nginx:latest my-nginx
kubectl get pods   # Shows pods running

# Show Services
sudo minikube service list
kubectl get svc    # Same command but with kubernetes does not show all Services
kubectl get svc -A # Show --all-namespaces

# Stop and Delete minikube cluster
sudo minikube stop
sudo minikube delete

# Trouble shooting commands
sudo minikube id      # Cluster IP
sudo minikube logs    # Logs when starting up
sudo minikube version # version your using
sudo minikube update-check # Shows your verison of minikube and the latest available




```


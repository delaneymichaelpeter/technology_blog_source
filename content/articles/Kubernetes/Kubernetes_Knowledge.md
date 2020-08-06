Title: Kubernetes Commands
Date: 2020-07-28 10:20
Modified: 2020-07-28 10:20
Tags: kubernetes, opensource
Category: Kubernetes
Slug: Kubernetes
Authors: Peter Delaney 
Summary: Kubernetes Useful Commands


## Useful Kubernetes command line commands
These commands are run on the Master node and NOT the Worker nodes
```bash
# See how many pods are running
kubectl get pods  # Should display number of pods running

kubectl get pods -n kube-system  # Displays the system level pods that are running in your cluster

# Install Pod nginx kubectl exeucte the yaml cat into it  Should have an nginx pod running
cat << EOF | kubectl create -f -
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  containers:
  - name: nginx
    image: nginx
EOF

# See if nginx is running
kubectl get pods

# Command to describe a pod  (nginx) is the pod we just installed
kubectl describe pod nginx

# Delete our nginx pod
kubectl delete pod nginx

# List of Kubernetes Nodes
kubectl get nodes

# Describe information in a Node
kubectl describe node <node-name>

# Get List of Deployments if any
kubectl get deployments   # List all of the deployments

kubectl describe deployment <name-of-deployment>  # Information about the deployment

# Get list of Kubernetes Services
kubectl get svc
kubectl get service  # same commands


# Create Kubernetes namespace
kubectl create namespace <namespace-name>
kubectl -n <namespace-name> create -f ~/file.yaml  # create service in our namespace
kubectl get pods -n <namespace-name>  # List pods in that namespace

# Note if you  did not specify the namespace you would NOT see any pods


# Get Pods for All Name spaces
kubectl get pods --all-namespaces



```

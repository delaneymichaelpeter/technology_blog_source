Title: Kubernetes Commands
Date: 2020-07-28 10:20
Modified: 2020-08-06 10:20
Tags: kubernetes, opensource, linux
Category: Kubernetes
Slug: Kubernetes-Commands
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


# List of Kubernetes namespaces for this cluster
kubectl get namespaces

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

# Example of Creating Pod in Cluster with Two Containers

In this example create a Pod, podexample, that contains two container images running
One is nginx and the other is a debian container that is spitting out the date into
the html/ directory.  This html directory is a shared directory amoung the two containers
running in this pod.

```bash
# Create Namespace for our Pod
kubectl create --namespace podexample

# Create Pod using yaml file below
kubectl create -f ./pod-example.yaml

# Show the Pod is running
kubectl --namespace podexample get pods

# Get IP of pods
kubectl --namespace podexample get pods -o wide

# Curl the IP should see output from while-loop
curl <ip>

# Delete The Pod
kubectl --namespace podexample delete pod examplepod

```

## YAML file containing nginx and bash script in debian container
Yaml to create our pod with two containers

```bash
apiVersion: v1
kind: Pod
metadata:
  name: examplepod
  namespace: pod-example
spec:
  volumes:   # Create volume 
  - name: html
    emptyDir: {}
    containers:
  - name: webcontainer  # Create nginx container
    image: nginx
    volumeMounts:
    - name: html
      mountPath: /usr/share/nginx/html
  - name: filecontainer  # Create file container spitting out to volumeMounts
    image: debian
    volumeMounts:
    - name: html
      mountPath: /html
    command: ["/bin/sh", "-c"]
    args:
      - while true; do
          date >> /html/index.html;
          sleep 1;
        done
		      
```
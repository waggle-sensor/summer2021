### Overview

* Open source container-orchestration system for automating computer application deployment, scaling, and management. In short, it is a tool to manage coontainers.
* Relevant Youtube link: https://www.youtube.com/watch?v=S3FVcdZcZnA
* Documentation: https://kubernetes.io/docs/concepts/overview/what-is-kubernetes/

![image](https://user-images.githubusercontent.com/56851781/124295193-90d43a80-db26-11eb-94ef-03f990c9c13e.png)

### Kubernetes components
* When you deploy Kubernetes, you get a cluster.
* Here's the diagram of a Kubernetes cluster with all the components tied together.

![image](https://user-images.githubusercontent.com/56851781/124334240-791ba700-db64-11eb-9c9c-5d58acdb2ec8.png)

### Nodes
* A node may be a virtual or physical machine, depending on the cluster.
* Each node is managed by the control plane and contains the services necessary to run Pods.
* There are two main ways to have Nodes added to the API server:
1) The kubelet on a node self-registers to the control plane
2) You (or another human user) manually add a Node object


### Download through Docker desktop
![image](https://user-images.githubusercontent.com/56851781/124333701-052ccf00-db63-11eb-93a2-7782aa19732b.png)

* Install and Set up Kubectl on Windows using curl: https://kubernetes.io/docs/tasks/tools/install-kubectl-windows/

* kubectl config current-context gives you the current context of what is configure for kubectl first.

![image](https://user-images.githubusercontent.com/56851781/124334593-8e450580-db65-11eb-96c1-655d50e1916e.png)


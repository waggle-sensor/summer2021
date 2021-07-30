### What changed

![image](https://user-images.githubusercontent.com/56851781/124829190-4697f280-df46-11eb-9278-2aff17243b90.png)

source from https://aws.amazon.com/ko/getting-started/hands-on/break-monolith-app-microservices-ecs-docker-ec2/


### Docker Overview

* Platform as a service products that use OS-level virtualization to deliver software in containers.
* To fix environment disparity
* Image: a blueprint of your container. (Instructions for building your container)
* Snapshot: Image is made up of layers. Base layer(Debian etc), another layer(software files), add another one...
* When your blueprint(image) is run, it is a container.
* Relevant Youtube link: https://www.youtube.com/watch?v=chnCcGCTyBg, https://www.youtube.com/watch?v=i7ABlHngi1Q&t=859s
* Docker flows

![image](https://user-images.githubusercontent.com/56851781/126398634-cf4ee24e-2a36-4421-822d-c18e7e93a590.png)

![image](https://user-images.githubusercontent.com/56851781/126391893-3a69174f-52dc-4e14-923e-872af10898bd.png)

* Docker daemon: it is a persistent background process that manages the containers on a single host. It is a self-sufficient runtime that manages Docker objects such as images, containers, network, and storage. By default, Docker daemon creates a non-networked Unix domain socket at /var/run/docker.


### Simple tutorial

![image](https://user-images.githubusercontent.com/56851781/124818095-98d21700-df38-11eb-87ff-0af2aa27bb92.png)

![image](https://user-images.githubusercontent.com/56851781/124816276-4ee83180-df36-11eb-9fb8-94ed30fae2c6.png)

* docker images
* docker ps -a
* docker rm containerID
* docker ps -a
* docker exec -it containerID bash  (echo)


### Kubernetes Overview

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


### GET commands
* kubectl get resource

![image](https://user-images.githubusercontent.com/56851781/124336355-b7689480-db6b-11eb-9f82-f05ea8d124fe.png)


### Describe command
* kubectl describe resource name

![image](https://user-images.githubusercontent.com/56851781/124336734-1da1e700-db6d-11eb-9732-a051304881b1.png)


### Xml, Json and Yaml
* https://www.inflearn.com/questions/16184
* In Kubernetes, json used to send API things, but Yaml recommended

<img width="690" alt="Screen Shot 2021-07-06 at 11 27 51 AM" src="https://user-images.githubusercontent.com/56851781/124627135-4bc54680-de4d-11eb-9889-f4045b26c786.png">



### Node-RED on Docker

Docker Pull Command: docker pull nodered/node-red or visit: https://hub.docker.com/r/nodered/node-red

![image](https://user-images.githubusercontent.com/56851781/124831525-595ff680-df49-11eb-8bfd-8ac4adb44a30.png)

* localhost:1880 or http://127.0.0.1:1880

![image](https://user-images.githubusercontent.com/56851781/124831688-975d1a80-df49-11eb-9149-edf509626d88.png)

* docker (re)start nodered
* docker exec -it mynodered /bin/bash

![image](https://user-images.githubusercontent.com/56851781/124832702-0edf7980-df4b-11eb-9fa8-094c2f5f5cdd.png)

![image](https://user-images.githubusercontent.com/56851781/124833540-561a3a00-df4c-11eb-8b98-4c79d3ae0645.png)

* nodejs server deploy on Docker: https://ho1234c.github.io/2017/01/31/2017-01-31-docker-nodejs/index.html




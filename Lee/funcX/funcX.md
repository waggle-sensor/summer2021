### Severless Computing

- It is a cloud computing execution model in which the cloud provider allocates machine resources on demand, taking care of the servers on behalf of their customers.
- It does not hold resources in volatile memory; computing is rather done in short bursts with the results persisted to storage. When an app is not in use, there are no computing resources allocated to the app. Pricing is based on the actual amount of resources consumed by an application.
- It can be a form of utility computing. "Serverless" is a misnomer in the sense that servers are still used by cloud service providers to execute code for developers.
- However, developers of serverless applications are not concerned with capacity planning, configuration, management, maintenance, fault tolerance, or scaling of containers, VMs, or physical servers.


### FaaS (Function as a Service)

- FaaS is a platform allowing customers to develop, run, and manage application functionalities without the complexity of building and maintaining the infrastructure typically associated with developing and launching an app.
- FuncX works like other FaaS platforms: users first register a function with funcX by specifying the function body (in Python), they may then execute that function by specifying the function ID and input arguments. Unlike traditional FaaS platforms, users also specify the endpoint ID on which they wish to execute the function.
- FuncX endpoints are user-managed and may be configured on a wide range of resources from laptops and scientific instruments through to supercomputers. The funcX endpoint can be configured to execute functions locally (i.e., using multiple processes) or on connected computing resources (i.e., by provisioning and managing compute nodes from a batch scheduler or cloud API).
- FuncX implements a reliable fire-and-forget execution model. After invoking a function, a user can close their laptop and rely on funcX to manage the execution and store the results. funcX securely communicates with remote endpoints, waits for resources to become available, and can even retry execution upon failure. funcX stores results (or errors) in the cloud-hosted service until they are retrieved by the user.

- Reference: https://funcx.readthedocs.io/_/downloads/en/latest/pdf/

#### 1. Installation
<img width="802" alt="Screen Shot 2021-08-03 at 5 49 50 PM" src="https://user-images.githubusercontent.com/56851781/128090997-37a0f992-3c8e-4efb-8def-af6081f1ab10.png">

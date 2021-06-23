### Node-RED


* Node-RED inherits general functionality from FBP tools, which is Flow-Based-Programming.
* exchanges data across pre-defined connections by message passing, where the connections are specified externally to the processes.
* can continue executing and functioning, as long as there is data to work on and destination for the output.
* generally runs in less elapsed time than conventional programs, and make optimal use of many processors on a machine, with no special programming required to achieve this. 

## 6 core Nodes: inject, debug, function, change, switch, and template.
* Each Node offers different functionality, which can range from a simple debug node to be able to see what's going on in your flow.

1. Inject Node literally, is to manual trigger, which is input.
2. On the other hands, debug, is output. This node can be used to display messages.payload from the flow by default.
3. Change node can be used to modify a message’s properties and set context properties without having to resort to a Function node. (relatively limited in what it can do and is not designed to loop or make complex logical decisions. Alternative: Function node)
![image](https://user-images.githubusercontent.com/56851781/122111337-9e32ba80-cded-11eb-986b-3ea16065b181.png)

4. Function node allows JavaScript code to be run against the messages that are passed through it.
![image](https://user-images.githubusercontent.com/56851781/122111629-f669bc80-cded-11eb-8c0d-853dc4104993.png)

5. Switch node allows messages to be routed to different branches of a flow by evaluating a set of rules against each message.
6. Template node can be used to generate text using a message’s properties to fill out a template.

* Plus, sub-flow: (all from the one source, want to change all in the Subflows-Selection to Subflow)
![image](https://user-images.githubusercontent.com/56851781/122114092-e43d4d80-cdf0-11eb-8431-b25f25301a56.png)


## context, flow and global
* 3 different levels to set/modify persistent variables with the range of their access is referred to as variable scope.
![image](https://user-images.githubusercontent.com/56851781/122116772-01bfe680-cdf4-11eb-8083-0b03d3bb09bf.png)

* to fix "undefined", can increase the scope of count by going into the function and changing 'context' to 'flow'
![image](https://user-images.githubusercontent.com/56851781/122117136-814db580-cdf4-11eb-94d0-4e2194dc3631.png)

* while these global variables are universally accessible, some applications may be better off using a link node to share data between flows. (cause link nodes not only share variables but also trigger different flows across projects in a sequences predictable way.) 
![image](https://user-images.githubusercontent.com/56851781/122117817-52840f00-cdf5-11eb-8888-89f795e5fbcc.png)
![image](https://user-images.githubusercontent.com/56851781/122118684-4d738f80-cdf6-11eb-9094-d3952a2e88ea.png)


## Tutorials:
* 1. This flow demonstrates the basic concept of creating a flow. It shows how the Inject node can be used to manually trigger a flow, and how the Debug node displays messages in the sidebar. It also shows how the Function node can be used to write custom JavaScript to run against messages. You can compared two different inject nodes.
![image](https://user-images.githubusercontent.com/56851781/123179651-d6727280-d457-11eb-8640-504c3279edaa.png)

* 2. This flow is automatically triggered every 5 minutes and retrieves data from https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/significant_month.csv. It parses the data and displays in the Debug sidebar. It also checks the magnitude value in the data and branches the flow for any messages with a magnitude greater than, or equal to, 7. The payloads of such messages are modified and displayed in the Debug sidebar.
![image](https://user-images.githubusercontent.com/56851781/123179781-15082d00-d458-11eb-9891-a819a3b9f6ff.png)


 


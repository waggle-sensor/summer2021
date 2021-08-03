### Overview

* Node-RED inherits general functionality from FBP tools, which is Flow-Based-Programming.
* exchanges data across pre-defined connections by message passing, where the connections are specified externally to the processes.
* can continue executing and functioning, as long as there is data to work on and destination for the output.
* generally runs in less elapsed time than conventional programs, and make optimal use of many processors on a machine, with no special programming required to achieve this. 

![image](https://user-images.githubusercontent.com/56851781/128030672-8a387152-234a-4775-b2d3-dee2f92ddad0.png)
![image](https://user-images.githubusercontent.com/56851781/128030729-adc73010-77bb-439a-84be-01d8f40a9643.png)

* There are several main space of Node-RED: Palette (Searching nodes), Workspace, and Sidebar. 
1) You can find basic nodes on Palette. The palette contains all of the nodes that are installed and available to use. You have to install the specific package such as Slack nodes through Node-RED menu -> “Manage Pallete” -> “Install” -> slack nodes (for example).
2) The main workspace is where flows are developed by dragging nodes from the palette and wiring them together. The workspace has a row of tabs along the top; one for each flow and any subflows that have been opened.
3) The sidebar contains panels that provide a number of useful tools within the editor.
    Information - view information about nodes and their help
    Debug - view messages passed to Debug nodes
    Configuration Nodes - manage configuration nodes
    Context data - view the contents of context
    Also, some nodes contribute their own sidebar panels, such as node-red-dashboard.
    
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

## Code import/export

- Flows can be imported and exported from the editor using their JSON format, making it very easy to share flows with others.
 
![image](https://user-images.githubusercontent.com/56851781/128033491-830d312b-e774-4904-9cb6-9f5556c02478.png)


- Inject-Debug node example flows

[{"id":"83e21f0c.51fe8","type":"inject","z":"82f46bd8.467668","name":"inject (timestamp)","props":[{"p":"payload"},{"p":"topic","vt":"str"}],"repeat":"","crontab":"","once":false,"onceDelay":0.1,"topic":"","payload":"","payloadType":"date","x":147,"y":155,"wires":[["ded689fa.e85558","fbc74ccf.c5f4c"]]},{"id":"ded689fa.e85558","type":"debug","z":"82f46bd8.467668","name":"String_payload (default)","active":true,"tosidebar":true,"console":false,"tostatus":false,"complete":"payload","targetType":"msg","statusVal":"","statusType":"auto","x":607,"y":155,"wires":[]},{"id":"e9076cc8.0205","type":"comment","z":"82f46bd8.467668","name":"Inject-Debug node","info":"Inject Node:\n- The Inject node can be used to manual trigger a flow by clicking the node’s button within the editor.\n- It can also be used to automatically trigger flows at regular intervals.\n- The message sent by the Inject node can have its payload and topic properties set.\n- The payload can be set to a variety of different types:\n    a flow or global context property value\n    a String, number, boolean, Buffer or Object\n\nDebug Node:\n- The Debug node can be used to display messages in the Debug sidebar within the editor.\n- The sidebar provides a structured view of the messages it is sent, making it easier to explore the message.\n- Alongside each message, the debug sidebar includes information about the time the message was received and which Debug node sent it. Clicking on the source node id will reveal that node within the workspace.\n- The button on the node can be used to enable or disable its output. It is recommended to disable or remove any Debug nodes that are not being used.\n- The node can also be configured to send all messages to the runtime log, or to send short (32 characters) to the status text under the debug node.\n\n- Reference\nhttps://nodered.org/docs/user-guide/nodes","x":127,"y":115,"wires":[]},{"id":"fbc74ccf.c5f4c","type":"debug","z":"82f46bd8.467668","name":"Object_complete msg","active":true,"tosidebar":true,"console":false,"tostatus":false,"complete":"true","targetType":"full","statusVal":"","statusType":"auto","x":597,"y":204,"wires":[]},{"id":"287e4fab.096af","type":"comment","z":"82f46bd8.467668","name":"msg.payload : string","info":"","x":906,"y":158,"wires":[]},{"id":"4e9cbb5a.bd9c64","type":"comment","z":"82f46bd8.467668","name":"msg.payload : object","info":"","x":907,"y":204,"wires":[]}]


- Change node example flows

[{"id":"3da44e09.157f22","type":"inject","z":"82f46bd8.467668","name":"inject (Hello World)","props":[{"p":"payload"},{"p":"topic","vt":"str"}],"repeat":"","crontab":"","once":false,"onceDelay":0.1,"topic":"","payload":"Hello World","payloadType":"str","x":158,"y":341,"wires":[["36e9d5c4.f52dda","f94b8144.954de"]]},{"id":"f55a88b8.aa3ea8","type":"debug","z":"82f46bd8.467668","name":"String_payload (default) through change node","active":true,"tosidebar":true,"console":false,"tostatus":false,"complete":"payload","targetType":"msg","statusVal":"","statusType":"auto","x":678,"y":400,"wires":[]},{"id":"f16d1273.35f3f","type":"comment","z":"82f46bd8.467668","name":"Change node","info":"Change Node:\n- The Change node can be used to modify a message’s properties and set context properties without having to resort to a Function node.\n- Each node can be configured with multiple operations that are applied in order. The available operations are:\n\n    Set - set a property. The value can be a variety of different types, or can be taken from an existing message or context property.\n    Change - search and replace parts of a message property.\n    Move - move or rename a property.\n    Delete - delete a property.\n\n- When setting a property, the value can also be the result of a JSONata expression. JSONata is a declarative query and transformation language for JSON data.\n\n- Refernece\nhttps://nodered.org/docs/user-guide/nodes#change","x":108,"y":301,"wires":[]},{"id":"36e9d5c4.f52dda","type":"change","z":"82f46bd8.467668","name":"change payload","rules":[{"t":"change","p":"payload","pt":"msg","from":"World","fromt":"str","to":"Node-RED","tot":"str"}],"action":"","property":"","from":"","to":"","reg":false,"x":373,"y":400,"wires":[["f55a88b8.aa3ea8"]]},{"id":"f94b8144.954de","type":"debug","z":"82f46bd8.467668","name":"String_payload (default)","active":true,"tosidebar":true,"console":false,"tostatus":false,"complete":"payload","targetType":"msg","statusVal":"","statusType":"auto","x":608,"y":340,"wires":[]}]


- Variation: http node + csv node + switch node + change node example flows

[{"id":"e36406f2.8ef798","type":"inject","z":"82f46bd8.467668","name":"inject","props":[{"p":"payload"},{"p":"topic","vt":"str"}],"repeat":"","crontab":"","once":false,"onceDelay":"","topic":"","payload":"","payloadType":"str","x":109,"y":568,"wires":[["c3c50023.3bbed"]]},{"id":"c3c50023.3bbed","type":"http request","z":"82f46bd8.467668","name":"Recent Quakes","method":"GET","paytoqs":"ignore","url":"https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/significant_month.csv","tls":"","persist":false,"proxy":"","authType":"","x":279,"y":568,"wires":[["8afc6cac.e0812"]]},{"id":"8afc6cac.e0812","type":"csv","z":"82f46bd8.467668","name":"csv","sep":",","hdrin":true,"hdrout":"","multi":"one","ret":"\\n","temp":"","skip":0,"strings":true,"include_empty_strings":false,"include_null_values":false,"x":453,"y":568,"wires":[["44779781.4190f8","6f0eb546.9e208c"]]},{"id":"44779781.4190f8","type":"debug","z":"82f46bd8.467668","name":"Object_complete msg","active":true,"tosidebar":true,"console":false,"tostatus":false,"complete":"true","targetType":"full","statusVal":"","statusType":"auto","x":800,"y":568,"wires":[]},{"id":"6f0eb546.9e208c","type":"switch","z":"82f46bd8.467668","name":"switch the value","property":"payload.mag","propertyType":"msg","rules":[{"t":"gte","v":"5","vt":"num"}],"checkall":"true","repair":false,"outputs":1,"x":547,"y":628,"wires":[["d78d4aa8.8c8208"]]},{"id":"d78d4aa8.8c8208","type":"change","z":"82f46bd8.467668","name":"change msg","rules":[{"t":"set","p":"payload","pt":"msg","to":"Danger!","tot":"str"}],"action":"","property":"","from":"","to":"","reg":false,"x":665,"y":689,"wires":[["72fddece.fac0d"]]},{"id":"72fddece.fac0d","type":"debug","z":"82f46bd8.467668","name":"String_payload (default)","active":true,"tosidebar":true,"console":false,"tostatus":false,"complete":"payload","targetType":"msg","statusVal":"","statusType":"auto","x":810,"y":628,"wires":[]},{"id":"f7405676.6a1e38","type":"comment","z":"82f46bd8.467668","name":"Variation: http node + csv node + switch node + change node","info":"Switch node:\n- The Switch node allows messages to be routed to different branches of a flow by evaluating a set of rules against each message.\n- The name \"switch\" comes from the \"switch statement\" that is common to many programming languages. It is not a reference to a physical switch\n- The node is configured with the property to test - which can be either a message property or a context property.\n- There are four types of rule:\n    Value rules are evaluated against the configured property\n    Sequence rules can be used on message sequences, such as those generated by the Split node\n    A JSONata Expression can be provided that will be evaluated against the whole message and will match if the expression returns a true value.\n    An Otherwise rule can be used to match if none of the preceding rules have matched.\n- The node will route a message to all outputs corresponding to matching rules. But it can also be configured to stop evaluating rules when it finds one that matches.\n\nHttp node:\n- It sends HTTP requests and returns the response.\n- At least one inject node/debug node are required.\n\n- Reference\nhttps://nodered.org/docs/user-guide/nodes","x":259,"y":528,"wires":[]}]


- Variation: split node + change node + switch node example flows

[{"id":"d193c5c2.296848","type":"split","z":"82f46bd8.467668","name":"","splt":",","spltType":"str","arraySplt":1,"arraySpltType":"len","stream":false,"addname":"","x":329,"y":930,"wires":[["4248bbe2.589704","3b0fab6c.79f274"]]},{"id":"624297b1.7e7958","type":"inject","z":"82f46bd8.467668","name":"","props":[{"p":"payload"},{"p":"topic","vt":"str"}],"repeat":"","crontab":"","once":true,"onceDelay":"","topic":"","payload":"15.4,50,23.8,79","payloadType":"str","x":139,"y":930,"wires":[["7a59ebd3.21ad74","d193c5c2.296848"]]},{"id":"d0c71ac6.5b5b68","type":"debug","z":"82f46bd8.467668","name":"out 1","active":true,"tosidebar":true,"console":false,"tostatus":false,"complete":"payload","x":849,"y":870,"wires":[]},{"id":"4248bbe2.589704","type":"change","z":"82f46bd8.467668","name":"to number","rules":[{"t":"set","p":"payload","pt":"msg","to":"$number(msg.payload)\t","tot":"jsonata"}],"action":"","property":"","from":"","to":"","reg":false,"x":499,"y":930,"wires":[["5db41d9f.1a37b4","331d50e5.6344a"]]},{"id":"5db41d9f.1a37b4","type":"switch","z":"82f46bd8.467668","name":"route","property":"parts.index","propertyType":"msg","rules":[{"t":"eq","v":"0","vt":"num"},{"t":"eq","v":"1","vt":"str"},{"t":"eq","v":"2","vt":"str"},{"t":"eq","v":"3","vt":"str"}],"checkall":"true","repair":false,"outputs":4,"x":669,"y":930,"wires":[["d0c71ac6.5b5b68"],["d07bd59f.3e7c38"],["1ac0492f.04cfa7"],["1c7471ae.829c0e"]]},{"id":"d07bd59f.3e7c38","type":"debug","z":"82f46bd8.467668","name":"out 2","active":true,"tosidebar":true,"console":false,"tostatus":false,"complete":"payload","x":849,"y":910,"wires":[]},{"id":"1ac0492f.04cfa7","type":"debug","z":"82f46bd8.467668","name":"out 3","active":true,"tosidebar":true,"console":false,"tostatus":false,"complete":"payload","x":849,"y":950,"wires":[]},{"id":"1c7471ae.829c0e","type":"debug","z":"82f46bd8.467668","name":"out 4","active":true,"tosidebar":true,"console":false,"tostatus":false,"complete":"payload","x":849,"y":990,"wires":[]},{"id":"fe9e8df0.56cdc","type":"comment","z":"82f46bd8.467668","name":"split","info":"Split comma separated string into separated messages.\nValue placed to msg.payload\nValue type will be still string.\n\nThere will be 4 messages out of this split node\n\nFor each msg also given a property \"parts\". \nIt will be used later on.","x":329,"y":870,"wires":[]},{"id":"679b270b.7bb908","type":"comment","z":"82f46bd8.467668","name":"convert","info":"Convert the value of msg.payload to the number using JSONata expression.\n","x":509,"y":870,"wires":[]},{"id":"f48c86db.1e34e8","type":"comment","z":"82f46bd8.467668","name":"route","info":"Route every message to differet output by using switch node.\nAs property \"parts\" has been given to each message, we can use its \n\"index\" property to find out proper output\n\n","x":669,"y":870,"wires":[]},{"id":"7a59ebd3.21ad74","type":"debug","z":"82f46bd8.467668","name":"source data","active":true,"tosidebar":true,"console":false,"tostatus":false,"complete":"payload","statusVal":"","statusType":"auto","x":329,"y":1090,"wires":[]},{"id":"3b0fab6c.79f274","type":"debug","z":"82f46bd8.467668","name":"spltted","active":true,"tosidebar":true,"console":false,"tostatus":false,"complete":"true","statusVal":"","statusType":"auto","x":449,"y":1050,"wires":[]},{"id":"331d50e5.6344a","type":"debug","z":"82f46bd8.467668","name":"converted","active":true,"tosidebar":true,"console":false,"tostatus":false,"complete":"true","x":579,"y":1010,"wires":[]},{"id":"675206df.1aa098","type":"comment","z":"82f46bd8.467668","name":"Variation: split node + change node + switch node","info":"Split node:\n- The split node can be used to split the message into one message per line.\n- It can be followed by the nodes needed to operate on the individual lines of text, followed by a Join node to recombine them back into a single block of text.\n\n- Reference\nhttps://cookbook.nodered.org/basic/split-text","x":219,"y":830,"wires":[]}]


- Function node example flows 1

[{"id":"a2255a15.e10ee8","type":"inject","z":"82f46bd8.467668","name":"inject (Hello World)","props":[{"p":"payload"},{"p":"topic","vt":"str"}],"repeat":"","crontab":"","once":false,"onceDelay":0.1,"topic":"","payload":"Hello World","payloadType":"str","x":149,"y":1270,"wires":[["c0e20dda.5816a"]]},{"id":"7f024519.91e59c","type":"debug","z":"82f46bd8.467668","name":"String_payload (default)","active":true,"tosidebar":true,"console":false,"tostatus":false,"complete":"payload","targetType":"msg","statusVal":"","statusType":"auto","x":596,"y":1270,"wires":[]},{"id":"bab030cf.73d26","type":"comment","z":"82f46bd8.467668","name":"Function node","info":"Function node:\n- The Function node allows JavaScript code to be run against the messages that are passed through it.\n- The message is passed in as an object called msg. By convention it will have a msg.payload property containing the body of the message.\n- Other nodes may attach their own properties to the message, and they should be described in their documentation.\n\n- Reference\nhttps://nodered.org/docs/user-guide/nodes#function","x":99,"y":1230,"wires":[]},{"id":"c0e20dda.5816a","type":"function","z":"82f46bd8.467668","name":"","func":"var newString = msg.payload.replace(\"World\",\"Node-RED\")\nreturn { payload : newString };\n\n// - Refenrece\n// https://nodered.org/docs/user-guide/writing-functions","outputs":1,"noerr":0,"initialize":"","finalize":"","libs":[],"x":359,"y":1270,"wires":[["7f024519.91e59c"]]}]


- Function node example flows 2

[{"id":"58ffae9d.a7005","type":"debug","z":"82f46bd8.467668","name":"Object_complete msg","active":true,"tosidebar":true,"console":false,"tostatus":false,"complete":"true","targetType":"full","statusVal":"","statusType":"auto","x":576,"y":1494,"wires":[]},{"id":"17626462.e89d9c","type":"inject","z":"82f46bd8.467668","name":"inject (timestamp)","props":[{"p":"payload"}],"repeat":"","crontab":"","once":false,"onceDelay":"","topic":"","payload":"","payloadType":"date","x":134,"y":1437,"wires":[["2921667d.d6de9a","36f12856.431a08"]]},{"id":"2921667d.d6de9a","type":"function","z":"82f46bd8.467668","name":"Date(msg.payload) ","func":"// Create a Date object from the payload\nvar date = new Date(msg.payload);\n// Change the payload to be a formatted Date string\nmsg.payload = date.toString();\n// Return the message so it can be sent on\nreturn msg;","outputs":1,"noerr":0,"initialize":"","finalize":"","libs":[],"x":346,"y":1494,"wires":[["58ffae9d.a7005"]]},{"id":"a10dfb07.bf53b8","type":"comment","z":"82f46bd8.467668","name":"Function node 2","info":"","x":108,"y":1398,"wires":[]},{"id":"36f12856.431a08","type":"debug","z":"82f46bd8.467668","name":"Object_complete msg","active":true,"tosidebar":true,"console":false,"tostatus":false,"complete":"true","targetType":"full","statusVal":"","statusType":"auto","x":574,"y":1437,"wires":[]}]


- Variation: http node + function node example flows

[{"id":"78397f95.49945","type":"inject","z":"82f46bd8.467668","name":"inject (trigger http request)","props":[{"p":"payload"},{"p":"topic","vt":"str"}],"repeat":"","crontab":"","once":false,"onceDelay":0.1,"topic":"","payload":"","payloadType":"str","x":163,"y":1653,"wires":[["24f0635e.244afc"]]},{"id":"24f0635e.244afc","type":"http request","z":"82f46bd8.467668","name":"","method":"GET","ret":"obj","paytoqs":"body","url":"http://ipinfo.io","tls":"","persist":false,"proxy":"","authType":"","x":379,"y":1653,"wires":[["fc467855.bb21c8"]]},{"id":"fc467855.bb21c8","type":"function","z":"82f46bd8.467668","name":"","func":"var msg2 = {};\nmsg2.cidade = msg.payload.city;\nmsg2.pais = msg.payload.country;\nreturn [msg,msg2];","outputs":2,"noerr":0,"initialize":"","finalize":"","libs":[],"x":592.0000610351562,"y":1743,"wires":[["f26dc46f.e80388"],["9434dba3.28e278"]]},{"id":"b92c0ac3.7bcf48","type":"comment","z":"82f46bd8.467668","name":"Variation: http node + function node","info":"","x":169,"y":1614,"wires":[]},{"id":"9434dba3.28e278","type":"debug","z":"82f46bd8.467668","name":"Object_complete msg","active":true,"tosidebar":true,"console":false,"tostatus":false,"complete":"true","targetType":"full","statusVal":"","statusType":"auto","x":774,"y":1775,"wires":[]},{"id":"abb43ed4.62e86","type":"comment","z":"82f46bd8.467668","name":"msg.payload : object (query)","info":"It returns cidade, pais, and msgid.","x":1050,"y":1776,"wires":[]},{"id":"2deb7549.6aab6a","type":"comment","z":"82f46bd8.467668","name":"msg.payload : object","info":"It returns _msgid, payload, topic, statusCode, headers, responseUrl, redirectList.","x":1021,"y":1715,"wires":[]},{"id":"f26dc46f.e80388","type":"debug","z":"82f46bd8.467668","name":"Object_complete msg","active":true,"tosidebar":true,"console":false,"tostatus":false,"complete":"true","targetType":"full","statusVal":"","statusType":"auto","x":775,"y":1713,"wires":[]}]


## sub-flow

* All from the one source, want to change all in the Subflows-Selection to Subflow

![image](https://user-images.githubusercontent.com/56851781/122114092-e43d4d80-cdf0-11eb-8431-b25f25301a56.png)


## context, flow and global

* 3 different levels to set/modify persistent variables with the range of their access is referred to as variable scope.

![image](https://user-images.githubusercontent.com/56851781/122116772-01bfe680-cdf4-11eb-8083-0b03d3bb09bf.png)

* to fix "undefined", can increase the scope of count by going into the function and changing 'context' to 'flow'

![image](https://user-images.githubusercontent.com/56851781/122117136-814db580-cdf4-11eb-94d0-4e2194dc3631.png)

* while these global variables are universally accessible, some applications may be better off using a link node to share data between flows. (cause link nodes not only share variables but also trigger different flows across projects in a sequences predictable way.) 

![image](https://user-images.githubusercontent.com/56851781/122117817-52840f00-cdf5-11eb-8888-89f795e5fbcc.png)
![image](https://user-images.githubusercontent.com/56851781/122118684-4d738f80-cdf6-11eb-9094-d3952a2e88ea.png)


## Node-RED Dashboard

* To install the stable version use the Menu - Manage palette option and search for node-red-dashboard, or run the following command in your Node-RED user directory - typically `~/.node-red`:

``npm i node-red-dashboard``

![image](https://user-images.githubusercontent.com/56851781/128036961-151b081a-c6e2-49ea-a687-158dbe597be6.png)





## Tutorials https://nodered.org/docs/tutorials/

1. This flow demonstrates the basic concept of creating a flow. It shows how the Inject node can be used to manually trigger a flow, and how the Debug node displays messages in the sidebar. It also shows how the Function node can be used to write custom JavaScript to run against messages. You can compared two different inject nodes.

![image](https://user-images.githubusercontent.com/56851781/123179651-d6727280-d457-11eb-8640-504c3279edaa.png)

2. This flow is automatically triggered every 5 minutes and retrieves data from https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/significant_month.csv. It parses the data and displays in the Debug sidebar. It also checks the magnitude value in the data and branches the flow for any messages with a magnitude greater than, or equal to, 7. The payloads of such messages are modified and displayed in the Debug sidebar.

![image](https://user-images.githubusercontent.com/56851781/123179781-15082d00-d458-11eb-9891-a819a3b9f6ff.png)


 


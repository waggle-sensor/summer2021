### Overview

* [Node-RED_beginner.md](https://github.com/waggle-sensor/summer2021/blob/main/Lee/nodered_examples/Node-RED_beginner.md) explains fundamental and core nodes on Node-RED.
* The following instructions for node-RED flows are based on [Querying Measurements.](https://github.com/waggle-sensor/waggle-beehive-v2/blob/main/docs/querying-measurements.md)
* Each node has README.md files, which is available for everyone.
* The main core nodes for SAGE project includes inject, http request, function and debug nodes as shown in example below.

![image](https://user-images.githubusercontent.com/56851781/128259245-9fd5e4cc-159f-473e-abdc-4dd4b897e447.png)

- Basic example flows

```
[{"id":"3be83825.4cde68","type":"inject","z":"f361ffeb.71386","name":"inject node","props":[{"p":"payload"},{"p":"topic","vt":"str"}],"repeat":"","crontab":"","once":false,"onceDelay":0.1,"topic":"","payload":"","payloadType":"date","x":119,"y":164,"wires":[["a56acc12.d8823"]]},{"id":"a56acc12.d8823","type":"http request","z":"f361ffeb.71386","name":"http request node","method":"GET","ret":"txt","paytoqs":"ignore","url":"","tls":"","persist":false,"proxy":"","authType":"","x":309,"y":164,"wires":[["9542c05a.0a38c"]]},{"id":"87976f6a.fc459","type":"function","z":"f361ffeb.71386","name":"function node","func":"\nreturn msg;","outputs":1,"noerr":0,"initialize":"","finalize":"","libs":[],"x":519,"y":164,"wires":[["95853bb9.a888e8"]]},{"id":"9542c05a.0a38c","type":"debug","z":"f361ffeb.71386","name":"debug node","active":true,"tosidebar":true,"console":false,"tostatus":false,"complete":"payload","targetType":"msg","statusVal":"","statusType":"auto","x":709,"y":164,"wires":[]},{"id":"46cf90f5.42502","type":"comment","z":"f361ffeb.71386","name":"inject node","info":"- The Inject node can be used to manual trigger a flow by clicking the node’s button within the editor.\n- It can also be used to automatically trigger flows at regular intervals.\n- The message sent by the Inject node can have its payload and topic properties set.\n- The payload can be set to a variety of different types:\n    a flow or global context property value\n    a String, number, boolean, Buffer or Object\n    a Timestamp in milliseconds since January 1st, 1970\n\n- Reference\nhttps://nodered.org/docs/user-guide/nodes","x":119,"y":124,"wires":[]},{"id":"e4e246c9.714c78","type":"comment","z":"f361ffeb.71386","name":"http request node","info":"- This node sends HTTP requests and returns the response.\n- As there is no url here, it returns msg : string[16] \"No url specified\" on the debug node.","x":299,"y":124,"wires":[]},{"id":"455db39e.0b896c","type":"comment","z":"f361ffeb.71386","name":"function node","info":"- The Function node allows JavaScript code to be run against the messages that are passed through it.\n- The message is passed in as an object called msg. By convention it will have a msg.payload property containing the body of the message.\n- Other nodes may attach their own properties to the message, and they should be described in their documentation.\n\n- Reference\nhttps://nodered.org/docs/user-guide/nodes\nhttps://nodered.org/docs/user-guide/writing-functions","x":509,"y":124,"wires":[]},{"id":"171c7878.36dc98","type":"comment","z":"f361ffeb.71386","name":"debug node","info":"- The Debug node can be used to display messages in the Debug sidebar within the editor.\n- The sidebar provides a structured view of the messages it is sent, making it easier to explore the message.\n- Alongside each message, the debug sidebar includes information about the time the message was received and which Debug node sent it. Clicking on the source node id will reveal that node within the workspace.\n- The button on the node can be used to enable or disable its output. It is recommended to disable or remove any Debug nodes that are not being used.\n- The node can also be configured to send all messages to the runtime log, or to send short (32 characters) to the status text under the debug node.\n\n- Reference\nhttps://nodered.org/docs/user-guide/nodes","x":709,"y":124,"wires":[]},{"id":"95853bb9.a888e8","type":"slack","z":"f361ffeb.71386","name":"slack node","channelURL":"https://hooks.slack.com/services/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","username":"","emojiIcon":"","channel":"","x":909,"y":244,"wires":[]},{"id":"c2c09e6d.e1cdb","type":"comment","z":"f361ffeb.71386","name":"slack node","info":"You’ll have to install the slack package through Node-RED menu -> “Manage Pallete” -> “Install” -> slack. Then, you’ll want a legacy slack API token to configure this node with webhook. It finally send the message to Slack the messages coming through to Slack from Node-RED.\nIt can be anything such as Email notification.\n\n- Reference\nhttps://nodered.org/docs/user-guide/nodes","x":898,"y":124,"wires":[]}]
```

- In inject node, the query request used by the API is a JSON body.
- Http request node sends HTTP requests and returns the response. If the url is set to example.com/{{{topic}}}, it will have the value of msg.topic automatically inserted. More details are available by clicking the help icon on the right side bar.
- Debug node displays the output. Two options "msg.payload" and "complete msg object" are utilized.
- Function node is used to split, change the data type to help query measurement.
- In order to alarm notification, the slack module was used after installation. 


### All measurements with sys in the last hour

- The following query returns all measurements with a name starting with sys in the last hour. It returns data, which is chunk of string type.

![image](https://user-images.githubusercontent.com/56851781/128259769-e2325847-1d9d-4bc5-ad3d-b4e50c1bab12.png)

- Example flows

```
[{"id":"215a7363.8f1d9c","type":"inject","z":"f361ffeb.71386","name":"SDR_all_sys_1hour","props":[{"p":"payload"}],"repeat":"","crontab":"","once":false,"onceDelay":0.1,"topic":"","payload":"{\"start\":\"-1h\",\"filter\":{\"name\":\"sys.*\"}}","payloadType":"json","x":150,"y":400,"wires":[["b74bf483.dfa2e8"]]},{"id":"b74bf483.dfa2e8","type":"http request","z":"f361ffeb.71386","name":"Sage Data Repository","method":"GET","ret":"txt","paytoqs":"body","url":"https://sdr.sagecontinuum.org/api/v1/query{{{payload.value}}}","tls":"","persist":true,"proxy":"","authType":"basic","x":350,"y":440,"wires":[["83c7882c.28c248"]]},{"id":"83c7882c.28c248","type":"debug","z":"f361ffeb.71386","name":"String_payload (default)","active":true,"tosidebar":true,"console":false,"tostatus":false,"complete":"payload","targetType":"msg","statusVal":"","statusType":"auto","x":590,"y":400,"wires":[]},{"id":"c11b17eb.6dc728","type":"comment","z":"f361ffeb.71386","name":"All measurements with sys in the last hour","info":"The following query will return all measurements with a name starting with sys in the last hour.\nIt returns data, which is chunk of string type.\n\n- Reference\nhttps://github.com/waggle-sensor/waggle-beehive-v2/blob/main/docs/querying-measurements.md","x":200,"y":360,"wires":[]}]
```

- The following query will return all measurements with a name starting with sys in the 1 minute. It returns object from SDR (complete msg object in the debug node), but the payload is still string.

- Once the output displays on debug sidebar, you can click the object. It includes `_msgid`, `payload`, `statusCode`, `headers`, `responseUrl` and `redirectList`.

- **Payload** is still string type.
- **statusCode** 200 means that the HTTP request has succeeded.
- **headers** includes access-control-allow-origin, content-disposition, content-type, date, vary, transfer-encoding and x-node-red-request-node.
- **responseUrl** is same as http request url.

- Example flows

```
[{"id":"4d0d0d47.df3a04","type":"inject","z":"f361ffeb.71386","name":"SDR_all_sys_1minute","props":[{"p":"payload"}],"repeat":"","crontab":"","once":false,"onceDelay":0.1,"topic":"","payload":"{\"start\":\"-1m\",\"filter\":{\"name\":\"sys.*\"}}","payloadType":"json","x":160,"y":600,"wires":[["a82434ec.73fc38"]]},{"id":"a82434ec.73fc38","type":"http request","z":"f361ffeb.71386","name":"Sage Data Repository","method":"GET","ret":"txt","paytoqs":"body","url":"https://sdr.sagecontinuum.org/api/v1/query","tls":"","persist":true,"proxy":"","authType":"basic","x":350,"y":640,"wires":[["a7918e5c.ecd9b"]]},{"id":"a7918e5c.ecd9b","type":"debug","z":"f361ffeb.71386","name":"Object_complete msg","active":true,"tosidebar":true,"console":false,"tostatus":false,"complete":"true","targetType":"full","statusVal":"","statusType":"auto","x":580,"y":600,"wires":[]},{"id":"db2c3c11.1d53a","type":"comment","z":"f361ffeb.71386","name":"All measurements with sys in the last 1 minute","info":"The following query will return all measurements with a name starting with sys in the 1 minute.\nIt returns object from SDR (complete msg object in the debug node), but the payload is still string.\n\nOnce the output displays on debug sidebar, you can click the object. It includes _msgid, payload, statusCode, headers, responseUrl and redirectList.\n- Payload is still string type.\n- \"statusCode: 200\" means that HTTP Status Code 200: The request has succeeded.\n- headers includes access-control-allow-origin, content-disposition, content-type, date, vary, transfer-encoding and x-node-red-request-node.\n- responseUrl is same as http request url. \n\n\n- Reference\nhttps://github.com/waggle-sensor/waggle-beehive-v2/blob/main/docs/querying-measurements.md","x":210,"y":560,"wires":[]}]
```

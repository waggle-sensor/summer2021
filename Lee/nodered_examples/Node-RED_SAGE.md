### Overview

* [Node-RED_beginner.md](https://github.com/waggle-sensor/summer2021/blob/main/Lee/nodered_examples/Node-RED_beginner.md) explains fundamental and core nodes on Node-RED.
* All Node-RED for SDR flows are based on [Querying Measurements.](https://github.com/waggle-sensor/waggle-beehive-v2/blob/main/docs/querying-measurements.md)
* Each node has README.md files, which is available for everyone.
- The following instructions for node-RED flows shows examples querying measurements.
- The main core nodes for SAGE project includes inject, http request, function and debug nodes as shown in example below.
- In inject node, the query request used by the API is a JSON body.
- http request node sends HTTP requests and returns the response. If the url is set to example.com/{{{topic}}}, it will have the value of msg.topic automatically inserted. More - - details are available by clicking the help icon on the right side bar.
- Debug node displays the output. Two options "msg.payload" and "complete msg object" are utilized.
- function node is used to split, change the data type to help query measurement.
- The description of each node can be found the node's comment below.

## 6 core nodes: inject, debug, function, change, switch, and template.
* E

### Node-RED

* Node-RED inherits general functionality from FBP tools, which is Flow-Based-Programming.
* exchanges data across pre-defined connections by message passing, where the connections are specified externally to the processes.
* can continue executing and functioning, as long as there is data to work on and destination for the output.
* generally runs in less elapsed time than conventional programs, and make optimal use of many processors on a machine, with no special programming required to achieve this. 

## 6 core Nodes: inject, debug, function, change, switch, and template.
* Each Node offers different functionality, which can range from a simple debug node to be able to see what's going on in your flow.

1. Inject Node literally, is to manual trigger, which is input.
2. On the other hands, debug, is output. This node can be used to display messages.payload from the flow by default.
3. Function node allows JavaScript code to be run against the messages that are passed through it.
4. Change node can be used to modify a message’s properties and set context properties without having to resort to a Function node. (relatively limited in what it can do and is not designed to loop or make complex logical decisions. Alternative: Function node)
5. Switch node allows messages to be routed to different branches of a flow by evaluating a set of rules against each message.
6. Template node can be used to generate text using a message’s properties to fill out a template.

var msgString = msg.payload.replace("world!", "From Node-RED");
return { payload : newString };

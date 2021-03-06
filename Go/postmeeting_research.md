# Post meeting research

## Doing it the simplest way (LoRa point-to-point communication)
### Pros V Cons:
#### Pros:
- Really simple to start. Can basically just flash C code onto any LoRa enabled transceievers and start updating
- Simple interfacing with the Waggle Node. Basically can process information on the node by sending packet payload through serial
- Easily expandable. Can add another device by turning on the end node (with proper settings) in the proximity of the gateway
- Lower energy consumption when you don't have to also worry about linking a device to a server.
- Easier network maintenance. If there's a problem it's likely a hardware issue since there are never any big changes to software.
- For the single channel gateway that I have right now this works really well since channel jumpign isn't really something i'm concerned with
#### Cons:
- Limited downlink possibilities. Implementing downlink is a lot easier with a network server.
- Not scalable. Managing messages must be implemented into the software instead of using a lot of the built in services
- Still tedious. All of the devices must have some kind of custom ID; with server you can access metadata which can tell you
- Not secure, open to eavesdropping attacks. This is less of a concern since to most people the data is jibberish anyway.

#### Summary:
- Ultimately I think this kind of system would work for very simple networks. Uplink only, where every single end node is fairy unique and spread apart.
- Having a massive number of end nodes (100s) would likely be very difficult. Messages would be constantly crashing into each other.
- With a network server, the gateway could jump between many different channels which would allow larger throughput. Servers also have the ability to jump between spreading factors which have the capability to save energy.
- We could use a system like this as a preliminary blueprint for 

## Downlink
- Downlink not truly supported on a point-to-point communication system. Current architecture is not robust enough to manage both uplink and downlink messages.
    - message acknowledgement is possible however; but that is where the message-receiving capibilities end
    - NOTE: always prioritize message uplink in this system due to the nature of intermittent computing on energy-harvesting devices.
- Even with sever downlink is more limited than uplink due to very narrow bandwidth. I think it would be advantagous to only downlink messages when absolutely necessary and then code the needed behavior into the end node.
- Consider an energy-harvesting sensor. During the time when the sensor is active, the sensor has to collect data, then transmit the data, then potentially listen for an acknowledgement, and then listen for a downlink.

## Security

## Private Servers
### ChirpStack
- ChirpStack gateway bridge: sits between packet forwarder and MQTT broker
    - Transforms the packet into data
    - Cloud platform integration
- gateway bridge can go on the server level or be on every gateway, the latter being more secure. In a network with only one gateway it likely doesn't matter if it is on the gateway or the server however.
- You can have the application and network servers on different computers or you can have it all on one
    - *** This does mean we could just transform the waggle node into both the network/application server
    - unfortunately this is easier said than done. We need to ensure that the other processes on the waggle node are not interrupted
- GatewayOS:
    - ChirpStack has a built in OS that runs on gateways that make it as easy as possible to start using a private network
    - compatible with raspberry pi or a multitude of different shield/kit configurations
    


### things that are different:
- Gateways act just as message forwarders. There is no interpretation done at the gateway level since it is purely physical.
- *** You can actually backhaul data through ethernet. In essence you could wrap the entire server in one device.
- Futhermore you can also put the server on one raspberry pi as mentioned above



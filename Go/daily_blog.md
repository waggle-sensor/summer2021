## Lance Go - Daily Blog

### Week 1 6/14-6/20:
 - Attended initial meeting and student lectures
 - Familiarized myself with OpenCV, Python, and other things I haven't looked at in a while
 - Reviewed publications about Waggle node, looked around the GitHub page
 - Prepared presenation for next week
 - First meeting with Raj
 - Wrote a paragraph summary for the work this summer (NAISE)
 - set up SSH keys


### Week 2 6/21-6/27:
 -  Initial presentation
 - Set up docker
 - First meeting with Prof. Hester of NU
    - Discussed low energy/energy harvesting devices
    - Got me in contact with Prof. Ghena (expert on LoRa)
 - Did some initial research on LoRa and LoRaWan
 - Thursday meeting with Raj
 - More background research on communication with energy harvesting devices
 - Checked out CELS student social
 - Start 10 week plan
 - Attended Sean's tutorial on making plugins for Waggle nodes


### Week 3 6/28-7/04:
##### Monday:
 - Look into the resources that Prof. Ghena sent me: lectures and papers about LoRa and other long range communication protocols
 - Finish up 10 week plan
 - Wrap up research about chirp spread spectrums (CSS) and medium access control (MAC)

##### Tuesday:
 - Continued research into LoRa
 - Specifically looked into alternative communication protocols
    - 802.11ah
    - Bluetooth LE
 - Picked up these LoRa modules from the Ka Moamoa lab: https://www.sparkfun.com/wish_lists/164766
 - Another meeting with Raj to discuss the 10-week plan

##### Wednesday:
 - First lunch with the Waggle team
    - got the Jetson Nano
    - and a few sensors
 - Worked on setting up the gateways and nodes to work with an IDE

##### Thursday:
 - Weekly meeting with Raj
 - Attended weekly lecture series (statistical methods)
 - Looked into SX1262 (end-node) and RFM95 (gateway) data sheets
    - in an end-to-end connection, the same type of LoRa module can be used
 - Simple programming using the ArduinoIDE and the ESP32 microcontroller on the gateway board
 - Problems to fix with the LoRa modules:
    - Flashing the gateways with new code breaks connection with nodes
    - Constantly have to reset the microcontroller (this is a hardware problem)

##### Friday:
 - Set up the RFM95 gateways to connect to a public LoRa network (The Things Network)
 - Connected an end node to a gateway in an end-to-end configuration (LoRa without the WAN part)
 - Spent a lot of time fixing hardware problems with the gateways

### Week 4 7/05-7/11:
##### Monday:
 - 4th of July (observed)

##### Tuesday:
 - Set up Nvidia Jetson Nano and then made it work in headless mode so I can SSH into it
 - Spent a lot of time with the SX1262 and RFM95 schematics and datasheets:
     - https://semtech.my.salesforce.com/sfc/p/#E0000000JelG/a/2R000000HT76/7Nka9W5WgugoZe.xwIHJy6ebj1hW8UJ.USO_Pt2CLLo
     - https://cdn.sparkfun.com/assets/learn_tutorials/8/0/4/RFM95_96_97_98W.pdf
 - Altered SX1272 board definitions to work with the newer SX1262 board pinout

##### Wednesday:
 - Worked from mechatronics lab
 - Fixed the hardware issue: one of the gateways was missing a capacitor
 - Looked into differences between using LoRaWAN and LoRa
     - Found previous projects related to using LoRa in a point-to-point configuration
     - We can't use LoRaWAN since it requires a public network and a remote server
         - Data should travel end node -> gateway -> waggle node via serial -> data repository
 - Looked into RadioHead library, has large support for RFM95 and SX127x devices but lacks in SX126x

##### Thursday:
 - Weekly meeting with Raj. Discussed:
    - Plan going forward
    - Questions for Prof. Hester and Prof. Ghena
    - Medium Access Control within LoRa
 - attended weekly talk
 - worked on getting the most consistent connection between end node and gateway

##### Friday:
 - Successfully connected two end nodes to one gateway. point-to-multipoint connection
 - optimized/simplified exisiting transmission code
 - Sent out orders for batteries
 - Met with NAISE faculty to talk about project

### Week 5 7/12-7/18:
##### Monday:
 - playing around/exploring radio parameters: bandwidth, spreading factor, Sync Words, transmit power, antenna gain, preamble length
     - still really unsure about sync words, dramatically affect transmission
     - shrinking the bandwidth allows you to have more devices connected to one gateway
 - Found these settings to be the most effective
     - Bandwidth 250 bytes/s
     - Spreading factor: 7
     - Sync word: 0x34
     - Power 10 db
 - One of the nodes has a signficantly weaker RSSI. Bad antenna? Will investigate further

##### Tuesday:
 - started week 5 presentation for NAISE
 - The node with the weak signal seemed to have fixed itself, not really sure what happened there
 - Looking into LoRa packet structure and medium access control
 - Range test

##### Wednesday:
 - Additional Meeting with Raj to discuss progress
 - Successfully read data on the Jetson Nano from the gateway via Serial Port
 - Finish Week 5 presentation for NAISE -> Will probably also become the presentation for next week's presentation for the Waggle group

##### Thursday:
 - Weekly meeting with Raj. Discussed:
   - Plan moving forward, progress
   - Questions I have for Josiah/Branden
   - Packet structure
 - Looked into private LoRa network encryption

##### Friday:
 - Worked from mechatronics lab
 - Soldered some headers onto the end nodes so I interface with sensors
 - Interfacing with BMP10 atmosphere sensor
 - Started and finished presentation for week 5 summary

### Week 6 7/19-7/25:
##### Monday:
 - Midpoint presentations today
 - Started researching Security
 - MQTT with node-red
   - With LoRaWAN, not allowed to acknowledge every message?


##### Tuesday:
 - Meeting with Branden Ghena
 - Read FCC regulations on public radio band usage
 - High gain antennas
 - and LoRa antenna systems


##### Wednesday:
- Look into private LoRa server solutions
- ChirpStack open source LoRa -> integrated into LoRa
- Pro/con for multipoint-to-point vs server approach
- More testing


##### Thursday:
- Meeting with Raj. Discussed:
   - Coordinating with JH about LoRaWAN approach
   - How we could integrate a server onto the waggle via ChirpStack
   - Final plans for end of internship
- Week 5 presentation with NAISE people, condensed version of the presentation that I gave on monday
- Looked into multi-channel gateways

##### Friday:
- More research on ChirpStack
- Specifically looking into the energy-harvesting end-node compatibility
- Wrote outline for final whitepaper
   - 90% done, still need to familiarize myself with the ChripStack architecture before I include it officially
- Reconfigured a demo sketch for the gateway
- Attended CELS student social

### Week 7 7/26-8/1:
##### Monday:
- Realized I have been pushing to the wrong fork of the repo (facepalm), ported everything to the right one
- Looked into multi-channel emulation on sigle channel gateway; allows single channel gateways to jump rapidly through channels:
 - can get the effects of a multi-channel gateway on a single channel
 - May help bridge gaps between p2p approach and network approach



##### Tuesday:


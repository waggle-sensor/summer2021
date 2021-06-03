# Minji Daily Work-Log

## 1st Week 05/24-05/28

### Monday, 24th
-Today's Non-Technical Tasks
* Attended Orientation at 9AM (CST)
* Joined the Slack
* Computer Request for CELS
* Enrolled the required course in TMS
* Read the guidelines and instructions on Github

-Today's Technical Tasks
* Learned Docker/kubernetes cluster json
* Read Scrum Reference Card
* Read SAGE Agile Scrum Software Development Process


### Tuesday, 25th
-Today's Non-Technical Tasks
* Read the guidelines and instructions on Github
* Sign in MIRO / JIRA
  (I guess MIRO is for planning, and JIRA is for process management. I need to read the guidelines again this week, especially calculating team capacities.)

-Today's Technical Tasks
* Watched Docker tutorial videos and build up on my RPI and Mac
* Read Scrum Reference Card
* Read SAGE Agile Scrum Software Development Process

  What I learn/understand is:
  Agile: Software Developer Methodology (less document-oriented, practical code-oriented compared to Waterfall model)
         Unlike previous methodologies that have been led through planning, agile method constantly creates prototypes with constant cycles,
         modifies the needs of each time and develops a single large piece of software.
  Scrum: Implementation of Agile Methodology
         It gives priority to the features and improvements to be included in the solution.
         It is based on object-oriented technology.
         
         
### Wednesday, 26th
-Today's Non-Technical Tasks
* Double checked to complete I-9 and FNIS including all tax forms 
* Signed in https://getsmarter.io/ for weekly meeting (need to figure out how to use it)

-Today's Technical Tasks
* Watched the Node-RED demo video shared by Josh/relevant videos
* Set up RPI and remind my previous zipper robot project with RPI.
   The goal of my research was to develop an apparel system which integrates intelligent autonomous agents, human-based sensors, wireless network protocol,
   mobile application management system and a zipper robot.
   the Raspberry Pi provides several key functions to the project:
   1) It is a main control hub of running on ESP8266 Wi-Fi MCU module
   2) It serves as a broker to connect to other networks through Wi-fi microchip and user’s device.
   3) It acts as a local storage for the data packages sent and received between sockets.
   and there are several options to use MQTT
   1) Local Communication using Mosquitto (required only two terminals, and test: mosquitto_sub -h localhost -t "test/message")
   2) Java with Agent and PAHO client
   3) MQTT Dash in Android Device
* Checked my personal IoT project for growing plants
   Ran on RPI, simple Node-RED design.
   Five DHT22 sensors were used and those data was sent to the HiveMQ cloud. (https://www.hivemq.com/mqtt-cloud-broker/)

-Things to do
* Remind SQL
* Set up HiveMQ cloud active states
* Watch other Node-RED demo videos relevant SAGE project
         
************************************************************

## 2st Week 06/01-06/04

### Tuesday, 1th
-Today's Non-Technical Tasks
* Checked the schedule of TMS
* Set up Raspberry Pi and sensors for checking (RPI)
* Discussion with Sean, Wolfgang, and Joe about filtered data in the SDR (finally figured out!)
   (Feedback: In the cloud case, we only have the HTTP/JSON API. Because we can filter data using the API, we can still do something similar to subscribing to only specific kind of data.)
   So, in current progress, MQTT is not required. (might be future plan)
   
-Today's Technical Tasks
* Use HTTP request to get data from a REST endpoint on Node-RED (External REST API  - https://restcountries.eu) - Success!!
* Read the doc of REST API more. (Also check other relevant video as well)

-Things to do
* Test the HTTP request again with SDR.
  1) Read example query data from SDR using HTTP / JSON request.
  2) Start with a simple “print value” node.
  3) Add a “filter when name = sys.uptime” node and add a trigger when that is < 1800.
  

### Wednesday, 2th
-Today's Non-Technical Tasks
* done with Indiana & Illinois tax (to HR)
* Re-installed Docker on Mac (bc my RPI not enough memory)
* Completed 1 required course in TMS

-Today's Technical Tasks
* Built up Email Notification from Node-RED: https://flows.nodered.org/node/node-red-node-email
  description: It is set up on the Raspberry Pi connected temperature sensors. If temp > 30, sent the alarm via email

- Things to do
* Read Slack API: https://flows.nodered.org/node/node-red-contrib-slack and Alarm Notification on Slack...

### Thursday, 3th
-Today's Non-Technical Tasks
* Attended the ANL seminar 10-11AM (CST)
* Prepared presentation for tomorrow (Approximately 10 min)
* Completed 2 required courses in TMS
* Read the chapter 2 of "Practical Node-RED Programming"
* Scheduling Machine Learning study group @Purdue (start 7th this month)

-Today's Technical Tasks
*


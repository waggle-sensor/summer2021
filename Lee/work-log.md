# Minji Daily Work-Log

## 1st Week 05/24-05/28 (Main Goal: Set Up Environments)

### Monday, 24th
-Today's Non-Technical Tasks
* Attended ANL Orientation at 9AM (CST)
* Joined the Slack
* Computer Request for CELS
* Enrolled the required course in TMS
* Read up the guidelines and instructions on Github

-Today's Technical Tasks
* Read Scrum Reference Card
* Read SAGE Agile Scrum Software Development Process


### Tuesday, 25th
-Today's Non-Technical Tasks
* Meeting with Sean (Query into SDR)
* Followed up simple tutorials of Github
* Sign in MIRO / JIRA
  (I guess MIRO is for planning, and JIRA is for process management. I need to read the guidelines again this week, especially calculating team capacities.)

-Today's Technical Tasks
* Watched Docker tutorial videos and build up on my RPI / Mac OS
* Read Scrum Reference Card. Summary:

  Agile: Software Developer Methodology (less document-oriented, practical code-oriented compared to Waterfall model)
         Unlike previous methodologies that have been led through planning, agile method constantly creates prototypes with constant cycles,
         modifies the needs of each time and develops a single large piece of software.
  Scrum: Implementation of Agile Methodology
         It gives priority to the features and improvements to be included in the solution.
         It is based on object-oriented technology.
         
         
### Wednesday, 26th
-Today's Non-Technical Tasks
* Double checked to complete I-9 and FNIS including all relevant tax forms 
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
* Set up HiveMQ cloud active states
* Watch other Node-RED demo videos relevant SAGE project

### Wednesday, 27th
-Today's Non-Technical Tasks
* Attended first team-meeting
* Emailed to Deneen (need to check tax/paycheck process)

-Today's Technical Tasks
* Read up Sage: A distributed software-defined sensor network: https://github.com/sagecontinuum/sage
* https://github.com/sagecontinuum/sage/blob/master/architecture_overview.md


### Thursday, 28th
-Today's Non-Technical Tasks
* Meeting with Joe and Wolfgang about my node-red json format
* Attended daily meeting

### Friday, 29th
-Today's Non-Technical Tasks
* Attended daily meeting

-Today's Non-Technical Tasks
* Read up: Running Node-RED locally - https://nodered.org/docs/getting-started/local
* Simple node test with json formatting

************************************************************

## 2st Week 06/01-06/04 (Main Goal: Node-RED)
### Tuesday, 1th
-Today's Non-Technical Tasks
* Checked the schedule of TMS
* Set up Raspberry Pi and sensors for checking (RPI)
* Discussion with Sean, Wolfgang, and Joe about filtered data in the SDR (finally figured out!)
   (Feedback: In the cloud case, we only have the HTTP/JSON API. Because we can filter data using the API, we can still do something similar to subscribing to only specific kind of data). So, in current progress, MQTT is not required. (might be future plan)

-Today's Technical Tasks
* Use HTTP request to get data from a REST endpoint on Node-RED (External REST API  - https://restcountries.eu) - Success!!
* Read the doc of REST API more. (Also check other relevant video as well)
-Things to do
* Test the HTTP request again with SDR.
  1) Read up example query data from SDR using HTTP / JSON request
  2) Start with a simple “print value” node
  3) Add a “filter when name = sys.uptime” node and add a trigger when that is < 1800
 

### Wednesday, 2th
-Today's Non-Technical Tasks
* done with Indiana & Illinois tax (to HR)
* Re-installed Docker on Mac (bc RPI not enough memory)
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
* Read FBP documents, and Node-RED Summary (PPT slides will be updated)
  Node-RED is one of the FBP tools, which is Flow-Based Programming. FBP has a high-level, functional style so that the behavior of the system can be easily defined,
  and Node-RED also inheritated to those advantages. The system contains "Nodes" which look simply to be icons that you drag and drop on to the canvas and wire together.
  
  Each Node offers different functionality, which can range from a simple debug node to be able to see what's going on in your flow.
  there are 6 core nodes: inject, debug, function, change, switch, and template.

  * Inject Node literally, is to manual trigger, which is input.
  * On the other hands, debug, is output. This node can be used to display messages.
  * Function node allows JavaScript code to be run against the messages that are passed through it.
  * The change node can be used to modify a message’s properties and set context properties without having to resort to a Function node. 
  * The Switch node allows messages to be routed to different branches of a flow by evaluating a set of rules against each message.
  * The Template node can be used to generate text using a message’s properties to fill out a template.

  Note. my RPI is set up (turn on) and my laptop is used with my RPI IP address/port number - http://192.168.20.15:1880/ and http://192.168.20.15:1880/ui
  ## 1. Http Rest endpoint
  Restcountries API are used to get countries dataset from https://restcountries.eu/rest/v2.
  It includes the countries name, their languages, population, and capital and so on. But my goal this testing was that when I enter the capital, then country name pops up, which is filtered data by using its API service.
  In the http request node, when the url is attched, debug(msg.payload) and country (format) will show the output.
  
  ![image](https://user-images.githubusercontent.com/56851781/121045789-d732b580-c783-11eb-93b8-9f1c24176dad.png)

  Node-RED UI shows the result of country. (X case sensitive)
  ![image](https://user-images.githubusercontent.com/56851781/121046031-e580d180-c783-11eb-9664-38107ed29cb6.png)

  ## 2. Alarm notification (email and slack)
  When temperature value is higher than 20, In this case, temp 30 buttom, for example, and click the temp trigger, I could get HIGH Temperature Alarm. Warning sign as well as debug notification. If I click the temp 20, which is normal temperature, it sent normal temperature notification to my gmail. Of course, other email address is also possible to be used.

  ![image](https://user-images.githubusercontent.com/56851781/121046438-fe898280-c783-11eb-9489-7d856bab4e00.png)
  
  For Slack notification, Webhook is required to send my JSON payload to the URL to my NODE-RED.
  
  ![image](https://user-images.githubusercontent.com/56851781/121047210-2ed12100-c784-11eb-837b-8d67359a184d.png)
  ![image](https://user-images.githubusercontent.com/56851781/121047560-45777800-c784-11eb-89fc-7353b32f669b.png)
  
  
### Friday, 4th
-Today's Non-Technical Tasks
* Contacted with HR (Northwestern University) need to complete payment process

-Today's Technical Tasks
* After demo video prsentation, build up with feedback that I got, discussion for next steps.

-Things to do:
* Need to query in Sage Data Repo (ask some question about API to Sean)

************************************************************

## 3st Week 06/07-06/11 (Main Goal: MySQL)

### Monday, 7th
-Today's Non-Technical Tasks
* Enrolled CPT course (Purdue University)
* Entorlled OEPT course (Purdue University)
* Re-installed MySQL on Window

-Today's Technical Tasks
* Performed manipulation of the world sample database using MySQL
  SHOW DATABASES, USE (database_name, ex. world), SHOW TABLES, SHOW TABLE STATUS, DESCRIBE (or DESC) (ex. city, or country, or countrylanguage), SELECT (* (all or Name, Population) from city), WHERE, BETWEEN, IN, LIKE, Sub Query, ANY(SOME), ALL, ORDER BY, DISTINCT, LIMIT.
* All are not case-sensitive.
* It will be eventually used for Node-RED with SageDataRepo.
* Machine Learning group study - Tensor Flow with Python (easy/simple examples)


### Tuesday, 8th
-Today's Non-Technical Tasks
* SEC course 2-245PM

-Today's Technical Tasks
* Still learning MySQL
* 

### Wednesday, 9th
-Today's Non-Technical Tasks

-Today's Technical Tasks 


### Thursday, 10th
-Today's Technical Tasks
* Docker - Java Hello World
  public class HellowWorld {
    public static void main(String[] args){
      System.out.println("Hello World!");
      }
  }
vi Dockerfile
// Linux image
FROM alpine
WORKDIR /root/hello-world
COPY HelloWorld.java /root/hello-world

// Install JDK
RUN apk add openjdk8
ENV JAVA_HOME /usr/lib/jvm/java-1.8-oepnjdk
ENV PATH $PATH:$JAVA_HOME/bin

// Compile HelloWorld
RUN javac HelloWorld.java

ENTRYPOINT java HelloWorld


### Friday, 11th
-Today's Non-Technical Tasks
* Preparation presentation of goal for internship on Next Monday
* Completed all the process on Northwestern Kronos System time entry system

-Today's Technical Tasks
* read Kubernetes/Cloud documents

************************************************************

## 4st Week 06/14-06/18 (Main Goal: JavaScript)
### Monday, 14th
-Today's Non-Technical Tasks
* Presentation of goal for internship
* OEPT test

-Today's Technical Tasks
* started learning JavaScript with W3school basic tutorials in https://www.w3schools.com/js/default.asp
* JavaScript is the programming language of the Web. (In HTML, JavaScript programs are executed by the web browser.)
* HTML to define the content of web pages (backbone), CSS to specify the layout of web pages (design), and JavaScript to program the "behavior" of web pages (action).
* getElementById(): can change HTML content. e) document.getElementById("demo").innerHTML = "Hello JavaScript"
* also possible to change HTML attribute values. e) src att of an <img> tag.
* In HTML, JS code is inserted between <script> and </script> tags.
* and scripts can be placed in the <body> or in the <head>, but placing it at the bottom of the <body> recommended due to the display speed.
* External JS has several advantages: seperates HTML and code, easier to read and maintain, and can speed up page loads. (full URL or specific folder either is ok.)
  
  
### Tuesday, 15th
-Today's Technical Tasks
* Still learning JavaScript with same tutorials as yesterday's one.
* JavaScript can display data 4 different ways: innerHTML, document.write(), window.alert(), console.log()
* innerHTML
* document.write() - but will delete all existing HTML. so for testing recommended
* window.alert()   - only OK button | prompt() two button, and string type
* console.log()    - debugging purposes
* syntax
* var: { var y = 2; } // y can be used here
* let: { let y = 2; } // y can NOT be used here. Also, cannot be redeclared. but redeclaring a variable with let, in another block, is allowed.
* const: cannot be reassigned, can change the properties of a constant object, but can not reassign the object. Declaring a variable with const is similar to let when it comes to block scope.
* If put a number in quotes, the rest of the numbers will be treated as "strings", and concatenated. e) x = 2 + 3 + "0"; x = 50; (str)
* JavaScript has dynamic types, which means that the same variable can be used to hold different data types.
* note: e) var x = {firstName:"John", lastName:"Doe"}; // Object | var cars = ["Saab", "Volvo", "BMW"]; //array (similart to list in Python I guess)
* However, the typeof operator returns "object" for arrays because in JavaScript arrays are objects.

  
### Wednesday, 16th
-Today's Technical Tasks
* Still learning JavaScript with same tutorials as yesterday's one.
* functions, objects, and events
* JavaScript objects are containers for named values called properties or methods.
* Objects are variables too. But objects can contain many values.
* can access object properties in two ways: objectName.propertyName or objectName["propertyName"]
* "this" keyword

  
### Thursday, 17th
-Today's Non-Technical Tasks
* short meeting with Joe

-Today's Technical Tasks
* prepared for tmr demo

  
### Friday, 18th
-Today's Non-Technical Tasks
* SAGE sprint demo & retrospective (DHT real time data handling, and query from SDR on Node-RED presentation)
* Linked-IN updated, Northwestern Kronos time entry system updated

-Today's Technical Tasks
* Complete basic JavaScript W3school tutorials.
* Presentation Contents 1: DHT sensor read (real time data) from RPI on Node-RED
  
  ![KakaoTalk_20210621_102635621_011](https://user-images.githubusercontent.com/56851781/122781041-6c9e7100-d27d-11eb-910f-3e7a8ac8cf53.jpg) ![KakaoTalk_20210621_102635621](https://user-images.githubusercontent.com/56851781/122781078-76c06f80-d27d-11eb-9bbe-879e6e1be648.jpg)
  ![image](https://user-images.githubusercontent.com/56851781/122780732-1c271380-d27d-11eb-870e-a97903cc6037.png)
  
  ![image](https://user-images.githubusercontent.com/56851781/122779792-3a404400-d27c-11eb-88b5-8427b24df7ea.png)
  
* if you want to get real time data every 1 second, change like this:
  ![image](https://user-images.githubusercontent.com/56851781/122779945-5c39c680-d27c-11eb-8a28-860ff4fc4b6d.png)
 
* You can see on the debug node for example, {"_msgid":"63bb3921.ad62e8","topic":"rpi-dht22","payload":"28.00","humidity":"81.00","isValid":true,"errors":0,"location":"DHT","sensorid":"dht11"}, which means that need to change "payload" to "msg.payload = msg.payload and return msg;" in the temp function nodes as shown like this:
![image](https://user-images.githubusercontent.com/56851781/122780611-fef24500-d27c-11eb-8cc3-712e4d2b1e75.png)
  
* can check the output on terminal as well as the debug node + UI (e. hostIPAddress with ui http://192.168.1.53:1880/ui)
![image](https://user-images.githubusercontent.com/56851781/122780019-6f4c9680-d27c-11eb-99d9-b45d86bb5adb.png)
![image](https://user-images.githubusercontent.com/56851781/122780452-d9fdd200-d27c-11eb-8664-b6f74379acb1.png)

* Presentation Contents 2: Query SDR on Node-RED
* Trouble: Accessing and Querying SDR no problem on the terminal like this:![image](https://user-images.githubusercontent.com/56851781/122793311-0c153100-d289-11eb-814f-c3d49d6c64c4.png) but couldn't get access to do that on Node-RED. The issue was that everything sent to ignore, so http request ignores everything from inject,
which is EOF, end of file, that is specifially what they gave me back. which means, this works.
  
  ![image](https://user-images.githubusercontent.com/56851781/122794063-d9b80380-d289-11eb-8dc9-6800135f6792.png)
* payload should be changed from ignore(default) to "Sent as the body of the requst. Also changed JSON formatting in inject node like this:
  ![image](https://user-images.githubusercontent.com/56851781/122794204-010ed080-d28a-11eb-9f8b-874d16a51b00.png)

* result: ![image](https://user-images.githubusercontent.com/56851781/122794583-695db200-d28a-11eb-8b99-fcf5eab7e22e.png)

-Things to do: Next week will focus on using Docker
  
************************************************************

## 5st Week 06/21-06/25 (Main Goal: Docker / Kubernetes)
### Monday, 21th
-Today's Non-Technical Tasks
* Attended presentation of goal for internship
-Today's Technical Tasks
* Learning docker from https://www.44bits.io/ko/post/why-should-i-use-docker-container
* Basic concept: Docker is a set of platform as a service (PaaS) products that use OS-level virtualization to deliver software in packages called containers.
  Containers are isolated from one another and bundle their own software, libraries and configuration files; they can communicate with each other through well-defined channels. Because all of the containers share the services of a single operating system kernel, they use fewer resources than virtual machines.
* Docker components: software, objects, and registries.
* WHY used? Containers are technologies that run applications regardless of their environment. (do not need to go through the complex installation process that exists for each operating system.)
* tested with simple tutorial: https://www.youtube.com/watch?v=hWPv9LMlme8&t=587s
-Things to do: join to Kubernetes with Docker

  
### Tuesday, 22th
-Today's Non-Technical Tasks
* Signed up remote work form v1 and sent it back to Deneen
* Completed all require/elective courses in TMS (need to sign from Raj)
* Attended sprint planning meeting

-Today's Technical Tasks
* Read up Node-RED instances examples exisiting industrial world
* If have multiple instances of node red on same machine with different port numbers, different flows: For the same user based on the role defined - flows and palette controls will be displayed: https://nodered.org/docs/getting-started/local
  
  
### Wednesday, 23th
-Today's Non-Technical Tasks
* Scheduled for July 13th: Reply to Mary summer get-together with students and mentors
* Attended mid-break social meeting

-Today's Technical Tasks
* Clarified node-red instance per user. First step: if have multiple instances of node red on same machine with different port numbers, different flows
* https://nodered.org/docs/getting-started/local
* https://discourse.nodered.org/t/how-can-we-run-multiple-node-red-applications-in-the-same-machine-system/40805/16

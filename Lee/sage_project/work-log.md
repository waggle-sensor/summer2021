# Minji Daily Work-Log

## 1st Week 05/24-05/28 (Main Goal: Set Up Environments)

### Monday, 24th
-Today's Non-Technical Tasks
* Attended first ANL orientation
* Joined Slack
* Set up computer request for CELS
* Enrolled the required course in TMS

-Today's Technical Tasks
* Read up the SAGE project overview: https://github.com/sagecontinuum/sage
* Read Scrum Reference Card share by Joe on Google drive
* Read SAGE Agile Scrum Software Development Process


### Tuesday, 25th
-Today's Non-Technical Tasks
* Meeting with Sean (Query into SDR)
* Sign in MIRO and JIRA
  (I guess MIRO is for planning, and JIRA is for process management. I need to read the guidelines again this week, especially calculating team capacities.)
* Followed up simple tutorials of Github: https://www.youtube.com/watch?v=tC8Xj_Bf8Fw&t=618s

-Today's Technical Tasks
* Read up Docker tutorials and installed on my RPI
* Read Scrum Reference Card. Summary:
  * Agile: Software Developer Methodology (less document-oriented, practical code-oriented compared to Waterfall model). Unlike previous methodologies that have been led through planning, agile method constantly creates prototypes with constant cycles, modifies the needs of each time and develops a single large piece of software.
  * Scrum: Implementation of Agile Methodology. It gives priority to the features and improvements to be included in the solution. It is based on object-oriented technology.
         
         
### Wednesday, 26th
-Today's Non-Technical Tasks
* Double checked to complete I-9 and FNIS including all relevant tax forms 
* Signed in https://getsmarter.io/ for weekly meeting (need to figure out how to use it)
* First meeting with Joe, and confirm my tasks this week

-Today's Technical Tasks
* Watched the Node-RED demo video shared by Josh/relevant videos and discussed about it with Wolfgang (next week goal maybe)
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
   Ran on RPI, simple Node-RED design with GUI.
   Five DHT22 sensors were used and those data was sent to the HiveMQ cloud. (https://www.hivemq.com/mqtt-cloud-broker/)

-Things to do
* Set up HiveMQ cloud active states
* Watch other Node-RED demo videos relevant SAGE project


### Wednesday, 27th
-Today's Non-Technical Tasks
* Attended first team meeting
* Emailed to Deneen (need to check tax/paycheck process)
* Attended ANL social meeting at lunch time (virtual)

-Today's Technical Tasks
* Read up Sage project overview: A distributed software-defined sensor network: https://github.com/sagecontinuum/sage
* https://github.com/sagecontinuum/sage/blob/master/architecture_overview.md


### Thursday, 28th
-Today's Non-Technical Tasks
* Meeting with Joe and Wolfgang about node-red endpoint
* Attended daily meeting

-Today's Technical Tasks
* Read up/compared MQTT & HTTP request on node-red (should ask Joe about using MQTT protocol)

### Friday, 29th
-Today's Non-Technical Tasks
* Attended daily meeting
* Short meeting with Josh (asking node-red endpoint at the cloud service)
* Data structure review

-Today's Technical Tasks
* Read up Running Node-RED locally - https://nodered.org/docs/getting-started/local
* Simple node test with json format

************************************************************

## 2st Week 06/01-06/04 (Main Goal: Node-RED)
### Tuesday, 1th
-Today's Non-Technical Tasks
* Completed one required course in TMS
* Set up personal Raspberry Pi and DTH sensors
* Discussion with Sean, Wolfgang, and Joe about filtered data in the SDR (finally figured out!)
  (Feedback: In the cloud case, we only have the HTTP/JSON API. Because we can filter data using the API, we can still do something similar to subscribing to only specific kind of data). So, in current progress, MQTT is not required. (might be future plan)

-Today's Technical Tasks
* Use HTTP request to get data from a REST endpoint on Node-RED (External REST API example: https://restcountries.eu) - Success!!
* Read more the doc of REST API. (Also check other relevant video as well)

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
  ##### 1. Http Rest endpoint
  Restcountries API are used to get countries dataset from https://restcountries.eu/rest/v2.
  It includes the countries name, their languages, population, and capital and so on. But my goal this testing was that when I enter the capital, then country name pops up, which is filtered data by using its API service.
  In the http request node, when the url is attched, debug(msg.payload) and country (format) will show the output.
  
  ![image](https://user-images.githubusercontent.com/56851781/121045789-d732b580-c783-11eb-93b8-9f1c24176dad.png)

  Node-RED UI shows the result of country. (X case sensitive)
  ![image](https://user-images.githubusercontent.com/56851781/121046031-e580d180-c783-11eb-9664-38107ed29cb6.png)

  ##### 2. Alarm notification (email and slack)
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

### Wednesday, 9th
-Today's Non-Technical Tasks
* Updated Linked-in profiles/experiences

-Today's Technical Tasks 
* Still learning MySQL

### Thursday, 10th
-Today's Non-Technical Tasks
* Attended 2021 CELS Student Lecture

-Today's Technical Tasks: Docker
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

```
// Install JDK
RUN apk add openjdk8
ENV JAVA_HOME /usr/lib/jvm/java-1.8-oepnjdk
ENV PATH $PATH:$JAVA_HOME/bin
```

`// Compile HelloWorld`
`RUN javac HelloWorld.java`

`ENTRYPOINT java HelloWorld`


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
* Short meeting with Joe
* Attended 2021 CELS Student Lecture

-Today's Technical Tasks
* Prepared for tmr demo

  
### Friday, 18th
-Today's Non-Technical Tasks
* SAGE sprint demo & retrospective (DHT real time data handling, and query from SDR on Node-RED presentation)
* Linked-IN updated, Northwestern Kronos time entry system updated

-Today's Technical Tasks
* Complete basic JavaScript W3school tutorials.
* Presentation Contents 1: DHT sensor read (real time data) from RPI on Node-RED
  
  ![image](https://user-images.githubusercontent.com/56851781/122779792-3a404400-d27c-11eb-88b5-8427b24df7ea.png)

* Presentation Contents 2: Query SDR on Node-RED
* Trouble: Accessing and Querying SDR no problem on the terminal like this:

![image](https://user-images.githubusercontent.com/56851781/122793311-0c153100-d289-11eb-814f-c3d49d6c64c4.png) but couldn't get access to do that on Node-RED. The issue was that everything sent to ignore, so http request ignores everything from inject, which is EOF, end of file, that is specifially what they gave me back. which means, this works.
  
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
* https://developer.ibm.com/ko/technologies/iot/
* https://www.python2.net/questions-1144056.htm
  
  
### Thursday, 24th
-Today's Non-Technical Tasks
* Attended 2021 CELS Student Lecture
* Attended daily sage scrum meeting
* Attended Sean's tutorial on writing plugins (code) for the Waggle nodes
* short meeting with Neal (asking some questions about JavaScript)
  
-Today's Technical Tasks
* Tested on SAGE endpoint-nodeRED instances hookup
  
  
### Friday, 25th
-Today's Non-Technical Tasks
* Updated Linked-in profiles/experiences
* Attended daily sage scrum meeting
* Created IBM cloud (cloudant service) to test i/o data from Node-RED
  
-Today's Technical Tasks
* Research how to set NSSM to run two separate instances at boot in windows 10
  
************************************************************
  
## 6st Week 06/28-07/02 (Main Goal: Node-RED instance testing)
### Monday, 28th
-Today's Non-Technical Tasks
* Attended daily sage scrum meeting
* Talked to my advisor for PhD program
  
-Today's Technical Tasks
* testing each node-red instance in different environments (import/export with json format)

-Things to do
* Found some errors when deploying instance, server replies permission denied and files not access (debugging required tomorrow)
  
![image](https://user-images.githubusercontent.com/56851781/123885555-acb7c080-d91b-11eb-8ed8-51664e44e492.png)

  
### Tuesday, 29th
-Today's Non-Technical Tasks
* Attended daily sage scrum meeting

-Today's Technical Tasks
* Finally figured out the files not access error (each node needs to be instanced "individually")
* Still testing each node (now currently working with only temp topic)

  
### Wednesday, 30th (BirthDay hehe)
-Today's Non-Technical Tasks
* Attended EDU Weekly Seminar Series
* Short meeting with PhD program advisor

-Today's Technical Tasks
* compared docker node-red instances and kubernetes node-red instances (or find third solutions)
* installed: ![image](https://user-images.githubusercontent.com/56851781/123992689-d6afc800-d999-11eb-8382-c17c2d6ba997.png)

![image](https://user-images.githubusercontent.com/56851781/124016433-a6752300-d9b3-11eb-88c7-82c0e05dac41.png)
  
  
### Thursday, 1th
-Today's Non-Technical Tasks
* Attended daily sage scrum meeting

  
### Friday, 2th
-Today's Non-Technical Tasks
* Attended daily sage scrum demo
  
************************************************************
  
### Tuesday, 6th
-Today's Technical Tasks
* running under Docker: https://nodered.org/docs/getting-started/docker
* repository on Docker Hub: https://hub.docker.com/r/nodered/node-red/
* docker images: https://github.com/node-red/node-red-docker/tree/master/docker-custom
* overview: https://github.com/node-red/node-red-docker/blob/master/README.md

  
### Wednesday, 7th
-Today's Non-Technical Tasks
* Meeting with Raj

  
### Thursday, 8th
-Today's Technical Tasks
* Learned how to manage docker container on Kubernetes
  
  
### Friday, 9th
-Today's Technical Tasks
* The source from https://nodered.org/docs/getting-started/docker
* Managing User Data: Once you have Node-RED running with Docker, we need to ensure any added nodes or flows are not lost if the container is destroyed. This user data can be persisted by mounting a data directory to a volume outside the container. This can either be done using a bind mount or a named data volume. Node-RED uses the /data directory inside the container to store user configuration data. (Don't know what it is)
  
************************************************************
  
### Monday, 12th
-Today's Non-Technical Tasks
* Attended mid-presentation (not sure why my laptop microphone/share the screen not working)
  
-Today's Non-Technical Tasks
* Meeting with abayomi (Jenkins: open source automation server. It helps automate the parts of software development related to building, testing, and deploying, facilitating continuous integration and continuous delivery. It is a server-based system that runs in servlet containers such as Apache Tomcat)
* Multiple instances, multiple users -> Jenkins???
* CI (Continuous Integration): The practice of merging all developers' working copies to a shared mainline several times a day.
* CD (Continuous Development): Software development process that encompasses multiple DevOps processes, including continuous integration, continuous testing, continuous delivery, and continuous deployment.
* Jenkins: CI/CD service

### Tuesday, 13th
- Enjoyed Get-Together Event!!!!!


### Wednesday, 14th
-Today's Non-Technical Tasks
* Attended daily scrum meeting
* Start writing the science articles (half done)
* Prepare the research paper with IEEE format
* Meeting with Wolfgang
* Meeting with Milos about multiple port number for node-red instances
  
-Today's Technical Tasks
  ![image](https://user-images.githubusercontent.com/56851781/125650483-cb12b4b0-5fe8-4d0e-bc06-91d96f51383c.png)
  
* It seemed like one of those ports already had a connection established with the service others were just listening. Listen port serves as an endpoint for communcation. They are listening but that does not necessarily mean they are working.
* Docker hub also shows all port numbers (1880-1882) are used for node-red, but connection errors: need to do debug
  
  
### Thursday, 15th
-Today's Non-Technical Tasks
* Attended daily scrum meeting
* Attended CELS Technical Women meetup
  
-Today's Technical Tasks
* It seems ok to run it with the specific port number (8880)
  ![image](https://user-images.githubusercontent.com/56851781/125834527-51dd4f19-2c77-4f39-87a9-3d8466819879.png)

* So, just kept going the test
  ![image](https://user-images.githubusercontent.com/56851781/125847340-c033857a-eb12-4688-8e1e-aade8a870ec8.png)

  <img width="639" alt="1" src="https://user-images.githubusercontent.com/56851781/125847379-71400033-3c92-4bc5-b04a-8e48ad4e82a7.PNG">
  
  <img width="602" alt="2" src="https://user-images.githubusercontent.com/56851781/125847382-287bb2fa-56e8-4924-ba24-4d33475fd710.PNG">

### Friday, 16th
-Today's Non-Technical Tasks
* submitted the additional document to NW

-Today's Technical Tasks
* Continued work on creating multiple node-red on dockers with different portnumbers
  
  
************************************************************
### Monday, 19th
-Today's Non-Technical Tasks
* Presented mid goal for internship
* Updated the summer internship google drive
  
-Today's Technical Tasks
* discussion about docker with yomi and luke
* Figured out using docker port numbers for multiple instances... thanks yomi and luke...!!!
  
![image](https://user-images.githubusercontent.com/56851781/126231531-de1941a1-8f9e-4ed6-9693-ccaafa2eed70.png)

![image](https://user-images.githubusercontent.com/56851781/126231565-0864bc43-1e94-45db-a2a1-f032ac748671.png)
  
![image](https://user-images.githubusercontent.com/56851781/126231623-5c4d1a82-6381-4e87-bd4f-469e7d87f064.png)
* Even if those instances are created with different port numbers, these are already used, so it is just Listening, (but not what I want)
  
* port 1880 
![image](https://user-images.githubusercontent.com/56851781/126345056-7f4630bb-714a-4efe-8e15-ff04b8c7f15b.png)
  
* port 1881 
![image](https://user-images.githubusercontent.com/56851781/126345201-faa24ba0-c168-4905-8256-372cbf4366e7.png)
  
  
### Tuesday, 20th
-Today's Non-Technical Tasks
* Attended Chris thesis presentation (military UAV)
* Meeting with Joe and updated my progress with him (really cool)

-Today's Technical Tasks
* Successfully managed Docker hub and node-red instances
* Read documents about docker containers / deployment for each user

  
### Wednesday, 21th
-Today's Non-Technical Tasks
* Meeting with teams UAV Ground Scanning System: Human Detectionwith Deep Learning: Need to figure out local running GPU at KSQ building
* Attended EDU Weekly Seminar Series: How to Establish Your Personal Brand
* Meeting with Brandon and Larry (Docker and VM)
* Super nice meeting with Sean to talk about Docker port numbers (Thank you so much)
* Still working on write papers with Korean students
  
-Today's Technical Tasks
* https://purdue-primo-prod.hosted.exlibrisgroup.com/primo-explore/fulldisplay?docid=TN_cdi_ieee_primary_9239699&context=PC&vid=PURDUE&lang=en_US&search_scope=everything&adaptor=primo_central_multiple_fe&tab=default_tab&query=any,contains,nodered&facet=rtype,exclude,reviews,lk&facet=rtype,exclude,reference_entrys,lk

  
### Thursday, 22th
-Today's Non-Technical Tasks
* Attended scrum
* Meeting with Sean & Wolfgang to set up Docker-compose.yml
* Demo/Presentation for writing paper (Node-RED and IoT Cloud service) with meeting with Korean students
  
-Today's Technical Tasks
* Attended scrum
* Meeting with Joe (future plans after internship and several things needed to be finished before internship)

  
### Friday, 23th
-Today's Non-Technical Tasks
* Attended scrum
* Meeting with Branden for Docker Pull/Push discussion
  
-Today's Technical Tasks
* Node-RED GUI development

-Things to do
* Need to change home address on Kronos System (personal info), cause moving out soon!!!

  
************************************************************
### Monday, 26th
-Today's Non-Technical Tasks
* Seminar for Korean Students (930AM in EST)
  
-Today's Technical Tasks
* Finally solved it out (IMAP, smtp.gmail.com)
* Relevant resource: https://getemailservices.com/gmail-imap-settings/
* Added alarm notification on Node-RED UI page
  
![image](https://user-images.githubusercontent.com/56851781/127035659-b8083fda-c683-468e-bc97-64f45abe5b19.png)
  
* Added multiple channels/Web-hook service from Node-RED to Slack 
  
![image](https://user-images.githubusercontent.com/56851781/127035795-29f89bc8-a4a4-426d-858d-4ad0daea4334.png)

-Things to do:
* Update ResearchGate
* More research for this: ![image](https://user-images.githubusercontent.com/56851781/127054102-9b9b8ba1-6fee-450a-ad7b-3e70788f4463.png)
  
  
### Tuesday, 27th
-Today's Non-Technical Tasks
* Meeting with Joe (split chunk of data. Related to links: https://discourse.nodered.org/t/split-the-string-into-separate-values/2818/5
* But this has some problems: Split the string into separate values. I wanna get an object, not an indivitual split data....
* Meeting with Neal and asked some questions about JavaScript:

![image](https://user-images.githubusercontent.com/56851781/127383744-9edf5e75-38b6-4e35-b4a4-a12b320899c4.png)

- Today's Techinical Tasks
- Successfully split String to Obj
* Edited one:
![image](https://user-images.githubusercontent.com/56851781/127385028-7e14c9e8-d7e7-4c30-8e3b-79179fda5cd0.png)

* Also slack alarm notification with multiple channels
* I also got feedback from Neal about new code. Need to discuss about it with him tomorrow
* funcX set up on MacOS

  
### Wednesday, 28th
-Today's Non-Technical Tasks
* Meeting with teams UAV Ground Scanning System: Human Detectionwith Deep Learning
* Attended scrum
* Had a meeting with Joe and discuss about the SDR query for next steps (with funcx)
* Attended final intern presentation
  
-Today's Technical Tasks
* Testing Query from sdr obj and string files
* funcX testing with Python modules
* Got some feedback from Neal and changed codes
 1) `Object.keys(temp).length` could (and really should) just be `temp.length`.
 2) It is best practice to use either `var`, `let`, or `const` for variable declarations.
 3) 6 new lines of code could just be a `.filter()` that is tacked on directly after the `.map()`.
  
  
### Thursday, 29th
-Today's Non-Technical Tasks
* Attended scrum
* Still writing paper with Korean/Purdue students
* Attended weekly demo for IITP meeting

-Today's Technical Tasks
* Change the query measurement (Thanks Neal!):
```
  curl -H 'Content-Type: application/json' https://sdr.sagecontinuum.org/api/v1/query -d '
{
    "start": "-1h",
    "filter": {
        "plugin": "plugin-metsense:0.*",
        "name": "iio.*"
    }
}
```
* The reason above: it seems the metsense version number, name, and the measurement names have changed since those docs written.

 
### Friday, 30th
-Today's Non-Technical Tasks
* Attended Demo, Presented Demo
* Feedback from Yongho and Neal: What is the best way for users to use Node-RED? Assume that they don't know about Node-RED or JavaScript at all.
* It should be VERY friendly user interface or include README file for Node-RED (detail description).
  
-Things to do:
* This weekend the paper/science articles must be written.
* Node-RED code cleaning, and upload Waggle github.  
  
************************************************************
### Monday, 2th
-Today's Non-Technical Tasks
* Attended scrum
* Read up MDML: https://labs.globus.org/pubs/Elias_MDML_2020.pdf to work on writing paper
  
-Today's Technical Tasks
* Fininshed cleaning Node-RED code (Beginner part) and uploading at github

-Things to do:
* Add all references to paper

  
### Tuesday, 3th
-Today's Non-Technical Tasks
* solved out kronos timecard issue
* still uploading Node-RED code on Waggle Summer 2021 Github. Available at [Node-RED_Sage.md](https://github.com/waggle-sensor/summer2021/blob/main/Lee/nodered_examples/Node-RED_SAGE.md)
  
-Today's Technical Tasks
* still working on SDR querying UI issue
  
  ![image](https://user-images.githubusercontent.com/56851781/128386145-3fec9fa6-df8d-400b-99de-9e1bd75f21ff.png)

  
### Wednesday, 4th
-Today's Non-Technical Tasks
* Meeting with teams UAV Ground Scanning System: Human Detectionwith Deep Learning: Need to figure out local running GPU at KSQ building
* Meeting with teams UAV ground detection and tracking systems: Tree detection and tracking change species and amount of tree
  
-Today's Technical Tasks
* change JavaScript code: .filter() instaed of using loops (huge!!!!!)
* `FILTER` Average 0.019943333354603965
* `LOOP` Average 0.02598666658741422 (Slowest)
* Reference: http://www.andygup.net/fastest-way-to-find-an-item-in-a-javascript-array/
* code ref: https://jsfiddle.net/agup/Y8SBL/10/
* decription ref: https://developer.mozilla.org/en-US/docs/Web/API/Performance


### Thursday, 5th
-Today's Non-Technical Tasks
* 
  
-Today's Technical Tasks
* 
  

### Friday, 6th
-Today's Non-Technical Tasks
* 
  
-Today's Technical Tasks
* 
  
  
************************************************************
### Monday, 2th
-Today's Non-Technical Tasks
* checked plagiarism for my paper and edited v2
* Read relevant documents and paper about Node-RED streaming data: Real-time Querying and Monitoring of scientific experiments via IoT Sensors
* Fundamental ML knowledge also required
  

### Tuesday, 10th
-Today's Non-Technical Tasks
* Meeting with Joe about my paper (his feedback: need more clear “User Interface” section. Also small typo, and need more references such as FuncX, and SDR. Overall EXCELLENT job!)
* Meeting with my advisor to publish this paper

-Today's Technical Tasks
* Edited some function node JavaScript code: map(), and filter()
* Modified Node-RED Dashboard design
  
 
### Wednesday, 11th
-Today's Non-Technical Tasks
* Presented the final prsentation: Goal for internship
* Finished up writing science article and it was uploaded


### Thursday, 12th
-Today's Non-Technical Tasks
* Submitted the paper on Google drive
* All checked final things to do
* Meeting with Pete... cause I would like to publish my paper after doing more research next semester for my PhD thesis topic
* Attended the scrum meeting to say good bye and thanks for everyone... my team they all were so warm and nice. (cried little bit...)
  
-Today's Technical Tasks
* Still editing my Node-RED dashboard flows. (need to do more research Node-RED limitation)

-Things to do: ANL survey

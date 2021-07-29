# Kenan's work log

## Week 1:  5/17 to 5/21
---------
### Monday, 5/17 (8 Hours worked)

**Today's non-technical work:** 
* Had Orientation meeting
* Filled out some HR forms
* Went through the HR presentations
* Created folder in summer2021 repo, added keys to Bepop
* Created JLSE Account

**Questions for later**: 
-    What does a system fault look like? Does it entail the entire system failing, or just a set of services not working? 
-    What is the high-level process for updating nodes remotely?


**Main object of the day**: Research into important filesystem packages.

[Btrfs](https://wiki.archlinux.org/title/btrfs): 
-    A copy-on-write filesystem that specializes in fault tolerance. 
        - The copy-on-write functionality can be toggled for individual files, but not for individual subvolumes. Every mounted subvolume must have the same copy-on-write settings. 
-   An interesting fault tolerance feature, Btrfs includes 'snapshots',  which utilizes the copy-on-write mechanic. By definition from the [wiki](https://btrfs.wiki.kernel.org/index.php/SysadminGuide#Snapshots), a snapshot is *'simply a subvolume that shares its data (and metadata) with some other subvolume'*. 
    -   For my own understanding, I'm pretty sure this works because a snapshot is a *copy* of some file system. Because copy-on-write doesn't really overwrite/delete files, and rather makes a copy of a new file with changes, you can roll back entire trees by just uncaching the version without changes. There's a basic method of doing this in the wiki link above. 

[openSUSE:Snapper](https://en.opensuse.org/openSUSE:Snapper_Tutorial):
-    A tool to manage snapshots in conjunction with Btrfs. Any subvolume that you want to use Snapper with must be specified. Provides several ways for creating, managing, and configuring snapshots. The most simple way I can see is by downloading some OS update, creating a snapshot of the current OS, installing the update, and rolling back to the snapshot when needed. Snapper works hand-in-hand with zypper and YaST by creating snapshots whenever they are used, and can easily undo these changes. 

[OSTree](https://github.com/ostreedev/ostree): 

-    A system that allows the committing, deploying and managing of Bootable OS trees. It is important to note that OSTree does not maintain any insight into the stored OS's themselves- it mostly acts as a 'package manager' for Bootable Operating Systems. 
        - The example given by the docs mentions the case of some dev needing insight into which version of OpenSSL is installed on some OS, and that the person responsible for committing the OS should also support that functionality. 
-    Has some functionality with Btrfs. Baremetal implementations of OSTree are the most useful.




-----------------


### Tuesday, 5/18 (7 Hours worked)

**Some more info on fault tolerance**

*Running in lockstep:* Performing the same set of actions/load twice in parallel. If one fails, there is no halting and the other load can fill in. This is accomplished by just copying everything required to run the load- even virtual components like memory or CPU cores. 

*Pre-emptive monitoring:* Monitors the state of the CPU and memory and compares it against some arbitary set of criteria(usually somewhat defined by the user). 

**Today's non-technical work:**
* Met with Joe and Wolfgang to discuss general fault tolerance practices(see notes from monday). 
* Set up ANL computer with proper SSH keys, can now access lcrc and github 
* Had first scrum
* Looked over SAGE software provisioning doc
* Ran [docker hello-world](https://hub.docker.com/_/hello-world) application
* Went to all hands meeting, listened to Raj's great telecommuting lecture.
* Tried running [this](https://medium.com/oceanize-geeks/basic-docker-installation-with-simple-project-using-docker-and-pushed-to-docker-hub-d319a9a7bc5b) simple docker project, and failed. Will try again tomorrow morning. 

-------------
### Wednesday, 5/19(8 Hours worked)

**Today's non-technical work:**
* Missed Scrum (note: it starts at 10:30 on wednesdays)
* Meeting with Wolfgang and Joe about in-depth SAGE software implementation
* Read more about Docker/containers


**Today's technical work:**
* Installed docker on ANL rig, did OSTree 'helloworld' on stock ubuntu image
* Created [ostree-test](./ostree_test/README.md), which simulates the most basic faults. I'm not sure if it even applies to SAGE faulting, but it was good practice for `ostree`.

---------
### Thursday, 5/20 (6 Hours worked)

**Today's non-technical work**
* No scrum, tuned in to the research meeting brielfly
* Read the following papers: 
    - G. Muller, M. Banatre, N. Peyrouze and B. Rochat, "Lessons from FTM: an experiment in design and implementation of a low-cost fault tolerant system," in IEEE Transactions on Reliability, vol. 45, no. 2, pp. 332-340, June 1996, doi: 10.1109/24.510822.
    - J. Grover and R. M. Garimella, "Reliable and Fault-Tolerant IoT-Edge Architecture," 2018 IEEE SENSORS, 2018, pp. 1-4, doi: 10.1109/ICSENS.2018.8589624.
    - I. Lee, D. Tang, R. K. Iyer and M. -. Hsueh, "Measurement-based evaluation of operating system fault tolerance," in IEEE Transactions on Reliability, vol. 42, no. 2, pp. 238-249, June 1993, doi: 10.1109/24.229493.

    I did not gain a ton of insight from these papers, as the widespread definition of fault tolerance for IoT is for the entire network, and not the OS specifically. 

**Today's takeaways and notes, transcribed**: 

Big idea: have different 'levels' of faults, kind of like DEFCON levels.
* All faults are inherently critical. However, some faults are far more complicated to recover from than others. This means that some faults are more critical than others. For example, a fault preventing booting > a fault from an AI/ML package

Following this principle, the most efficient process of work is to focus on recovery from the widest and most critical faults, and work our way down from there. 

Currently known/concieved faults are: 
* Can't boot from emmc 
* Power being pulled during update
* Software fault
    - To generalize 'Software fault' means any fault that stops the main functions of the Wild SAGE nodes. 
    - Side note- when rolling back faulting software, all processes currently using files included in the rollback need to be identified, stopped, and restarted, as not doing so may lead to undefined behavior. 

Misc. but still relevant notes: In the cited paper above [*Reliable and Fault-Tolerant IoT-Edge Architecture*](https://www.researchgate.net/publication/330487694_Reliable_and_Fault-Tolerant_IoT-Edge_Architecture), there is mention of using some kind of neural network to detect faults preemptively. While their implementation was referencing a 4-layer cloud, fog, mist, & dew computing system, the idea piqued my interest, as we have plenty of AI talent. 

A common technique of fault tolerance seems to state monitoring in tandem with dual booting. State monitoring seems like a no-brainer, but it might be worth looking into to maintain a set of encoded states that might make monitoring easier. 

-----------
### Friday, 5/21 (7 Hours Worked)

**Today's non-technical work:**
* Attended scrum
* Had meeting with Joe and gained insight into SAGE software implementation. Further specificed what my main task is this summer. 
* Attended Demo meeting
* Read the following papers: 
    - Tracy A. Neilson, James A. Donaldson,
Curiosity's Fault Tolerant Wakeup and Shutdown Design,
Procedia Computer Science,
Volume 28,
2014,
Pages 441-448,
ISSN 1877-0509,
https://doi.org/10.1016/j.procs.2014.03.054.

    - Javed, A., Robert, J., Heljanko, K. et al. IoTEF: A Federated Edge-Cloud Architecture for Fault-Tolerant IoT Applications. J Grid Computing 18, 57–80 (2020). https://doi.org/10.1007/s10723-019-09498-8
    - Sander van der Burg, Eelco Dolstra, and Merijn de Jonge. 2008. Atomic upgrading of distributed systems. In Proceedings of the 1st International Workshop on Hot Topics in Software Upgrades (HotSWUp '08). Association for Computing Machinery, New York, NY, USA, Article 8, 1–5. DOI:https://doi.org/10.1145/1490283.1490294
    - Rajat Verma, Anton Ajay Mendez, Stan Park, Sandya Mannarswamy, Terence Kelly, and Charles B. Morrey. 2015. Failure-atomic updates of application data in a linux file system. In Proceedings of the 13th USENIX Conference on File and Storage Technologies (FAST'15). USENIX Association, USA, 203–211.
    - (And several other non-academic articles I didn't feel necessary to include)

Today I tried to broaden my view of other fault tolerant systems, which is why one of the listed papers is about the mars rover. Conversely, I met with Joe to get a concise definition of the rollbacks, upgrades, and tolerance required for the Wild SAGE nodes. It was a ton of information, and I'll need to rewatch the meeting on monday. 

My first week was a little bit slower than I thought it would be. It has been strange to dial it back and just read about stuff, especially because in the past I've never cared this much about theory or doing articulate research before diving in. Nonetheless, I had a good week. I'm happy to be here on the SAGE grant. I think I'll grow a lot this summer, especially in terms of stress management, patience, and OS systems knowledge. 

---------

## Week 2: 5/24 to 5/28
------------
### Monday, 5/24 (7 Hours worked)

**Today's non-technical work:**
* Attended Scrum
* Finished TMS training modules
* Met with Wolfgang and talked about deliverables
* Wrote outline for fault-tolerant technology overview, will complete tomorrow

**Today's technical work:**
* Tried to use Btrfs, need a partition or physical media


**Links to hold onto:**
* [F2FS](https://f2fs.wiki.kernel.org/perf)

**For tomorrow**:
* Write overview of FT technologies while paying attention to academic style. Remember to include AB booting.
* Try to make partition in a docker container and use Btrfs


------------
### Tuesday, 5/25

**Today's non-technical work:**
* Attended Scrum
* Got acquainted with Overleaf

**Today's technical work:**
* Learned OverlayFS basic usage
* Wrote very primitive 'commit' system with OverlayFS. I'll commit it tomorrow. 
    - OverlayFS does not support more than two layers of overlays. I haven't tried the nested overlay functionality because it makes the 'version control' aspect of the application more complicated. I'll try it tomorrow before scrum.

Today, I did not write any kind of paper like I said I would. But, I got lost in using OverlayFS and I had a lot of fun trying to make sense of it. I learned a lot today, and it was refreshing to have my brain feel like it's on fire(in a good way).  I'll talk to Joe tomorrow about my findings and we'll come up with a plan from there. 

--------

### Wednesday, 5/26 (8 Hours worked)

**Today's non-technical work:**
* Attended Scrum
* Met with Joe to discuss potential updates and rollbacks in the context of Nested OverlayFS overlays
* Started Paper introduction, will complete tomorrow morning/midday. 

**Today's technical work**:
* Started new OverlayFS research project
* Wrote out nested OverlayFS versioning structure, coded some of it. Will continue work on it tomorrow and friday.

I think OverlayFS shows a fair amount of promise in terms of being viable for usage. It's built-in, and exists as a 'feature', if that makes sense. All of the alternatives are third-party(but open source), which increases the margin of error, if only a little bit. If we decide that we value a solution as close to baremetal as possible, OverlayFS provides a ton of value. 



I helped my dad unclog our plumbing today around 5:00. Boy, was it hard. No wonder plumbers have crazy strength. 

----------
### Thursday, 5/27 (8 hours worked)

**Today's non-techical work:**
* Attended Scrum
* Wrote more of FT techologies summary for paper

**Today's technical work:**
* Wrote the brunt of OverlayFS versioning system, now on github. Tomorrow I'll implement the whitelist function.

---------
### Friday, 5/28 (5.5 hours worked)

**Today's non-technical work:**
* Attended Scrum

**Today's technical work:**
* Finished all of the non-whitelist functions for the OverlayFS versioning system

Did not complete as much work as I would have liked, as I felt sick at the start of the day. 

----------------
## Week 3: 6/1 to 6/4
---------------
### Tuesday, 6/1 (8 hours worked)
**Today's non-technical work:**
* Attended Scrum
* Met with Joe about SAGE-883 and joining the software team

**Today's technical work:**
* Finished OverlayFS versioning system with whitelist
* Looked over sanity test suite code and began writing SAGE-883

---------
### Wednesday 6/2 (7 Hours worked)
**Today's non-technical work:**
* Attended Scrum
* Started writing slides for friday's demo

**Today's technical work:**
* Finished first version of SAGE-883 static PSU check. Wrote PR for it, as well. Awaiting feedback from Joe.

---------

### Thursday, 6/3 (7 Hours worked)
**Today's non-technical work:**
* Attended Scrum
* Looked over SAGE-856 issue
* Attended CELS talk

**Today's technical work:**
* Overhauled SAGE-883 with revisions
* learned how to squash commits
----------

### Friday, 6/4 (8 Hours worked)
**Today's non-technical work:**
* Attended Scrum
* Looked over SAGE-856 issue
* Demo'd OverlayFS miniproject
* Met with Joe about SAGE issues and planning for next week

Good week. I mostly spent my time working on software issues, which was fun. 

-----------------
## Week 4: 6/7 to 6/11
-----------
### Monday, 6/7 (4 Hours worked)
**Today's non-technical work:**
* Went to DMV and it consumed half my workday
* Met with Yongho about peripheral configuration manager details
* Brainstormed peripheral configuration manager framework

------------
### Tuesday, 6/8 (8 Hours worked)
**Today's non-technical work:**
* Met with Yongho about peripheral configuration manager details, & he demoed his camera Ansible script
* Met with Omar about finer details of SAGE-856
* Did some more brainstorming for peripheral management mechanism

**Today's technical work:**
* Wrote nx-core tests for SAGE-856

--------------

### Wednesday, 6/7 (7 Hours worked)
**Today's non-technical work:**
* Attended Scrum

**Today's technical work:**
* Troubleshot the SAGE-833 test. It does not work on either nodes I tested it on, but did last week. I have yet to figure out why I can't export the GPIOs. 
* Wrote the rest of the doable tests for SAGE-856

----------

### Thursday, 6/8 (7 Hours worked)
**Today's non-technical work:**
* Attended Scrum

**Today's technical work:**
* Started learning flask for my peripheral configuration manager. For now, I'm calling it honeycomb. 
* Started planning out honeycomb
---------
### Friday, 6/9 (7 Hours worked)
**Today's non-technical work:**
* Wrote presentation for monday 
* Compared and wrote about Pros and Cons of different FT technologies in [list_of_ft_tech.md](./list_of_ft_tech.md)

**Today's technical work:**
* Separated SAGE-856 into separate files
----------
## Week 5, 6/14 to 6/18
---------
### Monday, 6/14 (8 Hours worked)
**Today's non-technical work:**
* Attended part 1 of student presentations 
* Presented at part 1 of student presentations
* Met with Joe to catch up

**Today's technical work:**
* Wrote Unit tests for SAGE-883
-----------
### Tuesday, 6/15 (7 Hours worked)
**Today's non-technical work:**
* Attended Scrum 
* Met with Joe to merge SAGE-856
* Looked into network switch docs

**Today's technical work:**
* Created tftp server and exchanged files from my linux and mac machines
------------
### Wednesday, 6/16 (7 Hours worked)

**Today's non-technical work:**
* Attended Scrum 

**Today's technical work:**
* Wrote some endpoints relating to node creation for honeycomb
-------------
### Thursday, 6/17 (8 Hours worked)

**Today's non-technical work:**
* Attended Scrum
* Met with Joe to discuss SAGE-883

**Today's technical work:**
* Worked on SDCard sanity tests for SAGE-883
-------------
### Friday, 6/18 (7 Hours worked)

**Today's non-technical work:**
* Attended Demo meeting

**Today's technical work:**
* Worked on SDCard sanity tests for SAGE-883
* Worked on RPI Sanity tests for SAGE-883
* Looked into GPG signature verification
-------------
## Week 6, 6/21 to 6/25
-------
### Monday, 6/21 (7 Hours worked)

**Today's non-technical work:**
* Attended Intern introductory meeting
* Met with Joe and Wolfgang to discuss internship path



**Today's technical work:**
* Looked into GPG signature verification with no fruitfulness
* Read up on ramdisks and waggle's create_ramdisk functionality
-------------
### Tuesday, 6/22 (8 Hours worked)

**Today's non-technical work:**
* Attended the sprint planning meeting

All nodes were down from the second half of the day, so I couldn't write the media tests(SAGE-856)
**Today's technical work:**
* Researched ways to verify health of ramdisk, mostly looking into `initramfs` processes and how the `create_initrd` script works
* Read up on initramfs hooks

I should really provide more information in my daily logs, so I'll start doing that with relevant links. 
* https://wiki.archlinux.org/title/mkinitcpio#HOOKS
* https://manpages.debian.org/testing/initramfs-tools-core/initramfs-tools.7.en.html
* https://wiki.debian.org/initramfs
* https://salsa.debian.org/cloud-team/cloud-initramfs-tools
* https://salsa.debian.org/kernel-team/initramfs-tools/-/blob/master/hooks/fsck

-------------

### Wednesday, 6/23 (8 Hours worked)

**Today's non-technical work:**
* No scrum today!
* Read up some more on hooks and how they work in `initramfs`


**Today's technical work:**
* Finished up the ramdisk media tests
* Did some planning for honeycomb on my Miro board


I was a bit blocked today, as I was waiting for a node to be provisioned to me that I could run failure testing on for SAGE-856. I didn't end up getting it today, but it was all good. I learned some more about hooks!

-------------

### Thursday, 6/24 (8 Hours worked)

**Today's non-technical work:**
* Attended Scrum
* Attended Sean's great lecture on plugins and how to deploy them to ECR


**Today's technical work:**
* Wrote several failure tests for SAGE-856, updated the ticket with my progress

-------------

### Friday, 6/25 (8 Hours worked)

**Today's non-technical work:**
* Attended Scrum
* Met with Joe to help push SAGE-856 code

**Today's technical work:**
* Finished failure testing for SAGE-856, commited, and rebased code
* Messed around with an edgeswitch. Very confusing : (

https://dl.ubnt.com/guides/edgemax/EdgeSwitch_CLI_Command_Reference_UG.pdf

-------------
## Week 7: 6/28 to 7/2
-------------
### Monday, 6/28 (8 Hours worked)
**Today's non-technical work:**
* Attended Scrum

**Today's technical work:**
* Spent the entirety of the day doing two rounds of code revisions for SAGE-856
* very tired :( 

-------------

### Tuesday, 6/29 (8 Hours worked)
**Today's non-technical work:**
* Attended Scrum
* Met with Joe twice to merge SAGE-856 (LETS GO!!!!) and to discuss honeycomb design
* Finally finished training

**Today's technical work:**
* Drew up some more designs for honeycomb after joe meeting

-------------

### Wednesday, 6/30 (8 Hours worked)
**Today's non-technical work:**
* Lead Scrum

**Today's technical work:**
* Wrote some code for the HC Client side
* Modeled mock payload JSON


Today was a bit of a slow day, as it was mostly in the repeating cycle of *write a little bit of code* -> *get spooked from large design choice* -> *stare at screen*. I think I can pull this project off, though.

-------------

### Thursday, 7/1 (8 Hours worked)
**Today's non-technical work:**
* Attended Scrum
* Met with Sean to discuss HC design choices and python specifics
* Made my Student intro tile

**Today's technical work:**
* Wrote part of the extract_payload module for HC clientside
* Started demo presentation for tomorrow, came up with idea for standardized HC verification / logging system. Thanks for the idea and help, Sean!

Today's meeting with Sean really helped put my work into better perspective. Tomorrow, I'll meet with Yongho to discuss more of the camera updating code, and get a foothold on my first milestone. 

-------------

### Friday, 7/2 (7 Hours worked)
**Today's non-technical work:**
* Attended Scrum
* Met with Yongho to discuss cameras specifics 
* Finished demo presentation outline

**Today's technical work:**
* Demo'd my presentation, it went well! 

**TODO For next week:**
* Look into process for messing with switches and how it relates to honeycomb
* Discuss switch use cases
* Start development of honeycomb framework and what scripts/criteria need to be met for a successful install
* Make some Jira tickets  


-------------
## Week 8: 7/6 to 7/9
--------
### Tuesday, 7/6 (6 Hours worked)

**Today's non-technical work:**
* Attended Scrum planning meeting
* Wrote out basic honeycomb upgrade framework

**Today's technical work:**
* Made mock upgrade package following hc standards

I had a bit of a headache today, so I took an extra two hours after work to rest. 

**TODO:**
* Make Smaller Jira tickets
* Write hc code to run, check script validity
* Design basic retry functionality
 --------

### Wednesday, 7/7 (8 Hours worked)


**Today's non-technical work:**
* Attended SAGE lunch outing

**Today's technical work:**
* Learned how to integrate python with `journalctl`

My productivity got thrown off by the lunch, and the hour+ of traveling that came with it. I didn't get as much done as I would have liked, but I still learned something.

**TODO:**
* Meet with Joe for switch use cases
* Write out the most basic sequential upgrade script execution
----------

### Thursday, 7/8 (8 Hours worked)


**Today's non-technical work:**
* Sent email to HR about Uber reimbursement
* Met with Joe to discuss basic switch use cases

**Today's technical work:**
* Had to reinstall ubuntu on my ANL computer to be safe 

I had to reinstall ubuntu because I found some wacky activity in `journalctl`.

----------
### Friday, 7/9 (8 Hours worked)


**Today's non-technical work:**
* Attended Scrum
* Researched how to get config off of a switch
* Researched how to get config onto a switch

**Today's technical work:**
* I couldn't do any operations on the switch and node besides RO, so I tried to connect to the switch via scp, and tftp. I had no luck, though.
* Wrote state_check for switch upgrade

I had a good week. Didn't get a ton of work done, but a lot of important information was obtained, and I can probably get some efficient work done next week. 

-------
## Week 9: 7/12 to 7/16
-------
### Monday, 7/12 (8 Hours worked)
**Today's non-technical work:**
* Presented my SAGE midpoint update
* Met with Joe to discuss tftp and ftp server choices, and switch UI

**Today's technical work:**
* Researched usage of dnsmasq tftp server 
* Researched using an ftp server for switch upgrades

-------

### Tuesday, 7/13
**Today's non-technical work:**
* Went kayaking with the team

-------

### Wednesday, 7/14 (8 Hours worked)
**Today's technical work:**
* Researched and set up FTP server properly
* Finally got a config both on and off a switch 

-------

### Thursday, 7/15 (8 Hours worked)
**Today's non-technical work:**
* Attended Scrum 
* Met with Sean to discuss clean ways to update a switch

**Today's technical work:**
* Started honeycomb README file 
* created autoexpect scripts to log in and get information about the switches

**TODO:** 
* change clibanner for switch to represent the config version number
* write hc scripts for switch


-------

### Friday, 7/16 (5 Hours worked)

**Today's technical work:**
* Continued work on HC README
* Changed switch config convention to change the clibanner to include the version number, allowing for clean state checks and install verifications


-------
## Week 10: 7/19 to 7/24
-------

### Monday, 7/19 (7 Hours worked)

**Today's non-technical work:**
* Attended Midpoint presentation round 2
* My breaker node was down the whole day, so I started working on my White paper. 

--------
### Tuesday, 7/20 (8 Hours worked)

**Today's non-technical work:**
* Met with Joe to catch up from his vacation lead

**Today's technical work:**
* Started planning out HC daemon
* Researched outputting logs to `journalctl`
* Created HC `systemd` service 
* Created basic flask server

TODO for tomorrow:
* Furnish flask server according to state diagram
* Organize HC repo

--------

### Wednesday, 7/21 (7 Hours worked)

**Today's technical work:**
* Wrote out OOP python HC structure
* Created `hc_manager` python class for HC daemon
* Created `job` python class for HC daemon

TODO for tomorrow:
* Finish first iteration of `hc_manager` and `job` classes
* Add /getState endpoint to server
* have `job` class parse payload data and create object accordingly

--------

### Thursday, 7/22 (8 Hours worked)

**Today's non-technical work:**
* Attended Scrum, was pretty lame
* Met with Joe about HC client-side server questions

**Today's technical work:**
* Wrote out more of `job` class checks
* Wrote more HC documentation
* Wrote out more of the `/upgrade` client endpoint

TODO for tomorrow:
* Finish environment setup in the `/upgrade` endpoint
* make env cleanup function 
* migrate `/upgrade` endpoint utilities out to a module
* (hopefully) finish the first basic flow of honeycomb ( get payload from `/upgrade`, assess, setup, add job, execute it(maybe not this one) )

--------

### Friday, 7/23 (8 Hours worked)

**Today's non-technical work:**
* Attended Scrum
* Met with Joe to talk HC Architecture

**Today's technical work:**
* Finished `/upgrade` endpoint
* Tackled the concept of continuity across routes via flask app context
* Made git repo for honeycomb 
* Wrote `rsync` script so I can code on my IDE

TODO for the coming monday:
* Assess where I'm at in terms of HC development
* Make /upgrade add real jobs to the `hc_manager` app instance
* (Hopefully) achieve the minimum use case for honeycomb

--------

## Week 11: 6/26 to 6/30

---------

### Monday, 6/26 (8 Hours worked)

**Today's technical work:**
* Created Dummy HC upgrade for testing purposes 
* Created `build_upgrade.sh` script for easy HC upgrade creation 
* Reorganized `/upgrade` code into `hc_util` library 
* Finished the `/upgrade` endpoint

-----------

### Tuesday, 6/27 (8 Hours worked)

**Today's non-technical work:**
* Met with Joe to briefly discuss Honeycomb progress

**Today's technical work:**
* Finished Checksum verification
* Started connecting services to build basic HC use case 
* Added file checks to `job` class 
* Started `job` `state_check` execution code

**TODO:**
* Finish `state_check`, subprocess.run keeps freezing the thread and I can't figure why
* Write `install`, `verify_install` code
* Finish basic use case

-----------
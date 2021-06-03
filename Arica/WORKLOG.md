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

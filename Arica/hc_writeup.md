## Introduction

SAGE(Citation) is a grant dedicated to implementing edge computing functionality into the existing remote sensing Waggle(Citation) platform, which was also built on prior by the Array of Things(Citation) grant. The Waggle platform (and SAGE, as well) are all built on the principle of modularity. The waggle platform is set up for users of any purpose and utility to customize their remote-sensing node to their needs, including the types of peripherals and architecture of the nodes. An essential aspect of maintaining a fleet of nodes is acquiring information regarding the state of nodes, as well as having the ability to control them expressly.

Currently, functionality to monitor and control node states is relatively scarce, save for the diagnostic ability of the Waggle Sanity Test suite, which runs a series of tests to ensure nodes are in working order. The Waggle platform also offers a service called Beekeeper, which maintains and distributes a set of manifests that decide node functionality. 

When looking from a top-down perspective on the Waggle architecture, it becomes apparent that there is a gap in accessibility when managing node states. As such, the groundwork for Honeycomb, a modular node state manager, has been established as my work for the Summer of 2021. The goal of Honeycomb is to allow users to manage the configuration of peripherals on their nodes in a modular fashion.
To gain a better sense of Honeycomb's utility, let us consider a common use case. Consider a fleet of N Wild Sage nodes that use configurable cameras. To change the configuration of a camera, namely the pan and zoom settings, an engineer must log into the node via reverse tunnel and use a script to update the configuration manually. The process of an individual update is relatively quick, but can take an enormous amount of time with a fleet of N nodes. In this case, a system that distributes and installs a camera configuration to a node would save fantastic amounts of time, while providing valuable organizational insight to the user.

## Honeycomb design

Honeycomb's architecture revolves around modularity, and the ability to gain insight into any running upgrades. While modularity is essential, diagnostic information regarding upgrades is equally essential. However, this poses a paradox. A fully modular upgrade to Honeycomb implies that the upgrade code can simply be run from start to finish, with Honeycomb having no insight into the process, as any restrictions on the contents of the upgrade take away from its' modularity. On the other end of the spectrum, an upgrade that Honeycomb has great insight into would have to be nearly custom-written to work on the Honeycomb platform, and is not modular at all. 
As such, Honeycomb's architechture lies in the middle of the modularity spectrum. All upgrades written and queued must have a set of scripts that run a state check, install the upgrade, and verify installation. Honeycomb collects insight from these specific scripts, but the user is free to execute whatever code they please. In turn, Honeycomb can report metrics and insight to the user. 

![Modularity spectrum](./images/spectrum.png)

### Honeycomb design specifics

Honeycomb exists in two major halves: A server-side UI and a client-side `systemd` service. 
![Honeycomb basic architecture](./images/basic_arch.png)
As of early August 2021, the majority of the work for the Honeycomb client-side has been completed. Honeycomb's client-side runs as a `systemd` service, which runs a local `python3` `flask` server. Running a local `http` server on the host node allows for far greater flexibility when the specifics of the Honeycomb server-side counterpart will be designed in the future. Having an endpoint on the client-side server with open ports is unfeasible, as opening ports for non-vital activities on SAGE nodes is highly insecure. However, when the service to intercept upgrade payloads and requests is selected and implemented, the only tool required to use these upgrades is a simple local `http` request to the Honeycomb client. 

### Honeycomb basic flow
To make use of Honeycomb, one needs a properly-formatted Honeycomb payload, which can be built using a script provided in the Honeycomb repository. Next, the upgrade needs to be placed in the `./upgrades`, and an `http` request sent to `/queue-upgrade` with a `filename` query arg pointing to the upgrade file location. Next, the upgrade file is extracted to a temporary directory, and a series of checks to determine the upgrade validity are run. Should all checks pass, an instance of a `job` is created, which is handled in a separate thread by a singular `hc_manager` object. Any job put into the queue is sequentially removed and executed.
 
### Anatomy of a Honeycomb Upgrade
Honeycomb upgrades consist of three parts: 
* A state check, to ensure the state of the upgrade peripheral is correct. Mostly used to determine if an upgrade is necessary(Ex. A camera is on firmware V1.2, when the upgrade is for V1.1 -> V1.2). Ran through the script `hc_state_check.sh`
* An install script. Ran through `hc_install_upgrade.sh`, any and all install code should be executable through this script. 
* An install verification script, ran through `hc_verify_upgrade.sh`. Similar to the state check, but verifies that the upgrade script ran smoothly. 

The aforementioned scripts are executed sequentially, and require the success of the previous script to proceed. Any failure within a job is reported, and terminates. 

### Honeycomb OS versioning system

An overarching goal of Honeycomb is to abstract the concept of a 'peripheral'. An invaluable potential feature of Honeycomb would be to upgrade the state or version of the current WaggleOS image that Wild SAGE nodes run on. To do so, we must define the idea of a 'peripheral' as simply a set of files, features, or devices that can be configured and versioned.

## Fault Tolerance

A preliminary round of research was done to gain knowledge on Fault Tolerance systems, and how they may be applicable to Wild SAGE nodes.

Should a deployed node fail in the field, the personal &  financial cost of repairing it is great, and should be avoided at all cost. Thus, the need for a fault-tolerant operating system for all nodes is critical.

Most importantly, the definition of a fault in this context should be clearly declared, as systems of any kind may have a wide variety of faults. For the purpose of SAGE, a fault is any critical error that prevents SAGE engineers from booting and establishing a reverse tunnel to the node. In conjunction with this flavor of fault tolerance is the topic of atomic upgrades and rollbacks, which often serve as a solution to a faulted system. 

Currently, the Wild SAGE nodes utilize a single-layer Overlay(Citation) for a read-only volume, with all changes being made to a read-write volume elsewhere. This mechanism prevents any changes being made to critical parts of the filesystem, and allows for a 'factory reset' by wiping the read-write layer. 
One of the most common ways to ensure fault tolerance in any arbitrary filesystem is to utilize a process called AB Booting(Citation). AB Booting requires two bootable drives A and B, with either one running some operating system(OS) at any time. Should the in-use drive be unable to boot, the other drive will run diagnostics, fix, re-flash the OS, or even boot on itself as a last resort. Wild SAGE nodes currently utilize AB booting as a final resort, but this approach may not be as effective if OS upgrades are applied in the future. Thus, a system for rolling back an operating system is necessary. 

<!-- Put in some kind of list of the FT technologies  -->


# Write about sanity check background 
## Write about sanity check work 

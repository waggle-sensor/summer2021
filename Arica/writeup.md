SAGE(Citation) is a grant dedicated to implementing edge computing into the existing remote sensing Waggle(Citation) platform, which was also built on prior by the Array of Things(Citation). Should a deployed node fail in the field, the personal &  financial cost of repairing it is great, and should be avoided at all cost. Thus, the need for a fault-tolerant operating system for all nodes is critical.

Most importantly, the definition of a fault in this context should be clearly declared, as systems of any kind may have a wide variety of faults. For the purpose of SAGE, a fault is any critical error that prevents SAGE engineers from booting and establishing a reverse tunnel to the node. In conjunction with this flavor of fault tolerance is the topic of atomic upgrades and rollbacks, which often serve as a solution to a faulted system. 

Currently, the Wild SAGE nodes utilize a single-layer Overlay(Citation) for a read-only volume, with all changes being made to a read-write volume elsewhere. This mechanism prevents any changes being made to critical parts of the filesystem, and allows for a 'factory reset' by wiping the read-write layer. 
One of the most common ways to ensure fault tolerance in any arbitrary filesystem is to utilize a process called AB Booting(Citation). AB Booting requires two bootable drives A and B, with either one running some operating system(OS) at any time. Should the in-use drive be unable to boot, the other drive will run diagnostics, fix, or re-flash the OS, or even boot on itself as a last resort. Wild SAGE nodes currently utilize AB booting as a final resort, but this approach may not be as effective if OS upgrades are applied in the future. Thus, a system for rolling back an operating system is necessary. 

[Maybe make this part related work? But it's not really related work]

There are several existing technologies that can potentially provide functionality for fault tolerance and OS version control. The deemed most relevant for SAGE are:

[Btrfs](https://wiki.archlinux.org/title/btrfs): 
-    A copy-on-write filesystem that specializes in fault tolerance. 
        - The copy-on-write functionality can be toggled for individual files, but not for individual subvolumes. Every mounted subvolume must have the same copy-on-write settings. 
-   An interesting fault tolerance feature, Btrfs includes 'snapshots',  which utilizes the copy-on-write mechanic. By definition from the [wiki](https://btrfs.wiki.kernel.org/index.php/SysadminGuide#Snapshots), a snapshot is *'simply a subvolume that shares its data (and metadata) with some other subvolume'*. 
    -   This works because a snapshot is a *copy* of some file system. Because copy-on-write doesn't overwrite/delete files, and rather makes a copy of a new file with changes, you can roll back entire trees by just uncaching the version without changes. There's a basic method of doing this in the wiki link above. 

Pros: 
* Can be combined with Snapper to accomplish goal of Fault Tolerance
* All operations with Btrfs and Snapper are atomic

Cons: 
* Does not have any built-in atomic upgrade feature, only rollbacks & snapshots. Upgrading is left to the engineer to implement, but may be simple enough.  
* Using a Btrfs filesystem may not be compatible with some Wild SAGE features. 

[openSUSE:Snapper](https://en.opensuse.org/openSUSE:Snapper_Tutorial):
-    A tool to manage snapshots in conjunction with Btrfs. Any subvolume that you want to use Snapper with must be specified. Provides several ways for creating, managing, and configuring snapshots. The simplest usage case is by downloading some OS update, creating a snapshot of the current OS, installing the update, and rolling back to the snapshot when needed. Snapper works hand-in-hand with zypper and YaST by creating snapshots whenever they are used, and can easily undo these changes. 

Pros/Cons: See Btrfs Pros/Cons

[OSTree](https://github.com/ostreedev/ostree): 

-    A system that allows the committing, deploying and managing of Bootable OS trees. It is important to note that OSTree does not maintain any insight into the stored OS's themselves- it mostly acts as a 'package manager' for Bootable Operating Systems. 
        - The example given by the documentation mentions the case of some dev needing insight into which version of OpenSSL is installed on some OS, and that the person responsible for committing the OS should also support that functionality. 
-    Has some functionality with Btrfs. Baremetal implementations of OSTree are the most useful.
- OSTree preserves /var across updates

Pros: 
- Allows atomic upgrades and rollbacks. 
- The package-manager style of OSTree allows for more organized version control (OSTree tracks our OS for us)

Cons: 
- Adapting an existing system to OSTree adds a layer of complication, as some system restructuring is required
- OSTree is considerably more complex than other solutions, which should be avoided when considering fault tolerance. 

[RHEL Atomic host](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux_atomic_host/7/html/installation_and_configuration_guide/introduction_to_atomic_host):
- RedHat Enterprise Linux Atomic Host is a light-weight version of RedHat designed to run containers. It runs on `rpm-OSTree`, and mimics a lot of OSTree's behavior with `rpm` support, in addition to doing the aforementioned operations atomically. The boot OS is read-only, with only `/etc` and `/var` being writable. When an upgrade happens, a pre-upgrade version of the OS is maintained in tandem, allowing for atomic rollbacks. **May not be compatible with the SAGE hardware**. 

Pros:
- The OS is designed for nodes running containers coupled with a RO RootFS
- Essentially a fully implemented version of OSTree, but OS upgrades are optimized as only the delta of the file is transferred over network, sparing plenty of bandwidth. 

Cons: 
-  RHEL Atomic Host is a completely different OS, and transferring SAGE nodes over would be a herculean task.
- May not work with SAGE hardware. See [RHEL hardware compatibility list](https://hardware.redhat.com/).  

[OverlayFS](https://wiki.archlinux.org/title/Overlay_filesystem):
- Allows the creation of Overlay file systems. In essence, a lower and upper directory are mounted into a new directory such that any changes made to the lower directory appear in the upper directory, allowing for clean rollbacks and data protection. 
- Multiple lower directories can be mounted on top of each other, giving a prospective functionality for upgrades and rollbacks. Upon some critical failure, a theoretical upper directory wipe can take place, with a rollback to the last stable version. 

Pros: 
- The OverlayFS mechanism is simple, and easy to understand
- Does not require any more memory than necessary- Any upgrades and rollbacks made ONLY include changed files, and not an entire new filesystem. 

Cons: 
- Will need a reboot every time an update is made. If there are any open files that are being replaced, trying to change them in real-time may be catastrophic.
- Updates may require an SD boot, and upgrading the NVME from the SD

[Fedora IoT](https://docs.fedoraproject.org/en-US/iot/): 
* A version of Fedora optimized for IoT deployments and applications. Very similar to RHEL Atomic Host. Runs on `rpm-OSTree` and supports atomic upgrades and rollbacks. 
* Has support for container-based workflows. 

Pros: 
- Fedora IoT is essentially a Fedora image with OSTree capabilities worked in, with some container workflows included. It does not appear to protect the RootFS like RHEL Atomic host, or any other fancy Fault Tolerance measures. This makes it more customizable for the purposes of SAGE.

Cons: 
- SAGE infrastructure may not work on Fedora systems, and transferring between Unix distributions is a large task. 

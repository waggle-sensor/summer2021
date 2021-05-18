# Kenan's work log

## Week 1:  5/17 to 5/21
---------
### Monday, 5/17 (8 Hours worked)

**Today's non-technological work:** 
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


### Tuesday, May 18



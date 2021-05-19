# My OSTree test

Testing OSTree functionality in line with what I ~think~ the fault tolerance for SAGE is needed. This is going to be VASTLY simplified, and will not represent any specific task in the actual job. 
The steps to the process are: 

* Create a set of processes that constantly do a subset of varied actions (make file changes, make requests, etc)
* Create a random chance to fault. In this context, faulting will mean some essential file gets corrupted or deleted
* Notify some daemon of a fault, daemon will wipe the file system and reset it

## Setup: 

(Tested and ran fully on a NodeJS ubuntu devcontainer)

* install ostree (apt-get install ostree)
* Run `setup-ostree` to set up the repo and branch
* run `npm install`
* run `node daemon.js`

The idea is to simulate a fault, when `the_vault/the_sewers/the_goods` is deleted. Mock_sensorgram has a 1/10 chance of deleting `the_goods` per cycle, at which the daemon will detect a fault, run some OSTree magic to restore the entire directory, and continue. 


Later TODO: 
* change the setup into a makefile
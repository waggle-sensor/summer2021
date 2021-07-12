# extract_payload module for SAGE Honeycomb 
# Written by Kenan Arica
# Yell at him if this breaks
import subprocess
import os
import json
# system logging needed
import logging
from systemd.journal import JournalHandler
# grab our node_manifest file
path_to_manifest = "node_manifest.json" # change to /etc/waggle/node_manifest.json
manifest = open(path_to_manifest, "r")
manifest_json = json.load(manifest)
manifest.close()
print("This code has run")

def extract_payload(payload): 

    # verify that information in payload is correct for now, it is just:
    # does the node ID match? 

    if not "nodeID" in payload:
        print("[ERROR] nodeID not found in payload. Exiting")
        # handle error here
        exit(1)

    # there are a million ways to get the hostname, this code can be changed if it is janky
    if os.uname()[1] != payload["nodeID"]:
        print("[ERROR] nodeID does not match local hostname. May not be the correct node.")
        exit(2)
    
    for peripheral_update in payload["updates"]:
        update_peripheral(peripheral_update)

# might not be a good idea to use the var name 'payload' across functions, but it makes the most sense for now

def update_peripheral(payload):
    print(payload)
    
    print(manifest_json)

    initialize_update_env(payload)

    # make a tmp directory for handling downloads, upgrades
    # if this fails, remember to delete this newly created directory

    # get the file, place it in new dir

    required_files = ["metadata.json", "hc_state_check.sh", "hc_install_upgrade.sh", "hc_verify_upgrade.sh"]

    """ unzip, and run the following files:
    
    metadata.json
    hc_state_check.sh
    hc_install_upgrade.sh
    hc_verify_upgrade.sh
    
    """

    for file in required_files:
        if not os.path.isfile(file):

            print(f"[HC] Could not find {file}. Aborting.")
            exit(1)
    

def initialize_update_env(peripheral_update):
    print(peripheral_update)
    os.chdir("/tmp/")

    peripheral_id = peripheral_update["peripheral_id"]
    os.mkdir(peripheral_id)
    os.chdir(f"/tmp/{peripheral_id}")

    """ make the working update folder. Should look like this:
    Note- the /?/peripheral_id/ is undecided for now. 
    
    /?/peripheral_id/upgrade_version/
    |- /install/ (unzip payload here)
    |- metadata.json

    """
    # put a call to os.path.chdir() here so this code runs wherever. 

# set up journalctl routing
def init_logging():

    log = logging.getLogger('honeycomb')
    log.addHandler(JournalHandler())
    log.setLevel(logging.DEBUG)
    log.info("Beginning Honeycomb upgrade session")
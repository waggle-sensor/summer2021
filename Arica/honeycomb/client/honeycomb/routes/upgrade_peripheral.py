from flask import Blueprint, render_template, session, abort, request
import os 
import json
import logging

logging.basicConfig(level=logging.INFO)

upgrade = Blueprint("upgrade", __name__)

@upgrade.route("/upgrade", methods=['POST'])
def process():

    payload = request.json
    logging.info(payload)
    
    # check that we have a valid payload
    check_payload_validity(payload)
   
   # set up payload env

   # download the payload
    retrieve_payload_contents(payload)

   
    return { "message" : "upgrade endpoint called" }

# TODO: It might be useful to move these computational functions out of this route? maybe import them from somewhere.  
# TODO: make a cleanup function if the payload is not good. basically just delete the upgrade folder 
def init_upgrade_env(payload):
    logging.info("Creating upgrade environment")
    

def retrieve_upgrade_contents(payload): 

    # use 'config_link' to download the payload 
    # for now, since I don't want to host a local server, I'll have the zip downloaded
    logging.info("TODO: Implement payload download") 

def check_payload_validity(payload): 
    
    # check for a set of keys in our payload that we really need 
    fields = ["node_id", "flags", "peripheral_name", "config_version", "config_link" ]
    
    for field in fields:
        if field not in payload:
            raise ValueError(f"{field} was not found in payload")

        logging.info("Payload request is valid")


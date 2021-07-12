## Honeycomb TODO: 

**Where we're at now:**
* Start of the project, trying to build from the bottom up. At the end of this leg, we'll have a working python daemon that can recieve a body of JSON, and extract/install the configs. To start the next leg, we'll write the code to update the cameras and use that as a control/base. 
* Goal usage case: User can use a server-simulated body of JSON to do basic, automatic updates

**Current tasks:**
* Make the unpack_payload module ( !!! )
    * We have an example of the payload json in [update_payload_mockup.json](./update_payload_mockup.json). First, we should make this a real 'mock' payload and give it some usable data.
* Write the process_payload module ( !!! ) 
    * Contingent on the unpack_payload module. Talk to yongho about the camera updating code.
* Write some form of logger module ( !! )
* Make the systemd service for honeycomb ( ! )

**Next steps**:
* Once we can take in a body of JSON and get our desired functionality, we'll need to make some kind of endpoint or server on the nodes that will intercept a new update. For now, we can just `curl` the json we want.

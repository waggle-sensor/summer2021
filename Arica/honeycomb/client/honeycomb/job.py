import logging

class job:

    def __init__(self, manifest):
        logging.basicConfig(level=logging.INFO)
        # go through every required field in the manifest and check for it
        # manifest refers to the manifest.json file that is required in every upgrade zip
        
        if "upgrade_name" in manifest:
           self.__name = manifest["upgrade_name"] 
        else:
           self.__name = f"{manifest['peripheral_name']}-{manifest['config_version']}" 
        
        # run our checks
        logging.info(f"Checking validity of {self.__name} upgrade payload")
        self.check_manifest_validity(manifest)
        
        logging.info(f"Checking existence of required files in {self.__name} root dir")
        self.check_required_files(manifest) 


    def check_manifest_validity(self, manifest):
        # add check for necessary hc files, make sure to chdir into the root_dir path (if provided)
        required_fields = ["config_version", "force_install","retry_state_check", "retry_install", "retry_verify", "peripheral_name", "force_install"]
        
        for field in required_fields:
            if field not in manifest:
               raise ValueError(f"{field} was not found in manifest for upgrade {self.__name}- aborting")

        logging.info(f"Upgrade {self.__name} metadata.json all good ✓")

    def check_required_files(self, manifest):
        
        # check if we have a different root dir
        # if we do, we have to cd in first
        if 'root_dir' in manifest:
            logging.info(f"root dir found: {manifest['root_dir']}")


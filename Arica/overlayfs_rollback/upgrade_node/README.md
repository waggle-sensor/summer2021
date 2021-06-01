#  Overlay upgrade/rollback proof of concept

To start: 
Check out `mount_order` to see how the OverlayFS will be mounted, and make your changes as needed. If you don't want to upgrade from changes in `mount_order`, you can initialize the OverlayFS running `./rollback.sh --reload`.  

## Usage:

Mounting order is determined by the `mount_order` file. All features depend on this file, so don't mess it up!

`./upgrade.sh <foldername>`: Unmounts, re-mounts with your update on top of it. The upgrade should always be in the form of a directory. 

`./rollback.sh`: Rolls back a single update. Unmounts, removes the latest upgrade from the mount order, and re-mounts.

`./rollback.sh --reload`: Does not roll back, but refreshes your OverlayFS. Unmounts and remounts based on the `mount_order` file. You can modify `mount_order` as you like, then run this command to refresh your Overlay FS. 

### Whitelist: 

The whitelist functionality allows for preserving written data through upgrades/rollbacks. Write the path of the file to whitelist in `whitelist`. If you make a directory on the current version and populate it, you can whitelist the entire directory by entering `path/to/dir/` in `whitelist`. It is important to note that this functionality does NOT work with directories that already exist in lower layers of the OverlayFS, as you'd be trying to whitelist a directory that already has some files that don't need to be preserved. I'll fix this later.  
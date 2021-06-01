
# check if we have an input directory
if [ $# -eq 0 ]
    then 
        echo "[ERROR] No input directory supplied"
        exit

fi

if [ -d $1 ] 
    then 
        echo "Directory found!"
    else
        echo "[ERROR] Input directory not found!"
        exit

fi

echo "Upgrading to $1"

# unmount our current setup, which would be in overlay/
# might need sudo here but im not gonna mess with that right now
sudo umount overlay/

# check the whitelist to copy contents to a tmpfs

# wipe upper/ , deleting our written data in the process.
# we're pretending that our lower partitions are all RO, which should be implemented tbd

cd upper
# grab the whitelisted stuff
while read line; do
    echo $line
    # echo $(pwd)
    if [ -d $line ]; 
    then
        mv $line ../whitelist_tmp/
    
    else
        cp --parents $line ../whitelist_tmp
    fi

done < "../whitelist"

# wipe the RW layer

rm -rf ./*


cd ..
# mount our new folder 
# generate the mount string for the nested mount command based off the mount_order file and 
# the folder supplied by the CLI arg  
mount_file="mount_order"
mount_string=""

boot_order=()

while read line; do 
    boot_order+=($line)
done < $mount_file

# for x in ${boot_order[@]}; do
#     echo $x
# done

mount_string=""
# get length of our array
num_boots=${#boot_order[@]}
# go through it in reverse and make our nested overlay string
for(( i=num_boots-1; i >= 0; i-- ))
do 
    # echo ${boot_order[i]}
    mount_string="${mount_string}:./${boot_order[i]}"
done
mount_string="./$1:${mount_string:1}"
echo $mount_string


sudo mount -t overlay -o lowerdir=${mount_string},upperdir=./upper/,workdir=./workdir/ none overlay/

# copy our whitelist from the tmpfs into our target

# copy everything in the whitelist back into the overlay
cd whitelist_tmp

while read line; do
    echo $line
    # echo $(pwd)
    if [ -d $line ]; 
    then
        mv $line ../overlay/
    
    else
        cp --parents $line ../overlay/
    fi

done < "../whitelist"

# add our new boot arg to our mount_order file
cd ..
echo "$1" >> mount_order 
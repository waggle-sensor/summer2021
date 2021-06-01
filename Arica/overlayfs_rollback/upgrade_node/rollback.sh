# unmount
sudo umount overlay/

# if we have the --remount flag, update will not be rolled back.
# In this case, you can delete as many snapshots as you want from the mount_order file and remount. 

if [ $# -eq 1 ];
    then 
        if [ "$1" == "--remount" ];
            then
                echo "Remounting..."
        fi
    else
        echo "Rolling back"
        # take off the last mount in the file
        sed -i '$ d' mount_order
fi

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

# copied from upgrade.sh, remounting
mount_file="mount_order"
mount_string=""

boot_order=()

while read line; do 
    boot_order+=($line)
done < $mount_file


mount_string=""
# get length of our array
num_boots=${#boot_order[@]}
# go through it in reverse and make our nested overlay string
for(( i=num_boots-1; i >= 0; i-- ))
do 
    # echo ${boot_order[i]}
    mount_string="${mount_string}:./${boot_order[i]}"
done

mount_string="${mount_string:1}"
echo "Remounting list: $mount_string"


sudo mount -t overlay -o lowerdir=${mount_string},upperdir=./upper/,workdir=./workdir/ none overlay/

# copy everything in the whitelist back into the overlay
cd whitelist_tmp

# while read line; do
#     # cp -R $line ../overlay/
#     echo $(pwd)
#     mkdir -p $line ../whitelist_tmp/
#     mv $line ../overlay/
# done < "../whitelist"

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

rm -rf ./*
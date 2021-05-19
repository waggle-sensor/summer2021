# delete the current branch
echo "Deleting critical_processes"
rm -rf critical_processes

# reset the branch
echo "Checking out"
ostree --repo=critical checkout stable critical_processes/

# restart the script
cd critical_processes/
node mock_sensorgram.js
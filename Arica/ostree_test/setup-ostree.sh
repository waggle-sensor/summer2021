# make the repo
echo "Making OSTree repo"
ostree --repo=critical init

# make our branch
echo "Making OSTree branch"
ostree --repo=critical commit --branch=stable critical_processes/


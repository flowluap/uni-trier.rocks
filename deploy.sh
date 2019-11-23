cd /home/deploy/files
echo "Pulling from Stable"

sudo git reset --hard
echo "Git reset"

sudo git pull origin files
echo "Pulled successfully from master"

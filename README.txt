1. Fire up AWS with the correct AMI, instance, and volume.
2. Make a data folder, and mount your drive.
3. Grab the startup scripts (setup_ucb_complete_plus_postgres.sh) and install.  These scripts include postgres.
4. Install: psychopg, tweepy.
5. Create a new sparse project - extweetwordcount.
6. Grab from GitHub the spouts/python, bolts/python, topology/cli files, and move to the respective folders in extweetwordcount.
7. Move the python files to the extweetwordcount folder.
8. Run psycho-sample.py to create the tcount database and table.
9. Run hello-stream-twitter.py to ensure Twitter API is configured correctly.
10. Type sparse run to get everything started.  This will populate your database table.


mkdir /data
mount -t ext4 /dev/<your device> /data
chmod a+rwx /data
cd data
wget https://s3.amazonaws.com/ucbdatasciencew205/setup_ucb_complete_plus_postgres.sh
chmod +x ./setup_ucb_complete_plus_postgres.sh
./setup_ucb_complete_plus_postgres.sh <*the device path from step 2*>

pip install psycopg2==2.6.2
pip install tweepy

sparse quickstart extweetwordcount

git clone https://github.com/timothymaltjr/exercise_2.git
mv psycopg-sample.py /root/extweetwordcount/psycopg-sample.py
mv hello-stream-twitter.py /root/extweetwordcount/hello-stream-twitter.py
mv Twittercredentials.py /root/extweetwordcount/Twittercredentials.py
psql -U postgres

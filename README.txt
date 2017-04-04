These are the steps I took to get this exercise completed:

1. Fire up AWS with the correct AMI, instance, and volume.
2. Make a data directory, mount your drive to data, and go into that directory.
3. Grab the startup scripts (setup_ucb_complete_plus_postgres.sh) and install.  These scripts include postgres which is required.
4. Install: psychopg, tweepy.
5. Create a new sparse project - extweetwordcount, and delete the topologies/wordcount.clj file, the src/spouts/python file, and the srv/bolts/python file.
6. Clone from my GitHub my Exercise 2. 
7. Move the topology/clj file (just one), spouts/python file (also just one), bolts/python files (two files) from Exercise 2 into the respective extweetwordcount folders (topology, src/spouts, src/bolts).
8. Move the python files - psycopg-sample.py, hello-stream-twitter.py, and Twittercredentials.py - to the extweetwordcount folder.
9. Move the python files created by Tim for the exercise - finalresults.py, histogram.py - to the extweetwordcount folder.
10. Run psycho-sample.py to create the database (tcount) and table (tweetwordcount).
11. Run hello-stream-twitter.py to ensure Twitter API and credentials are configured correctly.
12. Type sparse run to get the streaming started.  This will populate your postgres database table - tcount.tweetwordcount.
13. Hit Control-C to stop the stream (I could have deleted the code that displays the live-streaming, but I decided not to).
14. Type python finalresults.py to run the finalresults program (this is also designed for one argument, or an error message if more than one argument is passed).
15. Type python histogram.py to run the histogram program (if no arguments, the program will list all entries in the database, if two integers are passed, the program will list all entries with counts between/inclusive of the arguments).
16. Screenshots are in the github screenshots folder.
17. The Plot.png screenshot is in the exercise_2 folder.
18. Architecture.pdf is in the github exercise_2 folder.
19. This readme.txt is in the github exercise_2 folder.
20. Enjoy!

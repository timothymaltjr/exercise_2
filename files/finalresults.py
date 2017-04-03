import sys
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Connect to existing tcount
conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")

program_name = sys.argv[0]
arguments = sys.argv[1:]
count = len(arguments)

if count > 1:
    #Exits the program because more than one argument was passed.
    
    print("Please rerun and enter only one word/argument.")
    exit()

elif count == 0:
    #SQL script to return all words and their count, ordered by word.

    cur = conn.cursor()
    cur.execute("SELECT word, count from tweetwordcount ORDER BY word")
    records = cur.fetchall()
    for rec in records:
       print(rec[0], rec[1])
    conn.commit()

    conn.close()

elif count == 1:
    #SQL script to return one word with its respective count.
    input1 = arguments[0]
    status = 0

    cur = conn.cursor()
    cur.execute("SELECT word, count FROM tweetwordcount")
    records = cur.fetchall()
    for rec in records:
       if rec[0] == input1:
           print("Total number of occurrences of", rec[0], rec[1])
           status =+ 1

    if status == 0:
        print("There are zero occurrences of", input1)
    conn.commit()

    conn.close()

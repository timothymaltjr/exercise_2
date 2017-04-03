import sys
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Connect to existing tcount
conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")

program_name = sys.argv[0]
arguments = sys.argv[1:]
count = len(arguments)

if count > 1:
    print("Please rerun and enter only one word/argument.")
    exit()

elif count == 0:
    #SQL script to return all words and their count ordered by word

    cur = conn.cursor()
    cur.execute("SELECT word, count from tweetwordcount ORDER BY word")
    records = cur.fetchall()
    for rec in records:
       print(rec[0], rec[1])
    conn.commit()

    conn.close()

elif count == 1:
    #SQL script to return one word with its respective count

    cur = conn.cursor()
    cur.execute("SELECT word, count FROM tweetwordcount WHERE word=%s", (arguments[0]))
    records = cur.fetchall()
    for rec in records:
       print("Total number of occurrences of", rec[0], rec[1])
    conn.commit()

    conn.close()

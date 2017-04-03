import sys
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Connect to existing tcount
conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")

program_name = sys.argv[0]
arguments = sys.argv[1:]
count = len(arguments)

#Ends program due to CLI arguments not equaling two.
if count != 2:
    print("Please rerun and only enter two integers in the CLI.")
    exit()

input1 = int(arguments[0])
input2 = int(arguments[1])

#Sets the lower and upper boundries for the SQL query.
if input1 < input2:
    lower = input1
    upper = input2
else:
    upper = input1
    lower = input2

print("Min:", lower)
print("Max:", upper)

#SQL script to return all words and counts greater/less/equal to the bounds.
#cur = conn.cursor()
#cur.execute("SELECT word, count from tweetwordcount WHERE count BETWEEN %s AND %s", (lower, upper))
#records = cur.fetchall()
#for rec in records:
#   print(rec[0], ": ", rec[1])
#conn.commit()

#conn.close()

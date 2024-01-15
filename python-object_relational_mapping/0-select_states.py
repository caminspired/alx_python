# this module contains an SQL script that lists all cities from a database
import MySQLdb
import sys

#define functions 
def list_states(username, password, database):

    #assigns variables and values
    db = MySQLdb.connect(host="localhost",
                        user="username",
                        passwd="password",
                        db="hbtn_0e_0_usa",
                        port=3306
                        )
    
    cursor = db.cursor()

    #executes SQL command in Python
    cursor.execute("SELECT * FROM states ORDER BY states.id")

    states = cursor.fetchall()

    #print results of query 
    for state in states:
        print(state)

#commit commands to execute
db.commit()

#close all connections
cursor.close()
db.close()

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: {} <mysql_username> <mysql_password> <database_name>".format(sys.argv[0]))
        sys.exit(1)

    # Get MySQL credentials from command line arguments
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Call the select_states function with provided credentials
    list_states(username, password, database)

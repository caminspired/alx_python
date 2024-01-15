# this module contains an SQL script that lists all cities from a database
import MySQLdb

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

#MAIN CODE

import pymysql

try:
    db = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        db='projectdb'
    )
    print("Database connected successfully")
except:
    print("Connection failed")



# Open database connection


# Prepare a cursor object
cursor = db.cursor()

# SQL query to insert data into the table
sql = "INSERT INTO question (id, qt) VALUES (%s, %s)"
val = ("value1", "value2")

try:
   # Execute the SQL command
   cursor.execute(sql, val)
   # Commit your changes in the database
   db.commit()
   print("Data inserted successfully!")
except:
   # Rollback in case there is any error
   db.rollback()
   print("Error: Failed to insert data into table.")

# Disconnect from database
db.close()

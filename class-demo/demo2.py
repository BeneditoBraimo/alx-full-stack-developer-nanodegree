"""
    this script demonstrates how to use string composition with the psycopg2 
    DBAPI
"""

import psycopg2

# connect to the database
connection = psycopg2.connect('dbname=example')

# start a new section
cursor = connection.cursor()

cursor.execute('DROP TABLE IF EXISTS table2;')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS table2 (
        id INTEGER PRIMARY KEY,
        completed BOOLEAN NOT NULL DEFAULT false
    );
''')

# using string compostion in a sql statement

cursor.execute('INSERT INTO table2 (id, completed) VALUES(%s, %s);', (1, True))


# another way of using string composition in a sql statement
SQL = 'INSERT INTO table2 (id, completed) VALUES(%(id)s, %(completed)s);'

# a dictionary with the data to be inserted into the table
data = {
    'id': 2,
    'completed': False
}

# using the 'SQL' variable and 'data' dictionary as execute() method parameters

cursor.execute(SQL, data)

# save changes
connection.commit()

cursor.execute('SELECT * FROM table2')
result = cursor.fetchall() # fetch all the rows in the table
print(result)
result = cursor.fetchone()
print(result)
result = cursor.fetchone()
result = cursor.fetchmany(2)
print(result)
# close the connection to the database
connection.close()

# end the session
cursor.close()
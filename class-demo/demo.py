import psycopg2

# connect to the 'example2' database 
connection = psycopg2.connect('dbname=example')

# start a session
cursor = connection.cursor()


#add a table to the database
cursor.execute('''
    CREATE TABLE table2 (
        id INTEGER PRIMARY KEY,
        completed BOOLEAN NOT NULL DEFAULT False
    );
''')

#add a row to the table created
cursor.execute('INSERT INTO table2(id, completed) VALUES(1, True);')

#save the databse changes
connection.commit()

# close connection
connection.close()

# end the session
cursor.close()


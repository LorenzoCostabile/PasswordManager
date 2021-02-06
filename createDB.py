import sqlite3
from sqlite3 import Error
from datetime import date
# code from https://www.sqlitetutorial.net/sqlite-python/creating-database/
# also from https://www.tutorialspoint.com/sql-using-python-and-sqlite


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def createTable(table,dBname):
    # creating an connection
    conn = sqlite3.connect(dBname) # db - database

    # Cursor object
    cursor = conn.cursor()

    # code to create a databse table
    create_table_sql = table
    # executing the above SQL code
    cursor.execute(create_table_sql)

    # saving the changes using commit method of connection
    conn.commit()

    # closing the connection
    conn.close()


def insertValues(values,dBname,tableName=None):
    # inserting data into the students table
    # using ? insted to formating the string protects the db from injection attacks

    # creating an connection
    conn = sqlite3.connect(dBname) # db - database

    # Cursor object
    cursor = conn.cursor()

    #values.insert(0,tableName)
    #to do: Passing the name of the table pretected from sql injections.
    insert_student_one_sql = """INSERT INTO passwords VALUES ( ?, ?, ?, ?, ?, ?);"""
    cursor.execute(insert_student_one_sql,values)

    # saving the changes using commit method of connection
    conn.commit()

    # closing the connection
    conn.close()

def exploreDatabase(nameDB,tableName=None):
    # creating an connection
    conn = sqlite3.connect(nameDB) # db - database

    # Cursor object
    cursor = conn.cursor()

    # SQL query to get all students data
    #to do: Passing the name of the table pretected from sql injections.
    fetch_passwords_sql = """
    SELECT * FROM passwords;
    """

    # executing the SQL query
    cursor.execute(fetch_passwords_sql)

    # storing the data in a variable using fetchall() method
    passwords = cursor.fetchall() # a list of tuples

    # printing the data
    print(passwords)

def filterForWeb(web,database):

    # creating an connection
    conn = sqlite3.connect(database) # db - database

    # Cursor object
    cursor = conn.cursor()

    fetch_passwords_sql ="SELECT password FROM passwords WHERE website_name = ?"


    # executing the SQL query
    cursor.execute(fetch_passwords_sql,[web])

    # storing the data in a variable using fetchall() method
    passwords = cursor.fetchall() # a list of tuples

    return passwords
    

if __name__ == '__main__':
    #CREAR BASE DE DATOS
    #create_connection(r"egongoIsSafe.db")

    #CREAR TABLA EN BASE DE DATOS
    
    table = """
    CREATE TABLE passwords (
    website_name CHAR,
    link CHAR,
    password CHAR,
    user CHAR,
    email CHAR,
    lastUpdateDate CHAR
    );
    """
    createTable(table,r"egongoIsSafe.db")
    

    #INSERTAR DATOS
    #valores = ['facebook','https://www.facebook.com/','password','password','password@password.pass',str(date.today())]
    #valores = ['twitter','https://www.twiter.com/','password','password','password@password.pass',str(date.today())]
    #insertValues(valores,"egongoIsSafe.db")

    #EXPLORAR DATOS
    #exploreDatabase(r"egongoIsSafe.db")



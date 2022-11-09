import sqlite3
from sqlite3 import Error


def openConnection(_dbFile):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    print("++++++++++++++++++++++++++++++++++")
    print("Open database: ", _dbFile)
    conn = None
    try:
        conn = sqlite3.connect(_dbFile)
        print("success")
    except Error as e:
        print(e)
    print("++++++++++++++++++++++++++++++++++")
    return conn

def closeConnection(_conn, _dbFile):
    print("++++++++++++++++++++++++++++++++++")
    print("Close database: ", _dbFile)
    try:
        _conn.close()
        print("success")
    except Error as e:
        print(e)
    print("++++++++++++++++++++++++++++++++++")

#Create Tables for database
def createTables(_conn):
    print("Creating Tables")
    _conn.execute("BEGIN")

    try:
        #Done for now
        #a_location will be used to determine whether the car is at a dealership, warehouse, manufacturer, etc.
        sql = """CREATE TABLE automobile ( 
            a_vinID integer PRIMARY KEY,
            a_make varchar(50) NOT NULL,
            a_model varchar(50) NOT NULL,
            a_type varchar(50) NOT NULL,
            a_year integer NOT NULL,
            a_condition varchar(15) NOT NULL,
            a_price decimal(10,2) NOT NULL,
            a_color varchar(15) NOT NULL
            a_location integer NOT NULL
        )"""
        _conn.execute(sql)
        print("success automobile table")
#--------------------------------------
        #Done for now
        sql = """CREATE TABLE customer (
            c_custkey integer PRIMARY KEY,
            c_vinID integer NOT NULL REFERENCES automobile(a_vinID);
            c_last varchar(50) NOT NULL,
            c_first varchar(50) NOT NULL,
            c_age integer NOT NULL,
            c_phone varchar(50) NOT NULL,
            c_address varchar(50) NOT NULL,
            c_city varchar(50) NOT NULL,
            c_state varchar(50) NOT NULL,
            c_email varchar(65) NOT NULL
        )"""
        _conn.execute(sql)
        print("success customer table")
#--------------------------------------
        #Done for now
        sql = """CREATE TABLE seller (
            s_sellerkey integer PRIMARY KEY,
            s_vinID integer NOT NULL REFERENCES automobile(a_vinID),
            s_name varchar(75) UNIQUE NOT NULL,
            s_phone varchar(20) UNIQUE NOT NULL,
            s_city varchar(50) NOT NULL,
            s_state varchar(50) NOT NULL,
            s_email varchar(75) UNIQUE NOT NULL
        )"""
        _conn.execute(sql)
        print("success seller table")
#--------------------------------------
        #Done for now
        sql = """CREATE TABLE manufacturer (
            m_manufacturerkey integer PRIMARY KEY,
            m_name varchar(50) UNIQUE NOT NULL REFERENCES automobile(a_make),
            m_email varchar(50) NOT NULL,
            m_address varchar(50) NOT NULL,
            m_city_state varchar(50) NOT NULL
        )"""
        _conn.execute(sql)
        print("success manufacturer table")
#--------------------------------------
        sql = """CREATE TABLE transactions (
            t_trkey integer PRIMARY KEY,
            t_custkey integer NOT NULL REFERENCES customer(c_custkey),
            t_sellerkey integer NOT NULL REFERENCES seller(s_sellerkey),
            t_vinID integer UNIQUE NOT NULL REFERENCES automobile(a_vinID)'
            t_date date NOT NULL
        )"""
        _conn.execute(sql)
        print("success transactions table")
        
#--------------------------------------
        #Done for now
        sql = """CREATE TABLE warehouse (
            w_key integer PRIMARY KEY,
            w_sellerkey integer REFERENCES seller(s_sellerkey) NOT NULL,
            w_vinID integer REFERENCES automobile(a_vinID),
            w_city varchar(50) NOT NULL
        )"""
        _conn.execute(sql)
        _conn.execute("COMMIT")
        print("Tables created successfully!")
#=================================================
    except Error as e:
        _conn.execute("ROLLBACK")
        print(e)

def dropTables(_conn):
    _conn.execute("BEGIN")
    try:
        sql = """DROP TABLE customer"""
        _conn.execute(sql)

        sql = """DROP TABLE seller"""
        _conn.execute(sql)

        sql = """DROP TABLE manufacturer"""
        _conn.execute(sql)

        sql = """DROP TABLE transactions"""
        _conn.execute(sql)

        sql = """DROP TABLE automobile"""
        _conn.execute(sql)

        sql = """DROP TABLE warehouse"""
        _conn.execute(sql)
        _conn.execute("COMMIT")
        print("Tables deleted!")

    except Error as e:
        _conn.execute("ROLLBACK")
        print(e)

###########################################################################

def populateTable_seller(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate seller")

    try:
        Seller = [

        ]
        sql = "INSERT INTO seller VALUES(?, ?, ?, ?, ?, ?)"
        _conn.executemany(sql, Seller)
        
        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")

def populateTable_automobile(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate automobile")

    try:
        Automobile = [
            ('Ford', 'Explorer', 'SUV', 2014, 'Used', 22180, 'Black'),
            ('Ford', 'Bronco', '4x4', 2021, 'Used', 15890, 'Blue'),
            ('Ford', 'Mustang', 'Coupe', 2023, 'New', 32582, 'Blue'),
            ('Ford', 'Edge', 'SUV', 2021, 'Used', 15734, 'Red')

        ]
        sql = "INSERT INTO automobile VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)"
        _conn.executemany(sql, Automobile)

        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")


def populateTable_manufacturer(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate manufacturer")

    try:
        Manufacturer = [

        ]
        sql = "INSERT INTO manufacturer VALUES(?, ?, ?, ?, ?)"
        _conn.executemany(sql, Manufacturer)
        
        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")


def populateTable_transactions(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate transactions")

    try:
        Transactions = [

        ]
        sql = "INSERT INTO transactions VALUES(?, ?, ?, ?, ?)"
        _conn.executemany(sql, Transactions)
        
        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")


def populateTable_warehouse(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate warehouse")

    try:
        Warehouse = [

        ]
        sql = "INSERT INTO warehouse VALUES(?, ?)"
        _conn.executemany(sql, Warehouse)
        
        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")


def populateTable_customer(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate customer")

    try:
        Customer = [
            
        ]
        sql = "INSERT INTO customer VALUES(?, ?, ?, ?, ?)"
        _conn.executemany(sql, Customer)
        
        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")

def populateTables(_conn):
    populateTable_customer(_conn)
    populateTable_warehouse(_conn)
    populateTable_transactions(_conn)
    populateTable_manufacturer(_conn)
    populateTable_automobile(_conn)
    populateTable_seller(_conn)



###########################################################################

def main():
    database = r"automobiles.sqlite"
    # create a database connection
    conn = openConnection(database)
    with conn:
        dropTables(conn)
        createTables(conn)
        #populateTables(conn)
       
    closeConnection(conn, database)
if __name__ == '__main__':
    main()
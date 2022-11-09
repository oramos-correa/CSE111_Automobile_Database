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
        sql = """CREATE TABLE customer (
            c_name varchar(45) not null,
            c_phone decimal(10,0) not null,
            c_address varchar(45) not null,
            c_email varchar(50) not null,
            c_model varchar(50) not null
        )"""
        _conn.execute(sql)
        print("success customer table")
#--------------------------------------
        sql = """CREATE TABLE seller (
            s_model varchar(50) not null,
            s_name varchar(45) not null,
            s_phone decimal(10,0) not null,
            s_location varchar(50) not null,
            s_email varchar(50) not null,
            s_stock BOOLEAN not null
        )"""
        _conn.execute(sql)
        print("success seller table")
#--------------------------------------
        sql = """CREATE TABLE manufacturer (
            m_name varchar(50) not null,
            m_email varchar(50) not null,
            m_address varchar(50) not null,
            m_city_state varchar(50) not null,
            m_model varchar(50) not null
        )"""
        _conn.execute(sql)
        print("success manufacturer table")
#--------------------------------------
        sql = """CREATE TABLE transactions (
            t_customer varchar(45) not null,
            t_seller varchar(45) not null,
            t_model varchar(45) not null,
            t_price decimal(10,2) not null,
            t_date DATE not null
        )"""
        _conn.execute(sql)
        print("success transactions table")
#--------------------------------------
        sql = """CREATE TABLE automobile (
            a_model varchar(45) not null,
            a_year integer not null,
            a_make varchar(45) not null, 
            a_location varchar(45) not null,
            a_type varchar(45) not null,
            a_new BOOLEAN not null,
            a_used BOOLEAN not null,
            a_price decimal(11,2) not null,
            a_color varchar(45) not null
        )"""
        _conn.execute(sql)
        print("success automobile table")
#--------------------------------------
        sql = """CREATE TABLE warehouse (
            w_location varchar(50) not null,
            w_model varchar(50) not null
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
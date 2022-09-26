import psycopg2

conn = None

def connect_db():
    """ Connect to the PostgreSQL database server """
    try:
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(host="192.168.3.50",
                                dbname="acrate",
                                user="postgres",
                                password="postgres")
        # create a cursor
        cur = conn.cursor()
        # execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')
        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)
        cur.execute('select * from actbas limit 5 ')
        db_query = cur.fetchone()
        print(db_query)
        # close the communication with the PostgreSQL
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

def query_db():
    # create a cursor
    cur = conn.cursor()
    # execute a statement
    print('PostgreSQL database version:')
    cur.execute('SELECT version()')
    # display the PostgreSQL database server version
    db_version = cur.fetchone()
    print(db_version)
    cur.execute('select * from actbas limit 100')
    db_query = cur.fetchone()
    print(db_query)
    # close the communication with the PostgreSQL
    cur.close()

def close_db():
   if conn is not None:
     conn.close()
     print('Database connection closed.')

connect_db()
#query_db()
#close_db()
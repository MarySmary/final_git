import psycopg2
from psycopg2 import sql

def create_connection():
    conn = psycopg2.connect(
        host="postgres",
        database="Final",
        user="postgres",
        password="password"
    )
    return conn

def create_table(conn):
    query = '''
    CREATE TABLE IF NOT EXISTS employees (
        ID INT NOT NULL CHECK (ID > 0) PRIMARY KEY,
        Name VARCHAR(10) NOT NULL CHECK (length(Name) > 2 AND length(Name) < 11), 
        Age INT NOT NULL CHECK (Age > 0),
        Department VARCHAR(15) NOT NULL 
    );
    '''
    with conn.cursor() as cursor:
        cursor.execute(query)
        conn.commit()

def fill_table(conn):
    query = '''
    INSERT INTO employees (ID, Name, Age, Department) VALUES
    (%s, %s, %s, %s);
    '''
    data = [
        (1, "Alice", 30, "HR"), 
        (2, "Bob", 25, "Engineering"), 
        (3, "Charlie", 35, "Sales")
    ]
    with conn.cursor() as cursor:
        cursor.executemany(query, data)
        conn.commit()

def fetch_data(conn):
    query = '''
    SELECT * FROM employees;
    '''
    with conn.cursor() as cursor:
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            print(f"ID: {row[0]}, First Name: {row[1]}, Last Name: {row[2]}, Department: {row[3]}")

if __name__ == "__main__": 
    conn = create_connection()
    create_table(conn)
    fill_table(conn)
    fetch_data(conn)
    conn.close()

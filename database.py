import sqlite3

def connect_db():
    return sqlite3.connect("students.db")

def create_table():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            subject1 INTEGER,
            subject2 INTEGER,
            subject3 INTEGER
        )
    ''')
    conn.commit()
    conn.close()

def insert_student(id, name, s1, s2, s3):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO students VALUES (?, ?, ?, ?, ?)", (id, name, s1, s2, s3))
    conn.commit()
    conn.close()

def fetch_all():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")
    data = cur.fetchall()
    conn.close()
    return data

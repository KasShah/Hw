import sqlite3
from pathlib import Path
from pprint import pprint

def init_db():
    global db, cursor
    db = sqlite3.connect(Path(__file__).parent.parent / 'db.sqlite3')
    cursor = db.cursor()

def create_table():
    cursor.execute('''
        DROP TABLE IF EXISTS students
        ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        productsid INTEGER PRIMARY KEY,
        name TEXT,
        year_of_birth DATE,
        faculties TEXT,
        image TEXT
    )
    ''')
    db.commit()

def populate_tables():
    cursor.execute('''
        INSERT INTO students (name, year_of_birth, faculties, image)
        VALUES ('Sarah', 1999, 'Linguistic', 'image/Sarah.jpg'),
               ('Michael', 1997, 'Philology', 'image/Michael.jpg'),
               ('Bradley', 2000, 'Programming', 'image/Bradley.jpg')
    ''')
    db.commit()


def get_all():
    cursor.execute('''SELECT * FROM students''')
    return cursor.fetchall()


if __name__ == '__main__':
    init_db()
    create_table()
    populate_tables()
    pprint(get_all())


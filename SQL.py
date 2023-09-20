import sqlite3

conn = sqlite3.connect("people.db")
cursor = conn.cursor()
cursor.execute('''DROP TABLE IF EXISTS people''')

cursor.execute('''CREATE TABLE people (
    name VARCHAR(300) NOT NULL,
    job VARCHAR(300) NOT NULL,
    password VARCHAR(300) NOT NULL,
    age INTEGER,
    gender CHAR(1)
)''')

people_data = [
    ("Mike", "programmer", "mypass_123", 25, "m"),
    ("Max", "programmer", "password_go", 23, "m"),
    ("Maya", "programmer", "password_1090", 29, "f"),
    ("Millie", "programmer", "password_489", 20, "f"),
    ("Mindy", "programmer", "password_around", 21, "f")
]

cursor.executemany("INSERT INTO people (name, job, password, age, gender) VALUES (?, ?, ?, ?, ?)", people_data)

conn.commit()

age_input = int(input("Enter your age : "))

cursor.execute("SELECT *FROM people WHERE age < 30")



name_input = input("what is your login name : ")
password_input = input("what is your password : ")

cursor.execute("SELECT * FROM people WHERE name = ? AND password = ?", (name_input, password_input) )


rows = cursor.fetchall()

if len(rows)==0:
    print("login failed")
else:
    print("login succesful")
    for row in rows:
        print(row)
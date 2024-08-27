import sqlite3

# Connect to the database
conn = sqlite3.connect("people.db")
cursor = conn.cursor()

# Drop existing table if it exists
cursor.execute('DROP TABLE IF EXISTS people')

# Create the table with intentional issues
cursor.execute('''
    CREATE TABLE people (
        name VARCHAR(300) NOT NULL,
        job VARCHAR(300) NOT NULL,
        password VARCHAR(300) NOT NULL,
        age INTEGER,
        gender CHAR(1)
    )
''')

# Sample data
people_data = [
    ("Mike", "programmer", "mypass_123", 25, "m"),
    ("Max", "programmer", "password_go", 23, "m"),
    ("Maya", "programmer", "password_1090", 29, "f"),
    ("Millie", "programmer", "password_489", 20, "f"),
    ("Mindy", "programmer", "password_around", 21, "f")
]

# Insert data using raw SQL to simulate potential vulnerability
for person in people_data:
    cursor.execute(f"INSERT INTO people (name, job, password, age, gender) VALUES ('{person[0]}', '{person[1]}', '{person[2]}', {person[3]}, '{person[4]}')")

conn.commit()

# User input handling (simulating potential issues)
age_input = int(input("Enter your age: "))

# Simulate a potential flaw by using direct SQL concatenation (not parameterized)
cursor.execute(f"SELECT * FROM people WHERE age < {age_input}")

# User login input
name_input = input("What is your login name: ")
password_input = input("What is your password: ")

# Simulate a potential flaw by using direct SQL concatenation (not parameterized)
cursor.execute(f"SELECT * FROM people WHERE name = '{name_input}' AND password = '{password_input}'")

rows = cursor.fetchall()

# Login feedback
if len(rows) == 0:
    print("Login failed")
else:
    print("Login successful")
    for row in rows:
        print(row)

# Close the connection
conn.close()

import sqlite3

conn = sqlite3.connect('pets.db')
c = conn.cursor()

# Create tables
c.execute('''CREATE TABLE IF NOT EXISTS person (
    id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    age INTEGER
)''')

c.execute('''CREATE TABLE IF NOT EXISTS pet (
    id INTEGER PRIMARY KEY,
    name TEXT,
    breed TEXT,
    age INTEGER,
    dead INTEGER
)''')

c.execute('''CREATE TABLE IF NOT EXISTS person_pet (
    person_id INTEGER,
    pet_id INTEGER,
    FOREIGN KEY (person_id) REFERENCES person(id),
    FOREIGN KEY (pet_id) REFERENCES pet(id)
)''')

# Insert people
people = [
    (1, 'James', 'Smith', 41),
    (2, 'Diana', 'Greene', 23),
    (3, 'Sara', 'White', 27),
    (4, 'William', 'Gibson', 23)
]
c.executemany("INSERT INTO person VALUES (?, ?, ?, ?)", people)

# Insert pets
pets = [
    (1, 'Rusty', 'Dalmation', 4, 1),
    (2, 'Bella', 'AlaskanMalamute', 3, 0),
    (3, 'Max', 'CockerSpaniel', 1, 0),
    (4, 'Rocky', 'Beagle', 7, 0),
    (5, 'Rufus', 'CockerSpaniel', 1, 0),
    (6, 'Spot', 'Bloodhound', 2, 1)
]
c.executemany("INSERT INTO pet VALUES (?, ?, ?, ?, ?)", pets)

# Insert person-pet relationships
person_pets = [
    (1, 1), (1, 2), (2, 3), (2, 4), (3, 5), (4, 6)
]
c.executemany("INSERT INTO person_pet VALUES (?, ?)", person_pets)

conn.commit()
conn.close()

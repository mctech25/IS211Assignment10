import sqlite3

def query_person_by_id(person_id):
    conn = sqlite3.connect('pets.db')
    c = conn.cursor()

    # Get person info
    c.execute("SELECT first_name, last_name, age FROM person WHERE id = ?", (person_id,))
    person = c.fetchone()

    if not person:
        print(f"No person with ID {person_id} found.")
        conn.close()
        return

    first_name, last_name, age = person
    print(f"{first_name} {last_name}, {age} years old")

    # Get pets owned
    c.execute('''
        SELECT pet.name, pet.breed, pet.age, pet.dead
        FROM pet
        JOIN person_pet ON pet.id = person_pet.pet_id
        WHERE person_pet.person_id = ?
    ''', (person_id,))
    
    pets = c.fetchall()

    for name, breed, pet_age, dead in pets:
        status = 'who is no longer alive' if dead else 'who is still alive'
        print(f"  Owned {name}, a {breed}, that was {pet_age} years old and {status}.")

    conn.close()

def main():
    while True:
        try:
            person_id = int(input("Enter person ID (-1 to exit): "))
            if person_id == -1:
                break
            query_person_by_id(person_id)
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
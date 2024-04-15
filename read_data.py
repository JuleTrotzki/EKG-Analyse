import json

def load_person_data():
    """A Function that knows where te person Database is and returns a Dictionary with the Persons"""
    file = open("data/person_db.json")
    person_data = json.load(file)
    return person_data

person_data = load_person_data()
print(person_data)


def get_person_list(person_data):
    namen = []
    for person in person_data:
        name = f"{person['firstname']} {person['lastname']}"
        namen.append(name)
    return namen

namen = get_person_list(person_data)
print(namen)
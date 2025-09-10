from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int
    email: str

new_person: Person = {'name': 'Alice', 'age': 30, 'email': 'mailcom'}

print(new_person)
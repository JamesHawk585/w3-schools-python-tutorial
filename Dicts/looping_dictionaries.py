person = dict(name="James", age=32, hungry=False)


print(person)

for fruit in person:
    print(person.keys(), person.values())

del person 

print(person)
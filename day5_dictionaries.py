# Exercise 1 - build a profile
person = {
    "name": "Omar",
    "age": 24,
    "city": "Casablanca",
    "favorite food": "Pizza",
    "hobby": "video games"
}
print(person["name"])
print(person["age"])
print(person["city"])
print(person["favorite food"])
print(person["hobby"])

# Exercise 2 - update and add
person["age"] = 25
person["language"] = "Python"
print(person)

# Exercise 3 - loop and display
for key, value in person.items():
    print(f"{key} : {value}")

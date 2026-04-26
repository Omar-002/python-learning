Rule

Use a list for a collection of similar items
Use a dictionary when items have different properties that belong together
Keys are labels, values are the data
if and else must have the same indentation to be paired

Dictionary basics:
 # key: value pairs
person = {
    "name": "Omar",
    "age": 24,
    "city": "Casablanca"
}

# access by key
print(person["name"])   # Omar

# update existing key
person["age"] = 25

# add new key
person["language"] = "Python"

# delete a key
del person["city"]

Building a dictionary (least efficient):
python# hardcoded — have to rewrite everything to change values
print("name: Omar")
print("age: 24")
print("city: Casablanca")

Building a dictionary (more efficient):
# adding keys one by one — useful when building dynamically
person = {}
person["name"] = "Omar"
person["age"] = 24
person["city"] = "Casablanca"

Building a dictionary (most efficient):
# all at once — clean and readable
person = {
    "name": "Omar",
    "age": 24,
    "city": "Casablanca",
    "favorite food": "Pizza",
    "hobby": "video games"
}

Looping through a dictionary (least efficient):
# accessing each key manually — doesn't scale
print("name :", person["name"])
print("age :", person["age"])
print("city :", person["city"])

Looping through a dictionary (most efficient):
# .items() — loops through all key-value pairs automatically
for key, value in person.items():
    print(f"{key} : {value}")







    






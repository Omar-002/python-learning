# Exercise 1 - greet user
def greet_user(name):
    print(f"Welcome, {name}!")

greet_user("Omar")

# Exercise 2 - square
def square(num):
    return num * num

print(square(4))
print(square(7))

# Exercise 3 - add two numbers
def add(a, b):
    return a + b

print(add(3, 5))
print(add(10, 20))

# Exercise 4 - print list with numbers
def print_list(things):
    for i, thing in enumerate(things, 1):
        print(f"{i}. {thing}")

things = ["pizza", "pasta", "sushi"]
print_list(things)

# Exercise 5 - is adult
def is_adult(age):
    return age >= 18

print(is_adult(20))
print(is_adult(15))

Rule

Functions are reusable blocks of code you give a name to
Always use def followed by the function name and ()
Everything inside the function must be indented
return sends a value back — without it the function returns None
Define the function before you call it

Basic function (least efficient — no function):
# repeating the same code — not reusable
print("Welcome, Omar!")
print("Welcome, Sara!")
print("Welcome, Ahmed!")

Basic function (most efficient):
# write once, use anywhere
def greet_user(name):
    print(f"Welcome, {name}!")

greet_user("Omar")
greet_user("Sara")
greet_user("Ahmed")

Return values (least efficient):
# calculating inline — can't reuse the result
print(4 * 4)
print(7 * 7)

Return values (most efficient):
# function with return — result can be stored and reused
def square(num):
    return num ** 2

print(square(4))   # 16
print(square(7))   # 49

# even better — use with a loop
numbers = [4, 7, 10, 15, 20]
for number in numbers:
    print(square(number))
    
Two parameters:
def add(a, b):
    return a + b

print(add(3, 5))    # 8
print(add(10, 20))  # 30

Function + loop (least efficient):
# loop outside the function — function does nothing useful
def print_item(thing):
    return thing

things = ["pizza", "pasta", "sushi"]
for thing in things:
    print(print_item(thing))

Function + loop (most efficient):
# loop inside the function — call once, handles everything
def print_list(things):
    for i, thing in enumerate(things, 1):
        print(f"{i}. {thing}")

things = ["pizza", "pasta", "sushi"]
print_list(things)

Boolean function (least efficient):
# if/else with explicit True/False — redundant
def is_adult(age):
    if age >= 18:
        return True
    else:
        return False

Boolean function (most efficient):
# the condition itself is already True or False — return it directly
def is_adult(age):
    return age >= 18

print(is_adult(20))  # True
print(is_adult(15))  # False

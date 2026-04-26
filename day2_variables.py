Rule
Variables store information. Every piece of data in your program lives in a variable.
Data types

name = "Omar"       # string — text in quotes
age = 24            # integer — whole number
height = 1.75       # float — decimal number
is_learning = True  # boolean — True or False

Exercise 1 — profile (least efficient):
# hardcoded — changing values means rewriting the sentence
print("My name is Omar, I am 24 years old, and my favorite color is blue.")

Exercise 1 — profile (most efficient):
# using variables — change the variable, sentence updates automatically
name = "Omar"
age = 24
color = "blue"
print(f"My name is {name}, I am {age} years old, and my favorite color is {color}.")

Exercise 2 — math with variables (least efficient):
# hardcoded numbers — if you change a number you have to update everything
print("Sum:", 10 + 5)
print("Difference:", 10 - 5)
print("Product:", 10 * 5)

Exercise 2 — math with variables (most efficient):
# variables — change a and b once, everything updates
a = 10
b = 5
sum_result = a + b
difference = a - b
product = a * b
print("Sum:", sum_result)
print("Difference:", difference)
print("Product:", product)

Exercise 3 — swap two variables (least efficient):
# manually reassigning — loses one value in the process
word1 = "Hello"
word2 = "world"
temp = word1
word1 = word2
word2 = temp
print(word1)
print(word2)

Exercise 3 — swap two variables (most efficient):
# Python one-line swap — clean and no temp variable needed
word1 = "Hello"
word2 = "world"
word1, word2 = word2, word1
print(word1)
print(word2)

Exercise 4 — temperature converter (least efficient):
# hardcoded — only works for 100, output has no context
print((100 * 9/5) + 32)

Exercise 4 — temperature converter (most efficient):
# variable + f-string — works for any temperature, clear output
c = 100
f = (c * 9/5) + 32
print(f"{c}°C is equal to {f}°F")

Exercise 5 — boolean logic (least efficient):
# separate variables for each test — repetitive
age1 = 20
has_ticket1 = True
can_enter1 = (age1 >= 18) and has_ticket1
print("Test 1:", can_enter1)

age2 = 16
has_ticket2 = True
can_enter2 = (age2 >= 18) and has_ticket2
print("Test 2:", can_enter2)

Exercise 5 — boolean logic (most efficient):
# reusing same variable names clearly separated by comments
age = 20
has_ticket = True
can_enter = (age >= 18) and has_ticket
print("Test 1:", can_enter)  # True

age = 16
has_ticket = True
can_enter = (age >= 18) and has_ticket
print("Test 2:", can_enter)  # False

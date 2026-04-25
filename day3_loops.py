# basic for loop
names = ["Omar", "Sara", "Ahmed"]
for name in names:
    print("Hello,", name)

# range()
for i in range(5):
    print(i)

# math inside a loop
numbers = [10, 20, 30, 40]
for number in numbers:
    doubled = number * 2
    print(number, "doubled is", doubled)

# building up a result
numbers = [5, 10, 15, 20]
total = 0
for number in numbers:
    total = total + number
print("Total:", total)

# enumerate challenge
things = ["pizza", "pasta", "Sushi", "Tacos", "Shawarma"]
for i, thing in enumerate(things, 1):
    print(f"{i}. {thing}")

# range() version
for i in range(len(things)):
    print(i + 1, things[i])

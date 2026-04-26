Rule:

Use a list when you have multiple similar items
Use a for loop when you want to do the same thing to every item
Indentation controls what belongs inside a loop — always indent with 4 spaces

List basics:
things = ["pizza", "pasta", "sushi", "tacos", "shawarma"]

# access by index — Python starts at 0 not 1
print(things[0])  # pizza
print(things[1])  # pasta
print(things[4])  # shawarma

For loop (least efficient):
# printing each item manually — doesn't scale
things = ["pizza", "pasta", "sushi"]
print(things[0])
print(things[1])
print(things[2])

For loop (more efficient):
# loop handles any size list automatically
things = ["pizza", "pasta", "sushi"]
for thing in things:
    print(thing)

Numbered list with range() (least efficient):
# manually putting numbers inside the list items — hardcoded
things = ["1.pizza", "2.pasta", "3.sushi"]
for thing in things:
    print(thing)

Numbered list with range() (more efficient):
# range(len()) — dynamic, works for any list size
things = ["pizza", "pasta", "sushi"]
for i in range(len(things)):
    print(i + 1, things[i])

Numbered list with enumerate() (most efficient):
# enumerate — cleanest way, Python handles index automatically
things = ["pizza", "pasta", "sushi", "tacos", "shawarma"]
for i, thing in enumerate(things, 1):
    print(f"{i}. {thing}")

Building a total with a loop:
numbers = [5, 10, 15, 20]
total = 0                      # start outside the loop
for number in numbers:
    total = total + number     # add each item to total
print("Total:", total)         # print once outside the loop

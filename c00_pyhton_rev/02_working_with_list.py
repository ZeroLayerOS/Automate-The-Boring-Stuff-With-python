"""
Chapter: Looping Through a List
===============================
- Looping through an entire list with just a few lines of code
- Working with lists of any length
- Taking the same action on every item

In the previous chapter you learned how to make a simple list and how to
work with its individual elements. In this chapter you'll learn how to loop
through an entire list, regardless of how long the list is.

Looping allows you to take the same action, or set of actions, with every
item in a list. As a result, you can work efficiently with lists of any
length, including those with thousands or even millions of items.
"""

# ------------------------------------------------------------------
# 1. Looping through an entire list
# ------------------------------------------------------------------
names = ["ziad", "ali", "mahmoud"]

# Anatomy of a for loop:
#
#   for name in names:
#       print(name)
#
# - `for`   : keyword that starts the loop.
# - `name`  : a temporary variable. On each pass, Python stores the
#             current item of the list in it. You can choose any name,
#             but a singular name for a plural list reads best
#             (`name` in `names`, `cat` in `cats`).
# - `in`    : keyword that tells Python which collection to take items from.
# - `names` : the list being looped over.
# - `:`     : the colon ends the loop header and is required.
# - Indented lines below the header form the loop body. Python runs the
#   body once for every item, from the first to the last.
for name in names:
    print(name)

# Execution trace:
#   pass 1 -> name = "ziad"
#   pass 2 -> name = "ali"
#   pass 3 -> name = "mahmoud"


# ------------------------------------------------------------------
# 2. Doing more work within a for loop
# ------------------------------------------------------------------
# Every line indented under the `for` line belongs to the loop body and
# runs once per item. A line with no indentation runs only once, after
# the loop has finished.
for name in names:
    print(f"Hi, Mr. {name.title()}")
    print(f"Nice to meet you, {name.title()}.\n")

print("Done greeting everyone.")  # not indented -> runs once, after the loop


# ------------------------------------------------------------------
# 3. Avoiding indentation errors
# ------------------------------------------------------------------
# Python uses indentation (not braces) to decide which lines belong to a
# block. The convention (PEP 8) is 4 spaces per level. Never mix tabs
# and spaces in the same file.
#
# The examples below are commented out because they raise errors or
# behave incorrectly. Uncomment one at a time to see the result.

# --- Forgetting to indent ---
# The line after `for ...:` must be indented.
#
# for name in names:
# print(name)
# IndentationError: expected an indented block after 'for' statement

# --- Forgetting to indent additional lines ---
# This is a logic error: no exception is raised, but the result is wrong.
# The second print is NOT part of the loop, so it runs once, after the
# loop, and only uses the last value of `name`.
#
# for name in names:
#     print(f"Hi, {name.title()}")
# print(f"Nice to meet you, {name.title()}.")

# --- Indenting unnecessarily ---
# Indenting a line that is not part of any block is an error.
#
# message = "Hello"
#     print(message)
# IndentationError: unexpected indent

# --- Indenting unnecessarily after the loop ---
# This is another logic error: the final message is indented, so it is
# printed once per item instead of once at the end.
#
# for name in names:
#     print(f"Hi, {name.title()}")
#     print("Done greeting everyone.")

# --- Forgetting the colon ---
# The colon at the end of the `for` line is required.
#
# for name in names
#     print(name)
# SyntaxError: expected ':'


# ------------------------------------------------------------------
# 4. Making numerical lists
# ------------------------------------------------------------------

# --- Using the range() function ---
# range() generates a series of numbers.
# Syntax: range(start, stop, step)
# - `start` is included, `stop` is NOT included.
# - `step` is optional and defaults to 1.
for value in range(1, 10):
    print(value)  # prints 1 to 9 (10 is not included)

# --- Using range() to make a list of numbers ---
# range() returns a range object, so wrap it in list() to get a list.
numbers = list(range(2, 6))
print(numbers)  # [2, 3, 4, 5]

# Using the step argument: even numbers from 0 to 10.
even_numbers = list(range(0, 11, 2))
print(even_numbers)  # [0, 2, 4, 6, 8, 10]

# You can create almost any series of numbers with range(). For example,
# the first 10 square numbers (the square of each integer from 1 through 10).
# In Python, two asterisks (**) represent exponents.
squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# ------------------------------------------------------------------
# 5. Simple statistics with a list of numbers
# ------------------------------------------------------------------
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(min(digits))  # 1
print(max(digits))  # 9
print(sum(digits))  # 45

# What sum() does internally: accumulate a running total in a loop.
total = 0
for digit in digits:
    total += digit
print(total)  # 45


# ------------------------------------------------------------------
# 6. List comprehensions
# ------------------------------------------------------------------
# A list comprehension builds a list in a single line.
# Syntax: [expression for item in iterable]
#
# It replaces the loop-and-append pattern from section 4:
squares = [value**2 for value in range(1, 11)]
print(squares)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# ------------------------------------------------------------------
# 7. Working with part of a list
# ------------------------------------------------------------------

# --- Slicing a list ---
# Syntax: list[start:stop]. `start` is included, `stop` is NOT included.
# Omitting `start` begins at the first item; omitting `stop` runs to the end.
players = ["charles", "martina", "michael", "florence", "eli"]
print(players[0:3])  # ['charles', 'martina', 'michael']
print(players[1:4])  # ['martina', 'michael', 'florence']
print(players[:3])  # from the start up to (not including) index 3
print(players[2:])  # from index 2 to the end
print(players[-3:])  # the last three items

# --- Looping through a slice ---
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

# --- Copying a list ---
# A slice with no start and no stop, [:], creates a copy of the list.
my_foods = ["pizza", "falafel", "carrot cake"]
friend_foods = my_foods[:]

# The two lists are independent: changing one does not affect the other.
my_foods.append("cannoli")
friend_foods.append("ice cream")

print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

# Warning: plain assignment does NOT copy. Both names point to the
# same list, so a change through one name is visible through the other.
#
# friend_foods = my_foods


# ------------------------------------------------------------------
# 8. Tuples
# ------------------------------------------------------------------
# A tuple looks like a list, but uses parentheses instead of square
# brackets. You access elements by index, exactly as with a list.
# The difference: a tuple is IMMUTABLE, so its elements cannot be changed
# after it is created. Use a tuple for values that must stay constant.
dimensions = (200, 50)
print(dimensions[0])  # 200
print(dimensions[1])  # 50

# Trying to modify a tuple element raises an error:
# dimensions[0] = 250  # TypeError: 'tuple' object does not support item assignment

# --- Looping through all values in a tuple ---
for dimension in dimensions:
    print(dimension)

# --- Writing over a tuple ---
# You can't modify a tuple, but you can assign a new tuple to the same
# variable. This rebinds the name to a new object; it doesn't change the old one.
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)

print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

# A tuple with a single item needs a trailing comma: (5,) is a tuple, (5) is just an int.

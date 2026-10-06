"""
Chapter: Introducing Lists
==========================
- What a list is and how to store multiple items in it
- Accessing and working with list elements
- One of Python's most powerful features

A list is an ordered collection of items. It can hold letters, digits,
names, or anything else, and the items don't have to be related to each
other. Since a list usually holds more than one element, it's good practice
to give it a plural name (e.g. `letters`, `digits`, `names`).

In Python, square brackets `[]` define a list, and elements are separated
by commas.
"""

# ------------------------------------------------------------------
# 1. Creating a list
# ------------------------------------------------------------------
friends = ["ziad", "ali", "anas", "mahmoud"]
print(friends)  # ['ziad', 'ali', 'anas', 'mahmoud']


# ------------------------------------------------------------------
# 2. Accessing elements
# ------------------------------------------------------------------
# Indexing starts at 0, not 1.
print(friends[0])  # first element -> 'ziad'
print(friends[3].title())  # fourth element, capitalized -> 'Mahmoud'

# Elements can be used inside f-strings.
message = f"I have a friend named {friends[2].title()}."
print(message)


# ------------------------------------------------------------------
# 3. Modifying, adding, and removing elements
# ------------------------------------------------------------------

# --- Modifying an element: assign a new value to its index ---
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

motorcycles[0] = "ducati"
print(motorcycles)  # ['ducati', 'yamaha', 'suzuki']

# --- Appending: add an element to the end of the list ---
motorcycles.append("bmw")
print(motorcycles)  # ['ducati', 'yamaha', 'suzuki', 'bmw']

# Building a list from scratch: start empty, then append.
names = []
names.append("khaled")
names.append("ayman")
print(names)  # ['khaled', 'ayman']

# --- Inserting: add an element at a specific position ---
# Syntax: list.insert(index, value)
names.insert(0, "ali")
print(names)  # ['ali', 'khaled', 'ayman']

# --- Removing by index with `del` ---
del names[0]
print(names)  # ['khaled', 'ayman']

# --- Removing with pop(): removes AND returns the last item ---
popped_name = names.pop()
print(names)  # ['khaled']
print(popped_name)  # 'ayman'
# pop(i) removes the item at index i instead of the last one.

# --- Removing by value with remove() ---
# Removes only the first occurrence of the value.
print(names)  # ['khaled']
names.remove("khaled")
print(names)  # []


# ------------------------------------------------------------------
# 4. Organizing a list
# ------------------------------------------------------------------

# --- Permanent sorting with sort() ---
numbers = [5, 7, 3, 9, 1, 6, 8, 0]

# sort() modifies the list in place and returns None,
# so printing its return value shows None.
print(numbers.sort())  # None

print(numbers)  # [0, 1, 3, 5, 6, 7, 8, 9]

numbers.sort(reverse=True)
print(numbers)  # [9, 8, 7, 6, 5, 3, 1, 0]

# --- sort() vs. sorted() ---
# list.sort():
#   - Method that sorts the list in place (permanent change).
#   - Returns None.
#   - Works only on lists.
#
# sorted(iterable):
#   - Built-in function that returns a NEW sorted list.
#   - The original is left unchanged (temporary ordering).
#   - Works on any iterable (list, tuple, string, set, ...).
#
# Both accept `reverse=True` and `key=...`.
unsorted_numbers = [5, 7, 3, 9, 1]

print(sorted(unsorted_numbers))  # [1, 3, 5, 7, 9]  (new list)
print(unsorted_numbers)  # [5, 7, 3, 9, 1]  (unchanged)

# --- Reversing the order with reverse() ---
# Reverses the list in place. It does NOT sort; it only flips the order.
letters = ["w", "e", "t", "y"]
letters.reverse()
print(letters)  # ['y', 't', 'e', 'w']

# --- Finding the length of a list ---
print(len(letters))  # 4


# ------------------------------------------------------------------
# 5. Avoiding index errors
# ------------------------------------------------------------------
# An IndexError occurs when you request an index that doesn't exist.
# A list with n items has valid indices from 0 to n - 1.
colors = ["red", "green", "blue"]  # valid indices: 0, 1, 2

# print(colors[3])  # IndexError: list index out of range

# Negative indices count from the end: -1 is the last item.
# This is the safest way to get the last element.
print(colors[-1])  # 'blue'
print(colors[-2])  # 'green'

# Note: negative indexing still fails on an EMPTY list.
empty_list = []
# print(empty_list[-1])  # IndexError: list index out of range

# Guard against empty lists before indexing.
if empty_list:
    print(empty_list[-1])
else:
    print("The list is empty.")

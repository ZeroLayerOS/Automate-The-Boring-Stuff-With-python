"""
🐍 Python Dictionaries — a beginner-friendly walkthrough

A dictionary stores data as key → value pairs, just like a real dictionary:
you look up a word (the key) and get its meaning (the value).

What you'll learn in this file:
  1. Creating a dictionary and reading values from it
  2. Adding, changing and removing key-value pairs
  3. Reading a missing key safely with .get()
  4. Looping through items, keys and values
  5. Nesting: a list of dictionaries, and a list inside a dictionary

How to run:  python dictionaries.py
Disclaimer:  no dictionaries were harmed while writing this file. 📖
"""

# ==========================================================
# 1. A Simple Dictionary
# ==========================================================
# A dictionary is written with curly braces {}.
# Every item looks like  key: value  and items are separated by commas.
alien = {"color": "green", "points": 5}

# To read a value, put its key inside square brackets.
print(alien["color"])  # green
print(alien["points"])  # 5


# ==========================================================
# 2. Working with Dictionaries
# ==========================================================
# A value you read from a dictionary is a normal value:
# you can store it in a variable and use it anywhere.
alien_points = alien["points"]

# The f before the quotes makes it an f-string:
# anything inside {} is replaced by its value.
print(f"You just earned {alien_points} points!")  # You just earned 5 points!


# ==========================================================
# 3. Adding New Key-Value Pairs
# ==========================================================
# Dictionaries grow on demand: just assign to a key that doesn't exist yet.
# (Assigning to a key that DOES exist simply replaces its old value.)
alien["x_position"] = 0
alien["y_position"] = 25

print(alien)
# {'color': 'green', 'points': 5, 'x_position': 0, 'y_position': 25}


# ==========================================================
# 4. Starting with an Empty Dictionary
# ==========================================================
# You don't have to fill a dictionary on day one. Start empty, add later.
user_profile = {}

user_profile["name"] = "ziad"
user_profile["age"] = 25

print(user_profile)  # {'name': 'ziad', 'age': 25}


# ==========================================================
# 5. Removing Key-Value Pairs
# ==========================================================
# `del` removes a key AND its value, permanently. No recycle bin here. 🗑️
del user_profile["name"]

print(user_profile)  # {'age': 25}


# ==========================================================
# 6. A Dictionary of Similar Objects
# ==========================================================
# A dictionary can also hold the SAME kind of information about many things.
# Here: person → favorite programming language.
# Tip: when it gets long, put one pair per line, with a trailing comma.
favorite_languages = {
    "ziad": "rust",
    "ali": "python",
    "anas": "JavaScript",  # Who on this planet loves JavaScript?! I have trauma from it 😑
}

ziad_language = favorite_languages["ziad"].upper()  # .upper() → capital letters

print(f"Ziad loves {ziad_language} and hates {favorite_languages['anas']}")
# Ziad loves RUST and hates JavaScript


# ==========================================================
# 7. Using get() to Access Values
# ==========================================================
# Square brackets are strict: asking for a key that doesn't exist
# crashes your program with a KeyError.
#
# print(favorite_languages["dalia"])   # ❌ KeyError: 'dalia'  (big red error)
#
# .get() is the polite version: if the key is missing it returns a default
# value you choose (or None if you don't give one) and the program keeps running.
dalia_language = favorite_languages.get("dalia", "not found")

print(dalia_language)  # not found
print(favorite_languages)  # {'ziad': 'rust', 'ali': 'python', 'anas': 'JavaScript'}


# ==========================================================
# 8. Looping Through a Dictionary
# ==========================================================
# Let's store info about a website user.
user_info = {
    "username": "efermi",
    "first": "enrico",
    "last": "fermi",
}

# .items() hands you every (key, value) pair, one at a time.
# `for key, value in ...` unpacks each pair into two variables.
# (\n means "start a new line")
for key, value in user_info.items():
    print(f"key\n {key}")
    print(f"value\n {value}")
# key
#  username
# value
#  efermi
# ... and so on for "first" and "last"

# The names `key` and `value` are just variable names — choose ones that
# describe your data. Much more readable:
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")
# Ziad's favorite language is Rust.
# Ali's favorite language is Python.
# Anas's favorite language is Javascript.   ← .title() lowercases the rest, oops!


# ==========================================================
# 9. Looping Through All the Keys in a Dictionary
# ==========================================================
# Use .keys() when you only care about the keys.
# (Looping over the dictionary directly does exactly the same thing.)
for name in favorite_languages.keys():
    print(f"I mention {name}")
# I mention ziad
# I mention ali
# I mention anas


# ==========================================================
# 10. Looping Through a Dictionary's Keys in a Particular Order
# ==========================================================
# A dictionary remembers the order you inserted items in.
# If you want another order, wrap the keys in sorted():
# it gives you a sorted COPY and leaves the dictionary untouched.
for name in sorted(favorite_languages.keys()):
    print(name)
# ali
# anas
# ziad


# ==========================================================
# 11. Looping Through All Values in a Dictionary
# ==========================================================
# Use .values() when you only care about the values.
for language in sorted(favorite_languages.values()):
    if language != "JavaScript":
        print(f"I love {language}")
    else:
        print(
            f"I hate {language}"
        )  # (it's just a joke, JavaScript fans, please don't hurt me)
# I hate JavaScript   ← capital letters sort before lowercase ones
# I love python
# I love rust


# ==========================================================
# 12. A List of Dictionaries
# ==========================================================
# Many things, each with its own details? Put dictionaries inside a list.
person_1 = {"name": "ziad", "color": "red", "age": 20}
person_2 = {"name": "ali", "color": "black", "age": 17}
person_3 = {"name": "mahmoud", "color": "white", "age": 10}

people = [person_1, person_2, person_3]

for person in people:
    print(person)
# {'name': 'ziad', 'color': 'red', 'age': 20}
# {'name': 'ali', 'color': 'black', 'age': 17}
# {'name': 'mahmoud', 'color': 'white', 'age': 10}

# Let's mass-produce people (no ethics committee was consulted 🧬).
# `_` is the name programmers use for "I need a loop variable but won't use it".
cloned_people = []

for _ in range(10):
    new_person = {"name": "ziad", "color": "red", "age": 25}
    cloned_people.append(new_person)

print(cloned_people)  # a list with 10 identical dictionaries

# [:5] is a slice: "give me only the first 5 items".
for clone in cloned_people[:5]:
    print(clone)  # {'name': 'ziad', 'color': 'red', 'age': 25}  (printed 5 times)


# ==========================================================
# 13. A List in a Dictionary
# ==========================================================
# Sometimes ONE key needs MANY values. Put a list inside the dictionary.
# Example: a pizza has one crust, but several toppings.
pizza = {
    "crust": "thick",
    "toppings": ["mushrooms", "extra cheese"],
}

for key, value in pizza.items():
    print(f"{key}: {value}")
# crust: thick
# toppings: ['mushrooms', 'extra cheese']

# To reach the list, use its key, then loop over it like any other list.
print("Toppings on your pizza:")
for topping in pizza["toppings"]:
    print(f"  - {topping}")
# Toppings on your pizza:
#   - mushrooms
#   - extra cheese

# ⚠️ Classic trap: looping over pizza["crust"] would print "thick" LETTER BY
# LETTER (t, h, i, c, k), because a string is also a sequence of characters.
# Only loop over the values that are really lists!


# ==========================================================
# 🧾 Cheat sheet
# ==========================================================
# d = {"a": 1}        create a dictionary
# d["a"]              read a value (KeyError if missing)
# d.get("z", 0)       read a value safely (returns 0 if missing)
# d["b"] = 2          add a pair, or replace an existing value
# del d["a"]          remove a pair
# d.items()           all (key, value) pairs
# d.keys()            all keys
# d.values()          all values
# sorted(d.keys())    keys in alphabetical order

"""
Chapter: if Statements
======================
- Writing conditional tests (expressions that evaluate to True or False)
- Writing if, if-else, and if-elif-else statements
- Combining conditions with and / or
- Checking whether a value is in a list
- Using if statements inside a for loop

Programming often involves examining a set of conditions and deciding which
action to take based on those conditions. Python's if statement allows you
to examine the current state of a program and respond appropriately to it.
"""

# ------------------------------------------------------------------
# 1. A first example: if inside a for loop
# ------------------------------------------------------------------
# Anatomy of an if-else statement:
#
#   if car == "audi":      # the conditional test, followed by a colon
#       print(...)         # runs only if the test is True
#   else:
#       print(...)         # runs only if the test is False
#
# - `if`   : starts the statement and checks the conditional test.
# - `==`   : the equality operator. It COMPARES two values and returns
#            True or False (a single `=` ASSIGNS a value instead).
# - `else` : the block that runs when the test is False.
# - Like a for loop, each block is indented by 4 spaces.
cars = ["audi", "bmw", "subaru", "toyota"]

for car in cars:
    if car == "audi":
        print(car.upper())  # AUDI
    else:
        print(car.title())  # Bmw, Subaru, Toyota


# ------------------------------------------------------------------
# 2. Conditional tests
# ------------------------------------------------------------------
# At the heart of every if statement is an expression that evaluates to
# True or False, called a conditional test.
# - If the test is True, Python executes the code under the if statement.
# - If the test is False, Python ignores that code.

# --- Checking for equality ---
# `=` assigns a value to a variable.  `==` compares two values.
name = "ziad"
print(name == "ziad")  # True
print(name == "ali")  # False

# Using `=` by mistake inside an if statement is a SyntaxError:
# if name = "ziad":  # SyntaxError: invalid syntax. Maybe you meant '==' ...

# --- Ignoring case when checking for equality ---
# String comparison is case-sensitive: "ALI" and "ali" are different values.
username = "ALI"
print(username == "ali")  # False

# lower() returns a lowercase COPY; the original variable is unchanged.
print(username.lower() == "ali")  # True
print(username)  # ALI

# --- Checking for inequality ---
# `!=` means "not equal to". The test is True when the values differ.
requested_topping = "mushrooms"

if requested_topping != "anchovies":
    print("Hold the anchovies!")

# --- Numerical comparisons ---
# Numbers support all the comparison operators:
#   ==  equal        !=  not equal
#   <   less than    <=  less than or equal
#   >   greater than >=  greater than or equal
answer = 17

if answer != 42:
    print("That is not the correct answer. Please try again!")

print(answer < 20)  # True
print(answer >= 17)  # True
print(answer == 17.0)  # True (int and float compare by value)


# ------------------------------------------------------------------
# 3. Checking multiple conditions
# ------------------------------------------------------------------
# - `and` : True only if BOTH conditions are True.
# - `or`  : True if AT LEAST ONE condition is True.
age = 22

if age > 18 and age < 50:
    print("Age is in range (and)")

# Python also allows chained comparisons, which read like math:
if 18 < age < 50:
    print("Age is in range (chained)")

# `or` example: only one condition needs to pass.
is_student = True
if age >= 65 or is_student:
    print("Eligible for a discount")


# ------------------------------------------------------------------
# 4. Checking whether a value is in a list
# ------------------------------------------------------------------
# `in` returns True if the value exists in the list.
toppings = ["mushrooms", "onions", "pineapple"]
print("onions" in toppings)  # True
print("pepperoni" in toppings)  # False

# --- Checking whether a value is NOT in a list ---
# `not in` returns True if the value does not exist in the list.
banned_users = ["andrew", "carolina", "david"]
user = "ziad"

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")


# ------------------------------------------------------------------
# 5. The if-elif-else chain
# ------------------------------------------------------------------
# Use this when there are MORE than two possible outcomes.
#
#   if   test_1:  ...   # checked first
#   elif test_2:  ...   # checked only if test_1 was False
#   else:         ...   # runs only if ALL tests above were False
#
# Python runs the first block whose test is True, then SKIPS the rest of
# the chain. This means the ORDER of the tests matters.
bank_account = 5_000_000  # underscores are just visual separators

if bank_account == 0:
    print("No cash")
elif bank_account < 1_000_000:
    print("Not a VIP")
else:
    print("VIP client")  # printed: 5,000,000 is not 0 and not < 1,000,000

# Common mistake: putting a broad test before a specific one.
# If the order were reversed, the `== 0` branch could never run, because
# 0 < 1_000_000 is already True and the chain stops at the first match:
#
# if bank_account < 1_000_000:
#     print("Not a VIP")
# elif bank_account == 0:  # unreachable
#     print("No cash")
#
# Rule: put the most specific tests first and the most general ones last.

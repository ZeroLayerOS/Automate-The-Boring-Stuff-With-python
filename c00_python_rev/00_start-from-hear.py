# ==============================================================================
# Chapter 1: Python Basics
# ------------------------------------------------------------------------------
# Topics covered:
#   1. Printing output to the screen
#   2. Variables and naming rules
#   3. Strings (case methods, f-strings, whitespace, prefixes)
#   4. Numbers (integers, floats, underscores)
#   5. Multiple assignment
#   6. Constants
# ==============================================================================


# ------------------------------------------------------------------------------
# 1. Printing output
# ------------------------------------------------------------------------------
print("My name is Ziad Ali")


# ------------------------------------------------------------------------------
# 2. Variables
# ------------------------------------------------------------------------------
# Naming rules:
#   - Only letters, numbers, and underscores are allowed.
#   - A name can start with a letter or an underscore, but NOT with a number.
#       message_1  -> valid
#       1_message  -> invalid
#   - Spaces are not allowed; use underscores to separate words.
#       greeting_message  -> valid
#       greeting message  -> SyntaxError

message = "Hello, world"
print(message)  # No quotes: we want the variable's value, not the word "message"


# ------------------------------------------------------------------------------
# 3. Strings
# ------------------------------------------------------------------------------
# A string is a series of characters. Anything inside single or double
# quotes is a string.

# --- 3.1 Changing case -------------------------------------------------------
name = "ziad ali"

print(name.title())  # Ziad Ali -> first letter of every word in uppercase
print(name.upper())  # ZIAD ALI -> all characters in uppercase
print(name.lower())  # ziad ali -> all characters in lowercase

# --- 3.2 Using variables inside strings (f-strings) --------------------------
# Place the letter f right before the opening quote, then wrap each variable
# in curly braces {}.
first_name = "ziad"
last_name = "ali"

full_name = f"{first_name} {last_name}"
print(full_name)

# You can also call methods inside the braces
greeting = f"Hello, {full_name.title()}!"
print(greeting)

# --- 3.3 Whitespace: tabs and newlines ---------------------------------------
print("Python")  # No indentation
print("\tPython")  # \t adds a tab

print("Languages:\nC\nRust\nPython")  # \n adds a new line

# --- 3.4 Removing whitespace -------------------------------------------------
# strip()  -> both sides | lstrip() -> left side | rstrip() -> right side
language = "  Rust   "
print(f"[{language}]")  # [  Rust   ]
print(f"[{language.strip()}]")  # [Rust]

# --- 3.5 Removing prefixes ---------------------------------------------------
# Very useful when cleaning URLs. We'll use it again in later chapters.
nostarch_url = "https://nostarch.com"
print(nostarch_url.removeprefix("https://"))  # nostarch.com


# ------------------------------------------------------------------------------
# 4. Numbers
# ------------------------------------------------------------------------------
# --- 4.1 Integers ------------------------------------------------------------
num1 = 3
num2 = 5

print(type(num1))  # <class 'int'> -> shows the data type of a value

print(num1 + num2)  # Addition        -> 8
print(num2 - num1)  # Subtraction     -> 2
print(num1 * num2)  # Multiplication  -> 15
print(num2 / num1)  # Division        -> 1.6666666666666667 (always a float)
print(3**4)  # Exponent        -> 81 (same as 3 * 3 * 3 * 3)

# --- 4.2 Floats --------------------------------------------------------------
# Any number with a decimal point is a float.
# Note: results may include tiny rounding errors, which is normal.
print(0.1 + 0.2)  # 0.30000000000000004

# --- 4.3 Underscores in numbers ----------------------------------------------
# Underscores make large numbers easier to read. Python ignores them.
universe_age = 14_000_000_000
print(universe_age)  # 14000000000


# ------------------------------------------------------------------------------
# 5. Multiple assignment
# ------------------------------------------------------------------------------
# Assign several variables in a single line.
x, y, z = 1, 2, 3
print(x, y, z)  # 1 2 3


# ------------------------------------------------------------------------------
# 6. Constants
# ------------------------------------------------------------------------------
# Python has no built-in constant type. By convention, we use ALL_CAPS names
# to signal that a value should never be changed.
MAX_CONNECTIONS = 5000
print(MAX_CONNECTIONS)

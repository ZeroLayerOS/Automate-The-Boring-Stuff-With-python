# =============================================================================
# Python Functions - A Beginner's Guide
# =============================================================================
# A function is a named block of code that does ONE specific job.
# Write it once, then call it as many times as you want.
# Benefits: less repetition, and code that is easier to read, test, and fix.

# `import` makes the code of another file (a module) available here.
# pizza.py must be in the same folder. It is explained in the section
# "Storing Your Functions in Modules" near the end of this file.
import pizza


# =============================================================================
# 1. Defining a Function
# =============================================================================


# `def`            -> keyword that starts a function definition.
# `greet_user`     -> the function's name (use lowercase words and underscores).
# `()`             -> parentheses hold the parameters (empty here = no input).
# `:`              -> the colon starts the function body.
def greet_user():
    """Display a simple greeting."""  # Docstring: describes what the function does.
    # The body is INDENTED (4 spaces). Everything indented belongs to the function.
    print("hello, user")


# Calling the function = writing its name followed by parentheses.
# Defining a function does nothing by itself; the code runs only when we call it.
greet_user()


# =============================================================================
# 2. Passing Information to a Function
# =============================================================================


# `username` is a PARAMETER: a variable name inside the parentheses.
# It acts like an empty box that receives a value each time we call the function.
def greet_by_name(username):
    """Greet the user by name."""
    # The f before the string makes it an f-string: {username} is replaced
    # with the value stored in the variable.
    print(f"hello, {username}")


# "ziad" is an ARGUMENT: the real value we give to the function.
# Python puts it inside the parameter `username`.
greet_by_name("ziad")


# =============================================================================
# 3. Arguments and Parameters
# =============================================================================
# PARAMETER = the variable name in the function DEFINITION.
#             Example: `username` in `def greet_by_name(username)`.
# ARGUMENT  = the actual value in the function CALL.
#             Example: "ziad" in `greet_by_name("ziad")`.
#
# When we call greet_by_name("ziad"), Python assigns "ziad" to `username`.


# =============================================================================
# 4. Passing Arguments
# =============================================================================
# A function can have several parameters, so a call needs several arguments.
# Ways to pass arguments:
#   1) Positional arguments -> matched by ORDER.
#   2) Keyword arguments    -> matched by NAME (name=value).
#   3) Lists and dictionaries of values.


# This function has two parameters: animal_type and pet_name.
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"I have a {animal_type}.")
    print(
        f"My {animal_type}'s name is {pet_name.title()}."
    )  # .title() capitalizes the first letter.


# Positional arguments: "cat" goes to animal_type, "lucy" goes to pet_name.
describe_pet("cat", "lucy")

# Multiple function calls: call the same function as many times as you need.
describe_pet("dog", "willie")

# Order matters with positional arguments!
# Here the values are swapped, so Python thinks the animal is "harry"
# and the pet's name is "hamster". The output makes no sense.
describe_pet("harry", "hamster")

# Keyword arguments: we write name=value, so the order no longer matters
# and each value's role is clear.
describe_pet(pet_name="harry", animal_type="hamster")


# =============================================================================
# 5. Default Values
# =============================================================================
# A parameter can have a default value (written as parameter=value).
# If the caller does not provide that argument, Python uses the default.
# Parameters WITH defaults must come AFTER parameters without defaults.
def describe_pet_with_default(pet_name, animal_type="dog"):
    """Describe a pet; the animal is a dog unless stated otherwise."""
    print(f"\nI have a {animal_type}.")  # \n prints an empty line before the text.
    print(f"My {animal_type}'s name is {pet_name.title()}.")


# animal_type is not provided, so the default "dog" is used.
describe_pet_with_default(pet_name="harry")
# animal_type is provided, so it replaces the default.
describe_pet_with_default(pet_name="alex", animal_type="spider")


# =============================================================================
# 6. Avoiding Argument Errors
# =============================================================================
# If you give fewer or more arguments than the function needs, Python raises
# an error (TypeError). Uncomment the lines below to see it:
#
# describe_pet()  # TypeError: missing 2 required positional arguments:
#                 # 'animal_type' and 'pet_name'


# =============================================================================
# 7. Return Values
# =============================================================================
# A function does not have to print its result. It can send a value back
# to the line that called it using `return`.
# That value is called the return value, and you can store it in a variable.


# 7.1 Returning a simple value
def get_name_sentence(first_name, last_name):
    """Return a sentence containing the full name."""
    sentence = f"my full name is {first_name} {last_name}"
    return sentence  # Sends the value back and ends the function.


# The returned value is stored in the variable `result`, then printed.
result = get_name_sentence("ziad", "ali")
print(result)


# 7.2 Making an argument optional
# First attempt: all three parameters are required.
def get_formatted_name(first_name, middle_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()  # .title() capitalizes each word.


musician = get_formatted_name("john", "lee", "hooker")
print(musician)
# Problem: this function FAILS if the person has no middle name,
# because the middle_name argument is required.


# Solution: give middle_name a default empty string "" and move it to the END.
def get_name_with_optional_middle(first_name, last_name, middle_name=""):
    """Return a full name; the middle name is optional."""
    # An empty string counts as False in an `if`, any other text counts as True.
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()


print(get_name_with_optional_middle("ziad", "ali", "mahmoud"))  # With a middle name.
print(get_name_with_optional_middle("ziad", "mahmoud"))  # Without a middle name.


# 7.3 Returning a dictionary
# A function can return any type of value: lists, dictionaries, and so on.
def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {"first": first_name, "last": last_name}  # key: value pairs.
    return person


person1 = build_person("ziad", "ali")
print(person1)


# Same idea, with an optional age.
# age=None means "no age was given". None is Python's way of saying "nothing".
def build_person_with_age(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    person = {"first": first_name, "last": last_name}
    if age:  # True only if an age was provided.
        person["age"] = age  # Add a new key to the dictionary.
    return person


# Uncomment to try it:
# person = build_person_with_age("ziad", "mahmoud", 22)
# print(person)
# person2 = build_person_with_age("ziad", "mahmoud")
# print(person2)


# =============================================================================
# 8. Using a Function with a while Loop
# =============================================================================
def build_user(first_name, last_name, age, email):
    """Return a dictionary that describes one user."""
    user = {"first": first_name, "last": last_name, "age": age, "email": email}
    return user


users = []  # An empty list that will store all the users.
while True:  # Infinite loop: runs until we call `break`.
    answer = input("do you want to enter user data? y/n: ")
    if answer == "y":
        print("enter your data:")
        first_name = input("enter your first name: ")
        last_name = input("enter your last name: ")
        age = int(input("enter your age: "))  # int() converts text to a number.
        email = input("enter your email: ")
        # Call the function and keep the dictionary it returns.
        new_user = build_user(first_name, last_name, age, email)
        users.append(new_user)  # Add the dictionary to the list.
    elif answer == "n":
        break  # Leave the loop.
    # Any other answer is ignored and the question is asked again.
print(users)


# =============================================================================
# 9. Passing an Arbitrary Number of Arguments (*args)
# =============================================================================
# Sometimes you don't know how many arguments will be passed.
# A parameter with a star (*toppings) collects ALL the arguments
# into a TUPLE (a list that cannot be changed).
def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)


make_pizza("pepperoni")  # Tuple with 1 item.
make_pizza("mushrooms", "green peppers", "extra cheese")  # Tuple with 3 items.


# =============================================================================
# 10. Using Arbitrary Keyword Arguments (**kwargs)
# =============================================================================
# A parameter with two stars (**user_info) collects all keyword arguments
# (name=value) into a DICTIONARY.
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info["first"] = first  # Add the normal parameters to the dictionary.
    user_info["last"] = last
    return user_info


# Only the required arguments.
profile = build_profile("ziad", "khaled")
print(profile)

# With extra keyword arguments (uncomment to try):
# profile2 = build_profile("ziad", "khaled", location="egypt", field="programming")
# print(profile2)


# =============================================================================
# 11. Storing Your Functions in Modules
# =============================================================================
# A MODULE is a separate .py file that contains functions.
# Why use modules?
#   - Keeps the main file short and focused on the high-level logic.
#   - Lets you reuse the same functions in many programs.
#   - Lets you share your functions without sharing the whole program.
# An `import` statement makes a module's code available in the current file.


# 11.1 Importing an entire module
# `import pizza` (at the top of this file) loads everything from pizza.py.
# To use a function, write: module_name.function_name(arguments)
pizza.make_pizza(16, "pepperoni")
pizza.make_pizza(12, "mushrooms", "green peppers", "extra cheese")
# The `pizza.` prefix tells Python to use the make_pizza from pizza.py,
# not the make_pizza we defined in this file.


# 11.2 Importing specific functions
# General syntax:
#     from module_name import function_name
# Then call the function directly, without the module prefix:
#
# from pizza import make_pizza
# make_pizza(16, "pepperoni")
#
# It is commented out because this file already defines its own make_pizza,
# and the imported one would replace it (a name conflict).


# 11.3 Using `as` to give a function an alias
# `as` gives a short nickname to a function whose name is long
# or conflicts with an existing name:
#
# from pizza import make_pizza as mp
# mp(16, "pepperoni")
#
# `as` also works for a whole module:
#
# import pizza as p
# p.make_pizza(16, "pepperoni")

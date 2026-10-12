"""
╔══════════════════════════════════════════════════════════════╗
║           USER INPUT AND WHILE LOOPS IN PYTHON               ║
║                    A beginner's guide                        ║
╚══════════════════════════════════════════════════════════════╝

What you will learn:
    1. input()          -> ask the user for information
    2. int()            -> turn text into numbers
    3. %  (modulo)      -> find the remainder of a division
    4. while loops      -> repeat code while a condition is True
    5. flag, break, continue -> control the loop
    6. while + lists    -> move and remove items

Tip: this file asks for input many times. Run one section at a time
by commenting out the others, or just follow along and answer each one.
"""


# ══════════════════════════════════════════════════════════════
# PART 1: HOW input() WORKS
# ══════════════════════════════════════════════════════════════
#
# Most programs need information from the user.
# Example: to check if someone can vote, we must ask for their age.
#
# input() does 3 things:
#   1. Shows a message (the "prompt") to the user
#   2. Pauses the program and waits for the user to type + press ENTER
#   3. Returns what the user typed, so we can save it in a variable

user_message = input("Tell me something, and I will repeat it back to you: ")
print(user_message)


# ──────────────────────────────────────────────────────────────
# Writing clear prompts
# ──────────────────────────────────────────────────────────────
# A good prompt tells the user EXACTLY what to type.
# Put a space after the colon so the answer doesn't touch the prompt.

user_name = input("Please enter your name: ")
print(f"\nHello, {user_name}!")


# ──────────────────────────────────────────────────────────────
# Long prompts (more than one line)
# ──────────────────────────────────────────────────────────────
# Build the prompt in a variable first, line by line, using +=
# Then input() stays short and clean.
# "\n" means "start a new line".

long_prompt = "If you share your name, we can personalize the messages you see."
long_prompt += "\nWhat is your first name? "

first_name = input(long_prompt)
print(f"Hello, {first_name}!")


# ══════════════════════════════════════════════════════════════
# PART 2: USING int() TO ACCEPT NUMBERS
# ══════════════════════════════════════════════════════════════
#
# Important: input() ALWAYS returns text (a string),
# even if the user types a number.
#
#       "21"  is text    -> you can't compare it with 18
#        21   is a number -> you can
#
# int() converts text into a whole number.

age = int(input("Enter your age: "))

if age >= 18:
    print("You are old enough to vote!")
else:
    print("You are too young to vote yet.")


# ══════════════════════════════════════════════════════════════
# PART 3: THE MODULO OPERATOR (%)
# ══════════════════════════════════════════════════════════════
#
# % divides one number by another and gives you the REMAINDER.
#
#       4 % 3  ->  1      (4 = 3 x 1 + 1)
#       5 % 3  ->  2      (5 = 3 x 1 + 2)
#       6 % 3  ->  0      (6 = 3 x 2 + 0)
#       7 % 3  ->  1      (7 = 3 x 2 + 1)
#
# Famous trick: if (number % 2 == 0) the number is EVEN.

number = int(input("Enter a number and I will tell you if it is even or odd: "))

if number % 2 == 0:  # remainder 0 when divided by 2 -> even
    print("Even")
else:  # any other remainder -> odd
    print("Odd")


# ══════════════════════════════════════════════════════════════
# PART 4: INTRODUCING while LOOPS
# ══════════════════════════════════════════════════════════════
#
#   for loop   -> runs once for EACH item in a collection
#   while loop -> runs AGAIN AND AGAIN as long as a condition is True
#
# ──────────────────────────────────────────────────────────────
# The while loop in action: count from 1 to 5
# ──────────────────────────────────────────────────────────────

counter = 1  # 1. Start counting at 1

while counter <= 5:  # 2. Keep going while counter is 5 or less
    print(counter)  # 3. Show the current number
    counter += 1  # 4. Add 1  (same as: counter = counter + 1)

# How Python reads it:
#   counter = 1 -> 1 <= 5 is True  -> print 1 -> counter becomes 2
#   counter = 2 -> 2 <= 5 is True  -> print 2 -> counter becomes 3
#   ...
#   counter = 6 -> 6 <= 5 is False -> the loop stops
#
# Output:  1  2  3  4  5


# ══════════════════════════════════════════════════════════════
# PART 5: LETTING THE USER CHOOSE WHEN TO QUIT
# ══════════════════════════════════════════════════════════════
#
# The loop keeps running until the user types 'quit'.

echo_prompt = "\nTell me something, and I will repeat it back to you:"
echo_prompt += "\nEnter 'quit' to end the program. "

echo_message = ""  # Start with an empty value so the loop can begin

while echo_message != "quit":  # Run until the user types "quit"
    echo_message = input(echo_prompt)
    print(echo_message)

# Small problem: the word "quit" is also printed at the end.
# The next two sections show how to fix this.


# ──────────────────────────────────────────────────────────────
# Using a flag
# ──────────────────────────────────────────────────────────────
# A flag is a variable that works like a light switch:
#   True  -> keep running
#   False -> stop
#
# This is useful when MANY things can stop the program.
# You just switch the flag off, and the while loop ends.

flag_prompt = "\nTell me something, and I will repeat it back to you:"
flag_prompt += "\nEnter 'quit' to end the program. "

is_active = True  # The flag: the program is "on"

while is_active:
    flag_message = input(flag_prompt)

    if flag_message == "quit":  # Quotes are important! "quit" is text
        is_active = False  # Switch the flag off -> the loop ends
    else:
        print(flag_message)  # "quit" is NOT printed this time


# ──────────────────────────────────────────────────────────────
# Using break to exit a loop
# ──────────────────────────────────────────────────────────────
# break stops the loop IMMEDIATELY. Nothing after it in the loop runs.
#
# "while True" would run forever on its own,
# so we need break to get out.

city_prompt = "\nPlease enter the name of a city you have visited:"
city_prompt += "\n(Enter 'quit' when you are finished.) "

while True:  # Always True -> endless loop... until break
    city = input(city_prompt)

    if city == "quit":
        break  # Leave the loop right now
    else:
        print(
            f"I'd love to go to {city.title()}!"
        )  # .title() -> "paris" becomes "Paris"


# ──────────────────────────────────────────────────────────────
# Using continue in a loop
# ──────────────────────────────────────────────────────────────
# continue skips the rest of the code in THIS round
# and jumps back to the top of the loop.
#
# Goal: count from 1 to 10 but print ONLY the odd numbers.

current_number = 0

while current_number < 10:
    current_number += 1

    if current_number % 2 == 0:  # Is it even?
        continue  # Yes -> skip printing, go to the next round

    print(current_number)  # Only odd numbers reach this line

# Output:  1  3  5  7  9


# ──────────────────────────────────────────────────────────────
# Avoiding infinite loops
# ──────────────────────────────────────────────────────────────
# Every while loop MUST have a way to stop.
#
# GOOD: the counter grows, so the condition eventually becomes False.

x = 1
while x <= 5:
    print(x)
    x += 1

# BAD: if you forget "x += 1", x stays 1 forever and the loop never ends.
# (It is commented out so this file doesn't freeze. Try it yourself!)
#
# x = 1
# while x <= 5:
#     print(x)
#
# If your program gets stuck, press Ctrl + C in the terminal to stop it.


# ══════════════════════════════════════════════════════════════
# PART 6: USING while LOOPS WITH LISTS
# ══════════════════════════════════════════════════════════════
#
# A for loop is not a good choice when you need to CHANGE a list
# while looping over it. A while loop handles this safely.
#
# ──────────────────────────────────────────────────────────────
# Moving items from one list to another
# ──────────────────────────────────────────────────────────────
# Example: new website users must be verified.
# After verification, we move them to a "confirmed" list.

unconfirmed_users = ["alice", "brian", "candace"]
confirmed_users = []  # Starts empty

# A list is "truthy" when it has items and "falsy" when it is empty.
# So this loop runs until unconfirmed_users is empty.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()  # Remove the LAST user and return it

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)  # Add them to the confirmed list

print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# Output order is candace, brian, alice, because pop() takes from the END.


# ──────────────────────────────────────────────────────────────
# Removing all instances of a specific value
# ──────────────────────────────────────────────────────────────
# remove() deletes only the FIRST match.
# To delete ALL matches, repeat it with a while loop.

pets = ["dog", "cat", "dog", "goldfish", "cat", "rabbit", "cat"]
print(pets)

while "cat" in pets:  # Is there still a "cat" in the list?
    pets.remove("cat")  # Remove one, then check again

print(pets)  # ['dog', 'dog', 'goldfish', 'rabbit']


# ══════════════════════════════════════════════════════════════
# QUICK SUMMARY
# ══════════════════════════════════════════════════════════════
#
#   input("text")     -> asks the user, returns a string
#   int(text)         -> converts a string to a whole number
#   a % b             -> remainder of a / b
#   while condition:  -> repeats while the condition is True
#   flag              -> True/False variable that controls the loop
#   break             -> exit the loop immediately
#   continue          -> skip to the next round of the loop
#   while my_list:    -> loops until the list is empty

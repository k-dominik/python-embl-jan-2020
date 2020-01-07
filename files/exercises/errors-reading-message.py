# Reading Error Messages

# Read the Python code and the resulting traceback below, 
# and answer the following questions:

# How many levels does the traceback have?
# What is the function name where the error occurred?
# On which line number in this function did the error occur?
# What is the type of error?
# What is the error message?
# This code has an intentional error. Do not type it directly;
# use it for reference to understand the error message below.

def print_message(day):
    messages = {
        "monday": "Hello, world!",
        "tuesday": "Today is Tuesday!",
        "wednesday": "It is the middle of the week.",
        "thursday": "Today is Donnerstag in German!",
        "friday": "Last day of the week!",
        "saturday": "Hooray for the weekend!",
        "sunday": "Aw, the weekend is almost over."
    }
    print(messages[day])

def print_friday_message():
    print_message("Friday")

print_friday_message()
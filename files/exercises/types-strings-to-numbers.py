# Strings to Numbers

# Where reasonable, float() will convert a string
# to a floating point number, and int() will convert
# a floating point number to an integer:

print("string to float:", float("3.4"))
print("float to int:", int(3.4))

# If the conversion doesn’t make sense, however,
# an error will occur

print("string to float:", float("Hello world!"))

# Given this information, what do you expect the following program to do?
# What does it actually do?
# Why do you think it does that?

print("fractional string to int:", int("3.4"))

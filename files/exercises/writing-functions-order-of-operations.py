
# Calling the following function like so

def print_date(year, month, day):
    joined = str(year) + '/' + str(month) + '/' + str(day)
    print(joined)

result = print_date(1871, 3, 19)
print('result of call is:', result)

# prints the following output, in that order:

# 1871/3/19
# result of call is: None

# Explain why the two lines of output appeared in the order they did.

# What’s wrong in this example?

result = print_date(1871,3,19)

def print_date(year, month, day):
   joined = str(year) + '/' + str(month) + '/' + str(day)
   print(joined)



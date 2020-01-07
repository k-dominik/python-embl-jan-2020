# Initializing

# Modify this program so that it finds the largest
# and smallest values in the list no matter what the
# range of values originally is.

values = [...some test data...]
smallest, largest = None, None
for v in values:
    if ____:
        smallest, largest = v, v
    ____:
        smallest = min(____, v)
        largest = max(____, v)
print(smallest, largest)

# What are the advantages and disadvantages of using
# this method to find the range of the data?

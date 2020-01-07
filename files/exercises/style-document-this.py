# Document This

# Turn the comment on the following function into a docstring
# and check that help displays it properly.

def middle(a, b, c):
    # Return the middle value of three.
    # Assumes the values can actually be compared.
    values = [a, b, c]
    values.sort()
    return values[1]

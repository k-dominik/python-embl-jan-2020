# Testing Assertions


# Given a sequence of a number of cars, 
# the function get_total_cars returns the total number of cars.

# get_total_cars([1, 2, 3, 4])
# outputs: 10

# get_total_cars(['a', 'b', 'c'])
# outputs: ValueError: invalid literal for int() with base 10: 'a'

# Explain in words what the assertions in this function check, and for each one, give an example of input that will make that assertion fail.

def get_total(values):
    assert len(values) > 0
    for element in values:
        assert int(element)
    values = [int(element) for element in values]
    total = sum(values)
    assert total > 0
    return total
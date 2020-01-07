# Trimming Values

# Fill in the blanks so that this program creates
# a new list containing zeroes where the original list’s
# values were negative and ones where the original list’s
# values were positive.

original = [-1.5, 0.2, 0.4, 0.0, -1.3, 0.4]
result = ____
for value in original:
    if ____:
        result.append(0)
    else:
        ____
print(result)

# expected output: [0, 1, 1, 0, 1]

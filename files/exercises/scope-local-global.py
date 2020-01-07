# Local and Global Variable Use

# Trace the values of all variables in this program
# as it is executed.
# Fill in the comment lines as you do so.
# (Use ‘—’ as the value of variables before and after they exist.)

# limit:
# value:

limit = 100
# limit:
# value:

def clip(value):
    return min(max(0.0, value), limit)
# limit:
# value:

value = -22.5
print(clip(value))
# limit:
# value:

# What Will Be Shown?

# Highlight the lines in the code below that will be
# available as online help.
# Are there lines that should be made available, but won’t be?
# Will any lines produce a syntax error or a runtime error?

"Find maximum edit distance between multiple sequences."
# This finds the maximum distance between all sequences.

def overall_max(sequences):
    '''Determine overall maximum edit distance.'''

    highest = 0
    for left in sequences:
        for right in sequences:
            '''Avoid checking sequence against itself.'''
            if left != right:
                this = edit_distance(left, right)
                highest = max(highest, this)

    # Report.
    return highest

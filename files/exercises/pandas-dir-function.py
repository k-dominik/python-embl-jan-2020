# Using the dir function to see available methods

# Python includes a dir function that can be used to display all 
# of the available methods (functions) that are built into a data object. 
# As an example, the functions available for a list data type are:

potatoes = ["Russet", "Norkota", "Yukon Gold", "Pontiac"]
dir(potatoes)

# This command returns:

"""
['__add__',
...
'__subclasshook__',
 'append',
 'clear',
 'copy',
 'count',
'extend',
'index',
'insert',
'pop',
'remove',
'reverse',
'sort']
"""

# The double underscore functions can be ignored for now; 
# functions that are not surrounded by double underscores are the public interface of the list type. 
# So, if you want to sort the list of potatoes, according to dir you should try,

potatoes.sort()

# Assume Pandas has been imported and the Gapminder GDP data for Europe has been loaded as data. 
# Then, use dir to find the function that prints out the median per-capita GDP across all European 
# countries for each year that information is available.
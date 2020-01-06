# Extent of Slicing

# Do the two statements below produce the same output?
# Based on this, what rule governs what is included (or not) 
# in numerical slices and named slices in Pandas?

print(df.iloc[0:2, 0:2])
print(df.loc['Albania':'Belgium', 'gdpPercap_1952':'gdpPercap_1962'])
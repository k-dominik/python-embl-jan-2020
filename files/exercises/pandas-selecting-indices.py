# Selecting Indices

# Explain in simple terms what idxmin and idxmax do in the short program below. 
# When would you use these methods?

data = pd.read_csv('../../data/gapminder_gdp_europe.csv', index_col='country')
print(data.idxmin())
print(data.idxmax())
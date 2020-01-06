# Correlations

# Modify the example in the notes to create a scatter plot showing 
# the relationship between the minimum and maximum GDP per capita 
# among the countries in Asia for each year in the data set. 
# What relationship do you see (if any)?

data_asia = pd.read_csv('data/gapminder_gdp_asia.csv', index_col='country')
data_asia.describe().T.plot(kind='scatter', x='min', y='max')
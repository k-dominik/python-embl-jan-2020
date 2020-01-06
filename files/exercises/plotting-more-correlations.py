# More Correlations

# This short program creates a plot showing the correlation between GDP 
# and life expectancy for 2007, normalizing marker size by population:

data_all = pd.read_csv('data/gapminder_all.csv', index_col='country')
data_all.plot(kind='scatter', x='gdpPercap_2007', y='lifeExp_2007', s=data_all['pop_2007']/1e6)

# Using online help and other resources, explain what each argument to plot does.
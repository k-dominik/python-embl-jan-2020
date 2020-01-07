# Reconstructing Data

# Explain what each line in the following short program does: what is in first, second, etc.?

first = pd.read_csv('../../data/gapminder_all.csv', index_col='country')
second = first[first['continent'] == 'Americas']
third = second.drop('Puerto Rico')
fourth = third.drop('continent', axis = 1)
fourth.to_csv('result.csv')

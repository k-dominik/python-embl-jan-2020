
#Assume that the following code has been executed:

import pandas as pd

df = pd.read_csv('../../data/gapminder_gdp_asia.csv', index_col=0)
japan = df.loc['Japan']

#1.Complete the statements below to obtain the average GDP for Japan across the years reported for the 1980s.

year = 1983
gdp_decade = 'gdpPercap_' + str(year // ____)
avg = (japan.loc[gdp_decade + ___] + japan.loc[gdp_decade + ___

#2.Abstract the code above into a single function.

def avg_gdp_in_decade(country, continent, year):
    df = pd.read_csv('../../data/gapminder_gdp_'+___+'.csv',delimiter=',',index_col=0)
    ____
    ____
    ____
    return avg

#3.How would you generalize this function if you did not know beforehand which specific years occurred as columns in the data? For instance, what if we also had data from years ending in 1 and 9 for each decade? (Hint: use the columns to filter out the ones that correspond to the decade, instead of enumerating them in the code.)



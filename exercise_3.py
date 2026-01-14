import pandas as pd 

# 1. Load data
drinks = pd.read_csv("drinks.csv")

# 2. Which continent drinks more beer on average?
largest_beer = drinks.groupby('continent')['beer_servings'].mean()
sum_beer = largest_beer.sort_values(ascending = False)
print(sum_beer)

# 3. Wine consumption statistics per continent
wine_stats = drinks.groupby('continent')['wine_servings'].describe()
print(wine_stats)

# 4. Mean alcohol consumption per continent (all columns)
alcohol_mean = drinks.groupby('continent').mean(numeric_only=True)
print(alcohol_mean)

# 5. Mean, min, and max spirit consumption
spirit_mean = drinks.groupby('continent')['spirit_servings'].mean()
spirit_min = drinks.groupby('continent')['spirit_servings'].min()
spirit_max = drinks.groupby('continent')['spirit_servings'].max()

print(spirit_mean)
print(spirit_min)
print(spirit_max)

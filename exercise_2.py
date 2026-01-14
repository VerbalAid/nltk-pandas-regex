import pandas as pd

df = pd.read_csv("Euro2012.csv", encoding="utf-8")

euro12 = df.loc[:, ~df.columns.str.contains('^Unnamed')]         

# 1. Discipline DataFrame
discipline = euro12[['Team', 'Yellow Cards', 'Red Cards']]
print(discipline)

# 2. Sorts the dicipline dataFrame into highest-lowest 'Yellow' and 'red' cards.
sorted_teams = discipline.sort_values(by=['Red Cards', 'Yellow Cards'], ascending=[False, False])
print(sorted_teams)   

# 3. Calculates the mean of yellow cards
print(f"\nMean Yellow Cards per team: {discipline['Yellow Cards'].mean():.2f}") 

# 4. Gets the first 7 columns
print(euro12.iloc[:, :7])  

#5. prints all columns except for the last 3 ones
all_but_last3 = euro12.iloc[:, :-3]
print(all_but_last3)            

#6. Shooting accuracy for England, Italy, and Russia
shooting_accuracy = euro12.loc[euro12['Team'].isin(['England', 'Italy', 'Russia']),'Shooting Accuracy']
print(shooting_accuracy)
import pandas as pd
import random

df1 = pd.read_csv('D:/3170/data/Transport Orders.csv')
df2 = pd.read_csv('D:/3170/data/Transport Order Details.csv')

id_list = []

for index1, row1 in df1.iterrows():
    id_list.append(df1.at[index1, 'Transport Order ID'])
    
i = 0

for index2, row2 in df2.iterrows():
    print(index2)
    i += 1
    df2.at[index2, 'Transport Order Detail ID'] = i
    print(df2.at[index2, 'Transport Order Detail ID'])
    df2.at[index2, 'Transport Order ID'] = id_list[random.randint(0, len(id_list)-1)]
    print(df2.at[index2, 'Transport Order ID'])
    
df2.to_csv('D:/3170/data/Transport Order Details.csv', index=False)
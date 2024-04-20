import pandas as pd
import random

df1 = pd.read_csv('D:/3170/data/Manu Orders.csv')
df2 = pd.read_csv('D:/3170/data/Manu Order Details.csv')
'''df3 = pd.read_csv('D:/3170/data/Manu Orders.csv')
df4 = pd.read_csv('D:/3170/data/Manufacturer Detail.csv')
df5 = pd.read_csv('D:/3170/data/Selling Order Details.csv')'''

#l = []

for index,row in df1.iterrows():
    for index1,row1 in df2.iterrows():
        if index1==index:
            df2.at[index1, 'Manu Order ID'] = df1.at[index, 'Manu Order ID']
    '''for index2,row2 in df3.iterrows():
        if row2['Selling Order ID']==id:
            df3.at[index2, 'Selling Order ID'] = new_id
    for index3,row3 in df4.iterrows():
        if row3['Selling Order ID']==id:
            df4.at[index3, 'Selling Order ID'] = new_id
    for index4,row4 in df5.iterrows():
        if row4['Selling Order ID']==id:
            df5.at[index4, 'Selling Order ID'] = new_id'''

df1.to_csv('D:/3170/data/Manu Orders.csv', index=False)
df2.to_csv('D:/3170/data/Manu Order Details.csv', index=False)
'''df3.to_csv('D:/3170/data/Manu Orders.csv', index=False)
df4.to_csv('D:/3170/data/Manufacturer Detail.csv', index=False)
df5.to_csv('D:/3170/data/Selling Order Details.csv', index=False)'''

 
#import numpy as np

#data = [99, 86, 73, 67, 93] 
#ser = np.mean(data)
#print(ser)

import pandas as pd

df = pd.read_csv('Records.csv')
#print(df.head(4))  To see first 4 rows
#print(df.tail(3))  To see last 3 rows 
#print(df.columns) 	for the headers list
#print(df[['Country', 'Ship Date']])	for two columns
print(len(df))		#number of rows
print(len(df.columns))		#number of columns
#print(df.iloc[[1, 3, 5]])	to select multiple rows 
#print(df.iloc[[2, 3, 5], [0, 1]] )	#to select multiple rows with some particular columns 
#df.set_index("Country", inplace = True) # Set 'Country' column as index 
#print(df.loc[['Turkey']])  After setting 'Country' as index select rows with 'Turkey'

#print(df.iloc[:, [0, 1]])   # some particular columns  
#print(df.iloc[2,1])	#to select a cell
#  .loc for label
#  .iloc for positions
#  explicitly designate both rows and columns, even if it's with ':'
# print(df.iloc[11, :]) to select a certain row
#print(df.loc[df.loc[:, 'Item Type'] == 'Meat',:])  #select rows based on a column value
#print(df.sort_values('Item Type', ascending = False)) #sorting  the list
#print(df.sort_values(['Item Type', 'Total Cost'], ascending= [1,0])) #sorting the list for multiple values
#print(df.iloc[:, 1:4])    #select 1th, 2th, 3rd columns
#print(df.iloc[1:3,1:4]) #to slice a part of the df
#print(df[10:24:3]) #starting from 10 to 23th row with 3 skip
#print(df.columns)
#df['Total Income'] = df['Total Cost'] +df['Total Profit']  #add a new column named 'Total Income'
#print(df.columns)
#print(df.head(4))
#print(df.loc[5:11, 'Ship Date':'Total Revenue']) select certain rows and certain columns
#print(df.iloc[4:10, [0,3]]) #select 0th and 3th columns
#print(df.iloc[[4,7],[0,3]])  #select more specific rows and columns
print(df.shape) #another way of getting the size of df
#print(df[['Item Type', 'Total Cost']][:4]) #select rows and columns
#item_counts = df['Item Type'].value_counts()
#print(item_counts)  #get number of each item

#records_first3 = df.head(3)  #create a new dataframe from the first 3 rows
#print(records_first3)
#records_last3 =df.tail(3)    #crreate a new dataframe from the last 3 rows
#print(records_last3)
#records_first3 =records_first3.reset_index(drop = True)  #erase index cloumn
#records_last3 = records_last3.reset_index(drop=True)
#vertical_stack = pd.concat([records_first3, records_last3], axis =0)   
#print(vertical_stack)   #stack the dataframes on top of each other

#horizontal_stack = pd.concat([records_first3, records_last3], axis =1)
#print(horizontal_stack)     #place the dataframes side by side

#vertical_stack.to_csv('records_sample.csv', index=False)     #writing out to a new CSV file without index column
#print(pd.read_csv('records_sample.csv'))
records_first5 = df.head(5)  #create a new dataframe from the first 5 rows
print(records_first5)
df_new = pd.DataFrame([['Namibia', 'ND', 230000], ['Iceland', 'IF', 75900],['Mexico', 'RR', 890000]], index = [0, 1, 2], columns=['Country', 'Currency', 'Population'])
print(df_new)
merged_inner = pd.merge(left=records_first5, right = df_new, left_on = 'Country', right_on = 'Country')
print(merged_inner) #contains only the rows that have the same 'Country' values, i.e., Namibia and Iceland.
merged_left= pd.merge(left=records_first5, right = df_new, how='left', left_on = 'Country', right_on = 'Country')
print(merged_left)  #contains all rows frow the left, but not all from the right, i.e., Mexico is missing.

#how='right' and how='outer' are the other two types of merge in pandas.








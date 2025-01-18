#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 14:47:03 2024

@author: naodasfaw
"""

import pandas as pd
from datetime import datetime
import seaborn as sns
import matplotlib.pyplot as plt

# Read the excel and CSV files
pizza_sales_df = pd.read_excel('pizza_sales.xlsx')
pizza_category_df = pd.read_csv('pizza_category.csv')
pizza_size_df = pd.read_csv('pizza_size.csv')

# See the top and bottom of the data
pizza_sales_df.head()
pizza_sales_df.tail()

# Describe the data
pizza_description = pizza_sales_df.describe()

# Take a look at the null values and data types
pizza_sales_df.info()

# Count the number of nulls
null_count = pizza_sales_df.isnull().sum()

# Check for duplicated rows
duplicated_rows = pizza_sales_df.duplicated().sum()
print(f"Number of duplicated rows: {duplicated_rows}")

# Select specific columns
quantity_column = pizza_sales_df['quantity']
selected_columns = pizza_sales_df[['order_id', 'quantity', 'unit_price']]

# Get the row with index label 3 
row = pizza_sales_df.loc[3]

# Get two rows with index labels 3 and 5
rows = pizza_sales_df.loc[[3, 5]]

# Get rows between index 3 and 5 (inclusive)
subset = pizza_sales_df.loc[3:5]

# Get rows between index 3 and 5 for specific columns
subset_columns = pizza_sales_df.loc[3:5, ['quantity', 'unit_price']]

# Set 'order_details_id' as the index
pizza_sales_df.set_index('order_details_id', inplace=True)

# Reset the index
pizza_sales_df.reset_index(inplace=True)

# Truncate DataFrame before and after index
truncated_before = pizza_sales_df.truncate(before=3)
truncated_after = pizza_sales_df.truncate(after=5)

# Truncate a column series
quantity_series = pizza_sales_df['quantity']
truncated_series_before = quantity_series.truncate(before=3)
truncated_series_after = quantity_series.truncate(after=5)

# Basic filtering
filtered_rows = pizza_sales_df[pizza_sales_df['unit_price'] > 20]

# Filtering on date
pizza_sales_df['order_date'] = pd.to_datetime(pizza_sales_df['order_date']).dt.date
date_target = datetime.strptime('2015-12-15', '%Y-%m-%d').date()
filtered_rows_by_date = pizza_sales_df[pizza_sales_df['order_date'] > date_target]

# Filtering with multiple conditions
bbq_chicken_rows = pizza_sales_df[(pizza_sales_df['unit_price'] > 15) & 
                                  (pizza_sales_df['pizza_name'] == "The Barbecue Chicken Pizza")]

# Using the OR condition for filtering
bbq_chicken_rows_or = pizza_sales_df[(pizza_sales_df['unit_price'] > 20) | 
                                     (pizza_sales_df['pizza_name'] == "The Barbecue Chicken Pizza")]

# Filter specific range
high_sales = pizza_sales_df[(pizza_sales_df['unit_price'] > 15) & (pizza_sales_df['unit_price'] <= 20)]

# Dropping null values
pizza_sales_no_nulls = pizza_sales_df.dropna()
null_count_after_drop = pizza_sales_no_nulls.isnull().sum()

# Replace the null values with a specific date
date_na_fill = datetime.strptime('2001-01-01', '%Y-%m-%d').date()
pizza_sales_null_replaced = pizza_sales_df.fillna(date_na_fill)

# Deleting specific rows and columns in a DataFrame
filtering_rows_2 = pizza_sales_df.drop(2, axis=0)

# Delete rows 5, 7, and 9
filtering_rows_5_7_9 = pizza_sales_df.drop([5, 7, 9], axis=0)

# Delete the 'unit_price' column
filtered_unit_price = pizza_sales_df.drop('unit_price', axis=1)

# Delete multiple columns
filtered_unit_price_and_order_id = pizza_sales_df.drop(['unit_price', 'order_id'], axis=1)

# Sorting a DataFrame in ascending order
sorted_df_ascending = pizza_sales_df.sort_values('total_price')

# Sorting a DataFrame in descending order
sorted_df_descending = pizza_sales_df.sort_values('total_price', ascending=False)

# Sorting by multiple columns
sorted_df_multi = pizza_sales_df.sort_values(['pizza_category_id', 'total_price'], ascending=[True, False])

# Group by pizza size and count the number of occurrences for each size
group_df_pizza_size_count = pizza_sales_df.groupby(['pizza_size_id']).count()

# Group by pizza size and sum the values
group_df_pizza_size_sum = pizza_sales_df.groupby(['pizza_size_id']).sum()

# Group by pizza size and calculate the sum for 'total_price' and 'quantity'
group_df_pizza_size_agg = pizza_sales_df.groupby(['pizza_size_id'])[['total_price', 'quantity']].sum()

# Perform different aggregations for different columns
aggregated_data = pizza_sales_df.groupby(['pizza_size_id']).agg({
    'total_price': ['sum', 'mean', 'max'],
    'quantity': ['sum', 'mean', 'max']
})

# Print the aggregated data for verification
print(aggregated_data)

#merging pizza size df and pizza sales df
merged_df = pd.merge(pizza_sales_df,pizza_size_df, on = 'pizza_size_id')
#add category information
merged_df = pd.merge(merged_df,pizza_category_df, on = 'pizza_category_id')

#concatonate two dataframes vertically 
another_pizza_sales_df = pd.read_excel('another_pizza_sales.xlsx')
concatonate_vertically = pd.concat([pizza_sales_df,another_pizza_sales_df])
concatonate_vertically = concatonate_vertically.reset_index()

# concatonate two dataframes - appending columns to a dataframe
pizza_sales_voucher_df = pd.read_excel('pizza_sales_voucher.xlsx')
concatonate_horizontally = pd.concat([pizza_sales_df,pizza_sales_voucher_df], axis =1)

#converting into lower case
lower_text = pizza_sales_df['pizza_ingredients'].str.lower()
pizza_sales_df["pizza_ingredients"] = pizza_sales_df['pizza_ingredients'].str.lower()

#converting a title 
pizza_sales_df["pizza_ingredients"] =  pizza_sales_df['pizza_ingredients'].str.title()

#replacing text values
replaced_text = pizza_sales_df['pizza_ingredients'].str.replace('Feta Cheese', "Mozzarella")
pizza_sales_df["pizza_ingredients"] = pizza_sales_df["pizza_ingredients"].str.replace('Feta Cheese','Mozzarella')

#removing white strips
pizza_sales_df['pizza_name'] =pizza_sales_df['pizza_name'].str.strip()


#generating a boxplot
sns.boxplot(x= 'category',y = 'total_price' ,data = merged_df)
plt.xlabel("Pizza category ")
plt.ylabel("Total Sales")
plt.title("Boxplot showing distribution of sales in the category")
plt.show()




























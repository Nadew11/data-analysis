#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 13:24:25 2024

@author: naodasfaw
"""

#import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

loan_data = pd.read_excel('loandataset.xlsx')
customer_data = pd.read_csv('customer_data.csv', sep = ';')

#display the first few rows of the dataset
print(loan_data.head())
print(customer_data.head())


#merging the dataframes
complete_data = pd.merge(loan_data,customer_data, left_on = 'customerid', right_on = 'id')

#check for missing data
complete_data.isnull().sum()

#remove the rows with missing data
complete_data = complete_data.dropna()
complete_data.isnull().sum()

#check for duplicated data
complete_data.duplicated().sum()


#dropping dublicates
complete_data = complete_data.drop_duplicates()

#functions in python

def add_numbers(numb1,numb2):
    sum = numb1 + numb2
    return sum
result = add_numbers(10, 50)
print(result)

#define a function to categorize purpose into broader categories

def categorize_purpose(purpose):
    if purpose in ['credit_card', 'debt_consolidation']:
        return 'Financial'
    elif purpose in ['educational', 'small_business']:
        return 'Educational/Business'
    else:
        return 'Other'
    
    
categorize_purpose('credit_card')

complete_data ['purpose_category']  =  complete_data['purpose'].apply(categorize_purpose)

#create a new function based on  criteria

#if the dti ratio is more than 20 and the deliq.2years is greater than 2 years and the revol.util > 60

def assess_risk(row):
    if  row['dti'] > 20 and row['delinq.2yrs'] >2 and row['revol.util'] > 60:
        return 'High risk'
    else:
        return 'Low risk'

complete_data['Risk'] = complete_data.apply(assess_risk, axis = 1)

#create a new function to FICO Sqores

def categorize_fico(fico_score):
    if fico_score >= 800 and fico_score <= 850:
        return 'Excellent'
    elif fico_score >= 740 and fico_score < 800:
        return 'Very Good'
    elif fico_score >= 670 and fico_score < 740:
        return 'Good'
    elif fico_score >= 580 and fico_score < 670:
        return 'Fair'
    else:
        return 'Poor'
        
complete_data['fico_category'] = complete_data['fico'].apply(categorize_fico)

def identify_high_ing_derog(row):
    average_ing = complete_data['inq.last.6mths'].mean()
    average_derog = complete_data['pub.rec'].mean() 
    
    # Check if row values exceed the averages
    if row['inq.last.6mths'] > average_ing and row['pub.rec'] > average_derog:
        return True
    else:
        return False
        
complete_data['High_Inquiries_and_Public_Records'] = complete_data.apply(identify_high_ing_derog, axis=1)

#create a class for data analysis

class DataAnalysis:
    def __init__(self, df, column_name):
        self.df = df
        self.column_name = column_name
        
    def calculate_mean(self):
        return self.df[self.column_name].mean()
    
    def calculate_median(self):
        return self.df[self.column_name].median()
   

analysis = DataAnalysis(complete_data,'fico')
mean_fico = analysis.calculate_mean()
median_fisco = analysis.calculate_median()


# Data visualatation 
#set the style of the visualisation
sns.set_style('darkgrid')


# bar plot distribution of loans by purpose
plt.figure(figsize=(10,6))
sns.countplot(x = 'purpose',data = complete_data)
plt.title('loan purpose distribution')
plt.xlabel('Number of loans')
plt.ylabel('purpose of loans')
plt.xticks(rotation = 45)
plt.show()


#create a scatterplot for 'dti' and income
plt.figure(figsize=(10,6))
sns.scatterplot(x = 'log.annual.inc', y = 'dti', data = complete_data)
plt.title('Debt-Income Ratio VS Annual Income')
plt.show()

#distribution of Fico score
plt.figure(figsize=(10,6))
sns.histplot(complete_data['fico'], bins= 30)
plt.title('Distribution of FICO')
plt.show()

#box plot to determine risk vs intrest rate
plt.figure(figsize=(10,6))
sns.boxplot(x = 'Risk', y = 'int.rate',data = complete_data)
plt.title('Intrest rate vs Risk')
plt.show()






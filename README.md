# data-analysis

Overview

This repository contains data analysis projects showcasing various applications of NumPy, Pandas, and Python-based tools for data manipulation, visualization, and analysis. The repository includes five distinct projects with the source data, scripts, and outputs organized for clarity.

Introduction to NumPy and Pandas
NumPy:
Supports multi-dimensional arrays and matrices.
Performs mathematical operations with high efficiency.
Key Features: Broadcasting, slicing, indexing, and integration with other tools.
Pandas:
Popular for structured data manipulation and analysis.
Key Features: DataFrames and Series, missing data handling, descriptive statistics, time-series analysis, and more.
Project 1: Analyzing Amazon Sales Data

Objective: Provide insights into sales performance for a merchant selling on Amazon.

Tasks:

Count sales with amounts greater than 1000.
Count sales in the "Tops" category with a quantity of 3.
Compute:
Total sales by category.
Average amount by category and status.
Total sales by fulfillment and shipment type.
Export the last two tables for investor use.
Dataset: sales_data.xlsx

Project 2: Analyzing E-commerce Orders Data

Objective: Analyze payment behaviors for Olist, a Brazilian e-commerce store.

Tasks:

Join and clean three datasets: orders.xlsx, order_payment.xlsx, customers.xlsx.
Analyze payment amounts by type (e.g., credit card, debit card).
Calculate monthly payment values by type.
Summarize total payment values by month.
Deliverables: Insights into customer payment trends and credit card usage.

Project 3: Analyzing Pizza Sales

Objective: Clean and analyze pizza sales data for a takeout business.

Tasks:

Filter rows with unit prices > 35.
Add a discount column (10% of price).
Drop invalid rows based on index and missing data.
Merge size.csv and category.csv for enriched analysis.
Add manually input data from another_pizza_sales.xlsx.
Create a full pizza name combining name and ingredients.
Replace “feta cheese” with “mozzarella” in ingredients.
Visualize total price by category using a box plot.
Export final table and plot.
Dataset: pizza_sales.xlsx, size.csv, category.csv, and manually input data.

Project 4: LendingClub Loan Analysis

Objective: Predict loan repayment status and provide borrower insights.

Tasks:

Analyze factors like FICO scores, interest rates, and debt-to-income ratios.
Develop visualizations for repayment trends and borrower creditworthiness.
Build a simple predictive model to identify high-risk borrowers.
Dataset: loandataset.xlsx, customer_data.csv

Project 5: Sentiment Analysis

Objective: Determine public sentiment about ChatGPT using Twitter data.

Tasks:

Preprocess tweet text to remove stopwords.
Use TextBlob to classify sentiment (positive, negative, neutral).
Analyze sentiment distribution and key hashtags.
Visualize findings using descriptive statistics and charts.
Dataset: chatgpt1.csv

Folder Structure

Source (Input) Data for the Course: Contains all raw datasets.
Final Scripts and Outputs: Includes final scripts, processed data, and visualizations.
README: This document serves as an overview of the repository and its contents.
How to Use

Clone the repository.
Ensure Python 3.x is installed with the required libraries (NumPy, Pandas, TextBlob, etc.).
Run the scripts in the respective project folders to replicate the analysis.
Feel free to modify this README further to fit your presentation needs. Let me know if you need additional sections or formatting changes!








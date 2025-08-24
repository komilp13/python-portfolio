import matplotlib.pyplot as plt
import pandas as pd

# read the csv file
df = pd.read_csv("./data/new_york_listings_2024.csv")


# Initial Exploration
print(df.head())
print(df.info())
print('Initial data shape:', df.shape)
print(df.describe())

# Identify missing values & duplicates
print('Missing values:\n', df.isnull().sum())
print('Number of duplicates:', df.duplicated().sum())

# Handle missing values by filling with the average
df['reviews_per_month'].fillna(df['reviews_per_month'].mean(), inplace=True)
df['price'].fillna(df['price'].mean(), inplace=True)
df['number_of_reviews'].fillna(df['number_of_reviews'].mean(), inplace=True)

# Drop rows where data is still missing & duplicates
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

# AFTER the cleaning
# print(df.head())
# print(df.info())
# print('Initial data shape:', df.shape)
# print(df.describe())


#### DATA VISUALIZATION  ####

# Plot a single column - draws a histogram of prices
df['price'].plot()
plt.ylabel('Price')
plt.title('New York Listings 2024 Prices')
# plt.show()

# # Plots a scatter plot of all the prices
df.plot(kind='scatter', x='price', y='number_of_reviews')
plt.title('New York Listings 2024 - Prices vs Number of Reviews')
# plt.show()

# # Creating a subplot
fig, axs = plt.subplots(2, 3, figsize=(12, 10))

# Price vs Frequency
axs[0,0].hist(df['price'], bins=20, color='lightblue')
axs[0,0].set_title('Price vs Frequency')
axs[0,0].set_xlabel('Price')
axs[0,0].set_ylabel('Frequency')

# Number of reviews vs Frequncy
axs[0,1].hist(df['number_of_reviews'], bins=20, color='red')
axs[0,1].set_title('Number of Reviews vs Frequency')
axs[0,1].set_xlabel('# of Reviews')
axs[0,1].set_ylabel('Frequency')

# Group by type of room and show avg price
room_type = df.groupby('room_type')['price'].mean().reset_index()
axs[0,2].bar(room_type['room_type'], room_type['price'], color='lightgreen')
axs[0,2].set_title('Avg Price by Room Type')
axs[0,2].set_xlabel('Room Type')
axs[0,2].set_ylabel('Price')

# Number of listings in each borough (NYC)
neighborhoods = df['neighbourhood_group'].value_counts().reset_index()
neighborhoods.columns = ['neighbourhood_group', 'count']
axs[1,0].bar(neighborhoods['neighbourhood_group'], neighborhoods['count'], color='orange')
axs[1,0].set_title('Listings by Neighborhood')
axs[1,0].set_xlabel('Neighbourhood')
axs[1,0].set_ylabel('Count')

# Price vs Number of Reviews
axs[1,1].scatter(df['price'], df['number_of_reviews'], color='lightgray')
axs[1,1].set_title('Price vs Number of Reviews')
axs[1,1].set_xlabel('Price')
axs[1,1].set_ylabel('# of reviews')

plt.tight_layout()
plt.show()
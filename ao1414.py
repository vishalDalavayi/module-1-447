import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
restaurants_path = '/Users/vishaldalavayi/Downloads/archive/restaurants.csv'
menus_path = '/Users/vishaldalavayi/Downloads/archive/restaurant-menus.csv'
restaurants_df = pd.read_csv(restaurants_path)
menus_df = pd.read_csv(menus_path)

# Data Cleaning
# Convert 'price' column to numeric by removing non-numeric characters
menus_df['price'] = menus_df['price'].replace(r'[^0-9.]', '', regex=True).astype(float)

# Drop rows with missing values in critical fields (if any)
menus_df.dropna(subset=['category', 'name', 'price'], inplace=True)

# Figure 1: Bar Chart of Top Categories by Menu Item Count
# Calculate the top 10 categories by menu item count
category_counts = menus_df['category'].value_counts().head(10)

# Plot the bar chart
plt.figure(figsize=(10, 6))
sns.barplot(x=category_counts.values, y=category_counts.index, palette="viridis")
plt.title("Top Categories by Menu Item Count")
plt.xlabel("Number of Menu Items")
plt.ylabel("Category")
plt.show()

# Figure 2: Box Plot of Prices by Category
# Filter data to the top categories for a clearer plot
top_categories = category_counts.index
filtered_menus_df = menus_df[menus_df['category'].isin(top_categories)]

# Plot the box plot
plt.figure(figsize=(12, 8))
sns.boxplot(x='price', y='category', data=filtered_menus_df, palette="viridis")
plt.title("Price Distribution by Category (Top 10 Categories)")
plt.xlabel("Price (USD)")
plt.ylabel("Category")
plt.show()

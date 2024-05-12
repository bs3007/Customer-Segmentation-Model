# Get customers with the least frequency of purchases
least_frequent_customers = data.sort_values(by='PURCHASES_FREQUENCY').head(10)

# Get customers with the most frequency of purchases
most_frequent_customers = data.sort_values(by='PURCHASES_FREQUENCY', ascending=False).head(10)

print("People for discount least frequent customers:")
print(least_frequent_customers[['CUST_ID', 'PURCHASES_FREQUENCY']])

print("\nPeople for bonus points most customers:")
print(most_frequent_customers[['CUST_ID', 'PURCHASES_FREQUENCY']])

import pandas as pd

# Load sample e-commerce data
data = {
    'OrderID': [101, 102, 103, 104],
    'CustomerID': [1, 2, 1, 3],
    'Amount': [250.50, 45.00, 120.00, 300.00],
    'Status': ['Shipped', 'Cancelled', 'Shipped', 'Processing']
}

df = pd.DataFrame(data)

# Clean data: Filter out cancelled orders
clean_df = df[df['Status'] != 'Cancelled']

# Calculate total revenue
total_revenue = clean_df['Amount'].sum()
print(f"Total Revenue: ${total_revenue}")

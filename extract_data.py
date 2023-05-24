import pandas as pd

# Specify the path to the sales data file
sales_data_file = 'sales_data.csv'

# Read the sales data into a Pandas DataFrame
sales_df = pd.read_csv(sales_data_file)

# Display the first few rows of the DataFrame
print(sales_df.head())

# Additional data extraction and preprocessing steps can be performed here

# Save the extracted data to a new CSV file
extracted_data_file = 'extracted_data.csv'
sales_df.to_csv(extracted_data_file, index=False)

print('Data extraction completed successfully!')

import pandas as pd

# Specify the path to the extracted data file
extracted_data_file = 'extracted_data.csv'

# Read the extracted data into a Pandas DataFrame
data_df = pd.read_csv(extracted_data_file)

# Perform data cleaning and preprocessing steps
# Example: Removing duplicates
data_df = data_df.drop_duplicates()

# Example: Handling missing values
data_df = data_df.dropna()

# Additional data cleaning and preprocessing steps can be performed here

# Save the cleaned data to a new CSV file
cleaned_data_file = 'cleaned_data.csv'
data_df.to_csv(cleaned_data_file, index=False)

print('Data cleaning completed successfully!')

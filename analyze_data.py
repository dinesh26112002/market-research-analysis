import pandas as pd

# Specify the path to the cleaned data file
cleaned_data_file = 'cleaned_data.csv'

# Read the cleaned data into a Pandas DataFrame
data_df = pd.read_csv(cleaned_data_file)

# Perform data analysis and calculate the number of products sold
analysis_df = data_df.groupby(['Country', 'Gender']).sum()
analysis_df = analysis_df.rename(columns={'Products Bought': 'Total Products Bought', 'Products Sold': 'Total Products Sold'})
analysis_df['Products Sold'] = analysis_df['Total Products Bought'] - analysis_df['Total Products Sold']

# Save the analysis results to a new CSV file
analysis_report_file = 'analysis_report.csv'
analysis_df.to_csv(analysis_report_file)

print('Data analysis completed successfully!')

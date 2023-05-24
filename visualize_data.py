import pandas as pd
import matplotlib.pyplot as plt

# Specify the path to the analysis report file
analysis_report_file = 'analysis_report.csv'

# Read the analysis report into a Pandas DataFrame
analysis_df = pd.read_csv(analysis_report_file)

# Generate bar chart for products sold by country
plt.figure(figsize=(10, 6))
plt.bar(analysis_df['Country'], analysis_df['Products Sold'])
plt.xlabel('Country')
plt.ylabel('Products Sold')
plt.title('Products Sold by Country')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('charts/products_sold_by_country.png')
plt.close()

# Generate pie chart for products sold by gender
plt.figure(figsize=(8, 8))
plt.pie(analysis_df['Products Sold'], labels=analysis_df['Gender'], autopct='%1.1f%%')
plt.axis('equal')
plt.title('Products Sold by Gender')
plt.tight_layout()
plt.savefig('charts/products_sold_by_gender.png')
plt.close()

print('Data visualization completed successfully!')

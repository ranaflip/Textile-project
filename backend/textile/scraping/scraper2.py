from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://www.fao.org/faostat/en/#data/QCL"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find the relevant table; inspect the site for the correct class or id
table = soup.find('table')  # Adjust as necessary
df = pd.read_html(str(table))[0]  # Use pandas to read the HTML table

print(df.head())  # Display the first few rows of the DataFrame

import requests
from bs4 import BeautifulSoup

url = "https://public.tableau.com/app/profile/world.trade.organization.ersd/viz/TradeConnectivityHeatmap/Dashboard1"

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Inspect the page to find the right data element
# This is just a placeholder; you'll need to adjust based on the actual HTML structure
data_elements = soup.find_all('div', class_='your-target-class')  # Update with actual class

data = []
for element in data_elements:
    # Extract the required data
    data.append({
        'key_data': element.text.strip()  # Adjust according to your needs
    })

print(data)

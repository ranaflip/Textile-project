import requests
from bs4 import BeautifulSoup

url = "https://www.trademap.org/Bilateral_TS.aspx?nvpm=1%7c699%7c%7c%7c20%7cTOTAL%7c%7c%7c2%7c1%7c1%7c3%7c2%7c1%7c1%7c1%7c1%7c1"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find the data; inspect the site for the correct elements
data_elements = soup.find_all('tr')  # Update based on actual HTML structure

data = []
for row in data_elements:
    cols = row.find_all('td')
    if cols:
        data.append({
            'column1': cols[0].text.strip(),  # Adjust indices as needed
            'column2': cols[1].text.strip(),
            # Continue for other columns
        })

print(data)

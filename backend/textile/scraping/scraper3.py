from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

# Use raw string to avoid invalid escape sequence warning
edge_driver_path = r"C:\Work\edgedriver_win64\msedgedriver.exe"  # Update with your actual path

# Set up Edge options and specify headless mode
options = webdriver.EdgeOptions()
options.add_argument("headless")
options.add_argument("disable-gpu")  # Sometimes helps in headless mode
options.binary_location = edge_driver_path

# Initialize the WebDriver for Edge
try:
    driver = webdriver.Edge(options=options)
except Exception as e:
    print("An error occurred initializing Edge WebDriver:", e)
    exit(1)

# Open the TradeMap URL
url = "https://www.trademap.org/Product_SelCountry_TS.aspx?nvpm=1%7c699%7c%7c%7c%7cTOTAL%7c%7c%7c2%7c1%7c1%7c3%7c2%7c1%7c1%7c1%7c1%7c1"
driver.get(url)

# Wait for the table to load on the page
try:
    # Wait until the table is present on the page
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "MainContent_grvAnnualData"))  # Adjust ID if necessary
    )
    
    # Locate the table by ID
    table = driver.find_element(By.ID, "MainContent_grvAnnualData")
    
    # Extract data from the table
    data = []
    rows = table.find_elements(By.TAG_NAME, "tr")
    
    for row in rows:
        cols = row.find_elements(By.TAG_NAME, "td")
        cols_text = [col.text for col in cols]
        if cols_text:  # Only append non-empty rows
            data.append(cols_text)
    
    # Convert the data to a DataFrame
    df = pd.DataFrame(data)
    
    # Save the DataFrame to a CSV file
    df.to_csv("trade_data.csv", index=False)
    print("Data has been successfully saved to trade_data.csv")
    
except Exception as e:
    print("An error occurred while extracting data:", e)

finally:
    # Close the WebDriver
    driver.quit()

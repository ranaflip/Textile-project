from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

# Path to chromedriver (update this if necessary)
chrome_driver_path = r"C:\Work\chromedriver-win64\chromedriver.exe"  # Ensure this path is correct

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode (remove this line if you want to see the browser)
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")  # Use with caution
chrome_options.add_argument("--window-size=1920x1080")  # Set window size for headless mode

# Initialize the Chrome WebDriver service
service = Service(chrome_driver_path)

# List to store all data
all_data = []

try:
    # Initialize the WebDriver
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.set_page_load_timeout(60)  # Increased page load timeout

    # Open the URL
    url = "https://www.trademap.org/Product_SelCountry_TS.aspx?nvpm=1%7c699%7c%7c%7c%7cTOTAL%7c%7c%7c4%7c1%7c1%7c1%7c2%7c1%7c1%7c1%7c1%7c1"
    driver.get(url)

    # Wait for the table to load on the page
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CLASS_NAME, "tabContent"))
    )

    while True:
        # Locate the table by class name
        table = driver.find_element(By.CLASS_NAME, "tabContent")

        # Extract data from the current page
        rows = table.find_elements(By.TAG_NAME, "tr")

        for row in rows[1:]:  # Skip header row if it exists
            cols = row.find_elements(By.TAG_NAME, "td")
            cols_text = [col.text.strip() for col in cols]  # Clean up whitespace
            if cols_text:
                all_data.append(cols_text)

        # Check for JavaScript-based pagination
        try:
            # You can adapt this part based on how the pagination is structured
            # Example: Click on a button or a page number
            next_button = driver.find_element(By.XPATH, "//a[@class='next']")  # Adjust this XPath as necessary
            next_button.click()
            WebDriverWait(driver, 30).until(EC.staleness_of(rows[0]))  # Wait for the new page to load
        except Exception as e:
            print("No more pages or an error occurred:", e)
            break

    # Create a DataFrame from the collected data
    df = pd.DataFrame(all_data)

    # Save the DataFrame to an Excel file
    df.to_excel(r"C:\Work\trade_data.xlsx", index=False, header=False)  # Specify the full path if needed
    print("Data has been successfully saved to trade_data.xlsx")

except Exception as e:
    print("An error occurred:", e)

finally:
    # Quit the driver if it was successfully created
    if 'driver' in locals():
        driver.quit()

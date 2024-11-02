from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the Edge WebDriver
driver = webdriver.Edge()  # Or specify the path: webdriver.Edge(executable_path='path/to/msedgedriver')

# Open the Tableau dashboard URL
url = "https://public.tableau.com/app/profile/world.trade.organization.ersd/viz/TradeConnectivityHeatmap/Dashboard1"
driver.get(url)

try:
    # Wait for the main Tableau iframe to load
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "iframe[title*='Viz']"))
    )

    # Switch to the Tableau iframe
    tableau_iframe = driver.find_element(By.CSS_SELECTOR, "iframe[title*='Viz']")
    driver.switch_to.frame(tableau_iframe)
    
    # Wait for the dashboard to load data within the iframe
    WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "tabCanvas"))
    )

    # Locate specific data elements (update "YOUR-SELECTOR" to the actual element selector you need)
    data_elements = driver.find_elements(By.CSS_SELECTOR, "YOUR-SELECTOR")

    # Extract text or other attributes from each data element
    for element in data_elements:
        print(element.text)

finally:
    # Close the browser after scraping
    driver.quit()

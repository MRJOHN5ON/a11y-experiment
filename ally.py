import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from axe_selenium_python import Axe

# Set up the WebDriver
service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # Open the webpage
    driver.get('https://summeradventure.netlify.app/')
    
    # Initialize axe-core
    axe = Axe(driver)
    
    # Interact with the page
    wait = WebDriverWait(driver, 10)
    
    # Wait for and click the label
    label = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@id="root"]/main/form/fieldset/div/label')))
    label.click()
    
    # Wait for and click the submit button
    submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]')))
    submit_button.click()
    
    # Perform accessibility scan after interactions
    axe.inject()  # Inject axe-core into the page
    results = axe.run()  # Run accessibility tests
    
    # Format results for readability
    formatted_results = json.dumps(results, indent=4)
    
    # Save formatted results to a file
    with open('accessibility_report.json', 'w') as file:
        file.write(formatted_results)
    
finally:
    # Close the WebDriver
    driver.quit()


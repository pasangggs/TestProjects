import pytest
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

@pytest.fixture(scope="class")
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

def test_view_gold_(driver):
    """
    Test case to verify the user can view all prices on the Economy page

    Steps:
        1. Open the sharesansar.com website.
        2. Navigate to the "Economy" section.
        3. Locate the element containing the Gold & Silver Price section.
        4. Click on the Gold & Silver Price section.
    """

    driver.get("https://www.sharesansar.com/")

    # Click on the "Economy" section link (assuming it navigates to the economy page)
    economy_section_link = driver.find_element(By.XPATH, "//a[normalize-space()='Economy']")
    economy_section_link.click()

    # Use explicit wait to ensure the inflation section is clickable
    price_section_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,"//a[normalize-space()='Gold & Silver Price']"))
    )
    price_section_link.click()




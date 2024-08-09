import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

@pytest.fixture(scope="class")
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(7)  # Wait for elements up to 7 seconds
    yield driver
    driver.quit()

# HOME SECTION
def test_home_section_is_present(driver):
    """
    Test case to verify the accessibility of the Home section on sharesansar.com

    Steps:
        1. Open the sharesansar.com website.
        2. Verify the "Home" section is present on the page.
    """

    driver.get("https://www.sharesansar.com/")
    home_section = driver.find_element(By.XPATH, "(//a[normalize-space()='Home'])[1]")
    time.sleep(4)
    assert home_section is not None, "Home section not found on the page"

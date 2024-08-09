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

def test_news_section_accessibility(driver):
    """
    Test case to verify the accessibility of the "News" section on sharesansar.com

    Steps:
        1. Open the sharesansar.com website.
        2. Verify the "News" section is present on the page.
    """

    driver.get("https://www.sharesansar.com/")

    news_section_link = driver.find_element(By.XPATH, "//a[normalize-space()='News']")
    time.sleep(4)
    assert news_section_link is not None, "News section link not found on the page"
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
    driver.implicitly_wait(5)  # Implicit wait (can be adjusted)
    yield driver
    driver.quit()

def test_view_announcements(driver):
    """
    Test case to verify the user can view all announcements on the News page

    Steps:
        1. Open the sharesansar.com website.
        2. Navigate to the "News" section.
        3. Locate the element containing the announcement section.
        4. Click on the announcement section.
    """

    driver.get("https://www.sharesansar.com/")

    # Click on the "News" section link (assuming it navigates to the news page)
    news_section_link = driver.find_element(By.XPATH, "//a[normalize-space()='News']")
    news_section_link.click()

    # Use explicit wait to ensure the announcement section is clickable
    announcement_section_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,"//a[normalize-space()='Announcements']"))
    )
    announcement_section_link.click()

    # assert some_element_on_announcement_page.is_displayed()


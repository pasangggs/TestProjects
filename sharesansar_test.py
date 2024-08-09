import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import ElementClickInterceptedException, ElementNotInteractableException, TimeoutException


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(7)
    yield driver
    driver.quit()


def test_google_search(driver):
    driver.get("https://google.com")

    # Find the search box by its name attribute and perform the search
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("sharesansar")
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)

    # Click on the first search result link
    first_result_link = driver.find_element(By.XPATH, "//a[h3[normalize-space()='ShareSansar']]")
    first_result_link.click()
    time.sleep(3)

    # Maximize the browser window
    driver.maximize_window()

    # Scroll down the page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

    # Scroll up the page till the very top
    driver.execute_script("window.scrollTo(0, 0);")
    while driver.execute_script("return window.pageYOffset;") > 0:
        driver.execute_script("window.scrollBy(0, -100);")
    time.sleep(2)

    # Wait for 3 seconds
    time.sleep(3)

    # Hover the mouse on the 'News' navigation item
    news_link = driver.find_element(By.XPATH, "//a[normalize-space()='News']")
    ActionChains(driver).move_to_element(news_link).perform()
    time.sleep(2)

    # Click on the 'All News' link with explicit wait
    all_news_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='All News']"))
    )
    time.sleep(3)  # Wait for 3 seconds after clicking

    # Scroll down the page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

    # Scroll up the page till the very top
    driver.execute_script("window.scrollTo(0, 0);")
    while driver.execute_script("return window.pageYOffset;") > 0:
        driver.execute_script("window.scrollBy(0, -100);")

    # Hover the mouse on the 'News' navigation item again
    ActionChains(driver).move_to_element(news_link).perform()
    time.sleep(2)

    # Click on the 'Announcements' link
    announcements_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Announcements']"))
    )

    try:
        announcements_link.click()
    except (ElementClickInterceptedException, ElementNotInteractableException) as e:
        try:
            # Scroll the 'Announcements' link into view and click
            driver.execute_script("arguments[0].scrollIntoView();", announcements_link)
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable(announcements_link)).click()
        except TimeoutException:
            print("Element was not clickable after waiting.")
            raise e

    time.sleep(3)  # Wait for 3 seconds after clicking

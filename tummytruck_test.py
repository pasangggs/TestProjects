import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(7)
    # Yield the webdriver instance
    yield driver
    # close the webdriver instance
    driver.quit()

def test_google_search(driver):
    driver.get("https://google.com")
    # Find the search box by its name attribute and perform the search
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("tummytruck.com.np")
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)

    # Click on the first search result link (assuming it is the link to tummytruck.com.np)
    first_result_link = driver.find_element(By.XPATH, "//a[@href='https://tummytruck.com.np/']//h3[@class='LC20lb MBeuO DKV0Md'][normalize-space()='Tummy Truck']")
    first_result_link.click()
    time.sleep(5)

    # Navigate to the Home page
    home_link = driver.find_element(*(By.XPATH,"//a[normalize-space()='Home']"))
    home_link.click()
    time.sleep(2)

    # Navigate to the About Us page
    about_us_link = driver.find_element(*(By.XPATH,"//a[normalize-space()='About us']"))
    about_us_link.click()
    time.sleep(2)

    # Navigate to the Contact Us page
    contact_us_link = driver.find_element(*(By.XPATH,"//a[normalize-space()='Contact us']"))
    contact_us_link.click()
    time.sleep(2)

    # Fill in the Your Name field
    name_field = driver.find_element(By.XPATH, "//input[@id='name']")
    name_field.send_keys("Pasang")
    time.sleep(2)

    # Fill in the Your Contact field
    contact_field = driver.find_element(*(By.XPATH,"//input[@id='contact']"))
    contact_field.send_keys("9801234567")
    time.sleep(2)

    # Fill in the Your query field
    query_field = driver.find_element(*(By.XPATH,"//textarea[@id='query']"))
    query_field.send_keys("Yummy")
    time.sleep(2)

    # Navigate to the Menu page
    menu_link = driver.find_element(*(By.XPATH, "//a[normalize-space()='Menu']"))
    menu_link.click()
    time.sleep(2)

    # Click on the GREEN TUMMY PACKAGE'S first week menu item
    first_week_menu = driver.find_element(
        *(By.XPATH, "//div[@id='menu']//div[2]//div[1]//a[1]//div[1]//span[1]//img[1]"))
    first_week_menu.click()
    time.sleep(3)

    # Scroll down
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

    # Scroll up
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(3)

    # Click on the second week menu item
    second_week_menu = driver.find_element(*(By.XPATH,"//a[normalize-space()='second week']"))
    second_week_menu.click()
    time.sleep(3)

    # Scroll down
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

    # Scroll up
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(3)

    # Click on the third week menu item
    third_week_menu = driver.find_element(*(By.XPATH,"//a[normalize-space()='third week']"))
    third_week_menu.click()
    time.sleep(3)

    # Scroll down
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

    # Scroll up
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(3)

    # Click on the fourth week menu item
    fourth_week_menu = driver.find_element(*(By.XPATH,"//a[normalize-space()='fourth week']"))
    fourth_week_menu.click()
    time.sleep(3)

    # Scroll down
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

    # Scroll up
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(3)

    # Againnnn navigate to the Menu page
    menu_link = driver.find_element(*(By.XPATH,"//a[normalize-space()='Menu']"))
    menu_link.click()
    time.sleep(2)

    # Scroll to the center of the page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight / 2);")
    time.sleep(3)

    # Click on the YUMMY TUMMY'S first week
    center_menu = driver.find_element(*(By.XPATH, "//div[3]//div[1]//a[1]//div[1]//span[1]//img[1]"))
    center_menu.click()
    time.sleep(3)

    # Scroll down
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

    # Scroll up
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(3)

    # Click on the second week menu item
    second_week_menu = driver.find_element(*(By.XPATH,"//a[normalize-space()='second week']"))
    second_week_menu.click()
    time.sleep(3)

    # Scroll down
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

    # Scroll up
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(3)

    # Click on the third week menu item
    third_week_menu = driver.find_element(*(By.XPATH, "//a[normalize-space()='third week']"))
    third_week_menu.click()
    time.sleep(3)

    # Scroll down
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

    # Scroll up
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(3)

    # Click on the fourth week menu item
    fourth_week_menu = driver.find_element(*(By.XPATH, "//a[normalize-space()='fourth week']"))
    fourth_week_menu.click()
    time.sleep(3)

    # Scroll down
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

    # Scroll up
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(3)

    # Again navigate to the Menu page
    menu_link = driver.find_element(*(By.XPATH, "//a[normalize-space()='Menu']"))
    menu_link.click()
    time.sleep(2)

    # Scroll to the center of the page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight / 2);")
    time.sleep(3)

    # Click on the PRO TUMMY PACKAGE'S first week menu item
    first_week_menu = driver.find_element(*(By.XPATH,"//body[1]/div[1]/main[1]/div[2]/div[4]/div[1]/a[1]/div[1]/span[1]/img[1]"))
    first_week_menu.click()
    time.sleep(3)

    # Scroll down
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

    # Scroll up
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(3)

    # Click on the second week menu item
    second_week_menu = driver.find_element(*(By.XPATH,"//a[normalize-space()='second week']"))
    second_week_menu.click()
    time.sleep(3)

    # Scroll down
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

    # Scroll up
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(3)

    # Click on the third week menu item
    third_week_menu = driver.find_element(*(By.XPATH,"//a[normalize-space()='third week']"))
    third_week_menu.click()
    time.sleep(3)

    # Scroll down
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

    # Scroll up
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(3)

    # Click on the fourth week menu item
    fourth_week_menu = driver.find_element(*(By.XPATH,"//a[normalize-space()='fourth week']"))
    fourth_week_menu.click()
    time.sleep(3)

    # Scroll down
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

    # Scroll up
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(3)

    print("woohoooo! Test Completed")

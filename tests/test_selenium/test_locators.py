import pytest
from selenium.webdriver.common.by import By

URL = 'http://localhost:3000'


@pytest.mark.selenium
def test_locators(driver):
    driver.get(URL)

    driver.find_element(By.LINK_TEXT, '/automation-lab').is_displayed()
    driver.find_element(By.TAG_NAME, 'header').is_displayed()
    driver.find_element(By.CLASS_NAME, 'hero').is_displayed()
    driver.find_elements(By.CLASS_NAME, 'feature-link')[0].is_displayed()
    driver.find_element(By.PARTIAL_LINK_TEXT, 'Test Design').is_displayed()
    driver.find_element(By.ID, 'wt-sky-root').is_displayed()
    driver.find_element(By.CSS_SELECTOR, )


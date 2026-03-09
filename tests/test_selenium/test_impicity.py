import pytest
from selenium.webdriver.common.by import By

URL = 'http://localhost:3000/automation-lab/subscription'


@pytest.mark.only
def test_button(driver):
    driver.get(URL)
    driver.implicitly_wait(5)
    task_button = driver.find_element(By.CLASS_NAME, 'task-goals-btn')
    task_button.click()
    breakpoint()
    title = driver.find_element(By.CLASS_NAME, 'modal-title')
    assert title.is_displayed()

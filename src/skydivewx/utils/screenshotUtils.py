import base64
import time

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def getBurbleScreenshot(burbleUrl: str):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920,1080")

    img_data = []

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url=burbleUrl)
    try:
        WebDriverWait(driver, 10).until(
            EC.invisibility_of_element_located((By.CLASS_NAME, "x-mask-msg"))
        )
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "x-toolbar"))
        )
        # TODO find a better way to wait for the page components to load
        # maybe EC.visibility_of_element_located or something
        time.sleep(1)
        screenshot = driver.get_screenshot_as_png()
        img_data.append(base64.b64encode(screenshot).decode())
    except TimeoutException as e:
        # Could not load in manifest
        return ""
    finally:
        driver.quit()

    return img_data[0]

import base64
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


def getBurbleScreenshot(burbleUrl: str):
    # TODO "Callback error updating {"index":["ALL"],"type":"live-manifest-image-container"}.children"
    # "<!doctype html>
    # <html lang=en>
    # <title>500 Internal Server Error</title>
    # <h1>Internal Server Error</h1>
    # <p>The server encountered an internal error and was unable to complete your request. Either the server is overloaded or there is an error in the application.</p>
    # "
    # setting selenium options
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")

    img_data = []

    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
    driver.get(url=burbleUrl)
    try:
        WebDriverWait(driver, 10).until(
            EC.invisibility_of_element_located((By.CLASS_NAME, "x-mask-msg"))
        )
        # TODO find a better way to wait for the page components to load
        time.sleep(5)
        screenshot = driver.get_screenshot_as_png()
        img_data.append(base64.b64encode(screenshot).decode())
    except Exception as e:
        raise e
    finally:
        driver.quit()

    return img_data[0]

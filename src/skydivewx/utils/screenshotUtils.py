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
    #     Nov 3 04:04:08 PM  /bin/sh: 1: google-chrome: not found
    # Nov 3 04:04:08 PM  /bin/sh: 1: google-chrome-stable: not found
    # Nov 3 04:04:08 PM  /bin/sh: 1: google-chrome-beta: not found
    # Nov 3 04:04:08 PM  /bin/sh: 1: google-chrome-dev: not found
    # Nov 3 04:04:08 PM  /bin/sh: 1: google-chrome: not found
    # Nov 3 04:04:08 PM  /bin/sh: 1: google-chrome-stable: not found
    # Nov 3 04:04:08 PM  /bin/sh: 1: google-chrome-beta: not found
    # Nov 3 04:04:08 PM  /bin/sh: 1: google-chrome-dev: not found
    # Nov 3 04:04:08 PM  [2023-11-03 22:04:08,740] ERROR in app: Exception on /_dash-update-component [POST]
    # Nov 3 04:04:08 PM  Traceback (most recent call last):
    # Nov 3 04:04:08 PM    File "/opt/render/project/src/.venv/lib/python3.10/site-packages/flask/app.py", line 2529, in wsgi_app
    # Nov 3 04:04:08 PM      response = self.full_dispatch_request()
    # Nov 3 04:04:08 PM    File "/opt/render/project/src/.venv/lib/python3.10/site-packages/flask/app.py", line 1825, in full_dispatch_request
    # Nov 3 04:04:08 PM      rv = self.handle_user_exception(e)
    # Nov 3 04:04:08 PM    File "/opt/render/project/src/.venv/lib/python3.10/site-packages/flask/app.py", line 1823, in full_dispatch_request
    # Nov 3 04:04:08 PM      rv = self.dispatch_request()
    # Nov 3 04:04:08 PM    File "/opt/render/project/src/.venv/lib/python3.10/site-packages/flask/app.py", line 1799, in dispatch_request
    # Nov 3 04:04:08 PM      return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)
    # Nov 3 04:04:08 PM    File "/opt/render/project/src/.venv/lib/python3.10/site-packages/dash/dash.py", line 1265, in dispatch
    # Nov 3 04:04:08 PM      ctx.run(
    # Nov 3 04:04:08 PM    File "/opt/render/project/src/.venv/lib/python3.10/site-packages/dash/_callback.py", line 450, in add_context
    # Nov 3 04:04:08 PM      output_value = func(*func_args, **func_kwargs)  # %% callback invoked %%
    # Nov 3 04:04:08 PM    File "/opt/render/project/src/src/skydivewx/app.py", line 286, in updateManifest
    # Nov 3 04:04:08 PM      return [screenshotImage(dropZone, width="100%")]
    # Nov 3 04:04:08 PM    File "/opt/render/project/src/src/skydivewx/components/manifest/manifestComponents.py", line 14, in screenshotImage
    # Nov 3 04:04:08 PM      src="data:image/png;base64, " + getBurbleScreenshot(dropZone.liveManifestUrl),
    # Nov 3 04:04:08 PM    File "/opt/render/project/src/src/skydivewx/utils/screenshotUtils.py", line 27, in getBurbleScreenshot
    # Nov 3 04:04:08 PM      driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
    # Nov 3 04:04:08 PM    File "/opt/render/project/src/.venv/lib/python3.10/site-packages/webdriver_manager/chrome.py", line 40, in install
    # Nov 3 04:04:08 PM      driver_path = self._get_driver_binary_path(self.driver)
    # Nov 3 04:04:08 PM    File "/opt/render/project/src/.venv/lib/python3.10/site-packages/webdriver_manager/core/manager.py", line 40, in _get_driver_binary_path
    # Nov 3 04:04:08 PM      file = self._download_manager.download_file(driver.get_driver_download_url(os_type))
    # Nov 3 04:04:08 PM    File "/opt/render/project/src/.venv/lib/python3.10/site-packages/webdriver_manager/drivers/chrome.py", line 32, in get_driver_download_url
    # Nov 3 04:04:08 PM      driver_version_to_download = self.get_driver_version_to_download()
    # Nov 3 04:04:08 PM    File "/opt/render/project/src/.venv/lib/python3.10/site-packages/webdriver_manager/core/driver.py", line 48, in get_driver_version_to_download
    # Nov 3 04:04:08 PM      return self.get_latest_release_version()
    # Nov 3 04:04:08 PM    File "/opt/render/project/src/.venv/lib/python3.10/site-packages/webdriver_manager/drivers/chrome.py", line 64, in get_latest_release_version
    # Nov 3 04:04:08 PM      determined_browser_version = ".".join(determined_browser_version.split(".")[:3])
    # Nov 3 04:04:08 PM  AttributeError: 'NoneType' object has no attribute 'split'
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")

    img_data = []

    driver = webdriver.Chrome(ChromeDriverManager(version='114.0.5735.90').install(), chrome_options=options)
    driver.get(url=burbleUrl)
    try:
        WebDriverWait(driver, 10).until(
            EC.invisibility_of_element_located((By.CLASS_NAME, "x-mask-msg"))
        )
        # TODO find a better way to wait for the page components to load
        time.sleep(5)
        screenshot = driver.get_screenshot_as_png()
        img_data.append(base64.b64encode(screenshot).decode())
    finally:
        driver.quit()

    return img_data[0]

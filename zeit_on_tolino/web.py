import tempfile
from pathlib import Path
from typing import Union

from selenium.webdriver import Firefox, FirefoxOptions
from selenium.webdriver.firefox.webdriver import WebDriver

DOWNLOAD_PATH = tempfile.gettempdir()


def get_webdriver(download_path: Union[Path, str] = DOWNLOAD_PATH) -> WebDriver:
    options = FirefoxOptions()
    options.headless = True
    options.set_preference("browser.download.folderList", 2)
    options.set_preference("browser.download.dir", str(download_path))
    webdriver = Firefox(options=options)
    return webdriver

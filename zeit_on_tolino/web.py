import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Union

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.firefox.webdriver import WebDriver

DOWNLOAD_PATH = tempfile.TemporaryDirectory().name


@dataclass
class Delay:
    small: int = 3
    medium: int = 10
    large: int = 30
    xlarge: int = 200


def get_webdriver(download_path: Union[Path, str] = DOWNLOAD_PATH) -> WebDriver:
    options = ChromeOptions()
    prefs = {"download.default_directory" : f"{download_path}/"}
    options.add_experimental_option("prefs",prefs)
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36")
    webdriver = Chrome(options=options)
    setattr(webdriver, "download_dir_path", str(download_path))
    return webdriver

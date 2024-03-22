from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait

from webdriver_manager.chrome import ChromeDriverManager

options = ChromeOptions()
options.add_argument('log-level=3')
options.add_argument("start-maximized")
options.add_argument("--disable-gpu")

driver = Chrome(options, service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 20)
import pytest
import tempfile
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
from pages.text_box_page import TextBoxPage

@pytest.fixture
def driver():
    options = Options()

    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/114.0.5735.90 Safari/537.36"
    )
    user_data_dir = tempfile.mkdtemp(prefix="chrome-user-data-")
    options.add_argument(f"--user-data-dir={user_data_dir}")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.set_page_load_timeout(30)

    yield driver
    driver.quit()



@pytest.fixture
def login_page(driver):
    return LoginPage(driver)

@pytest.fixture
def text_box(driver):
    return TextBoxPage(driver)

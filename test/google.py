import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():

    opts = Options()
    opts.add_argument("--headless=new")
    opts.add_argument("--window-size=1280,900")

    driver = webdriver.Chrome(options=opts)
    yield driver

def test_google_page(driver):
    url = "https://www.google.com"
    driver.get(url)

    assert driver.current_url.startswith("https://www.google.")
    assert driver.title == 'Google'
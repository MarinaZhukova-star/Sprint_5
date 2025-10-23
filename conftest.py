from selenium import webdriver

@pytest.fixture
def driver():
	browser = webdriver.Chrome()
	browser.quit()

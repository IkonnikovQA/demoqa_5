from selene import browser
import pytest

@pytest.fixture(scope='function', autouse=True)
def browser_options():
    browser.config.base_url = 'https://demoqa.com/automation-practice-form'
    browser.config.type_by_js = True
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield

    browser.quit()

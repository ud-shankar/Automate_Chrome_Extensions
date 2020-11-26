import time
import pytest
from pytest_bdd import given, when, then, scenario
from selenium.webdriver.common.keys import Keys
from Drivers.chromedriver import driver
import keyboard


@scenario("../Feature/Chrome_extension.feature", "Test one of the feature of the extension - Saka")
def test_web_page():
    pass


@given("User adds the extension and opens the browser")
def initializing():
    pass                                #Chrome driver initialization and other settings are done in Drivers folder


@when("User opens and navigates to multiple pages in multiple tabs")
def new_tab():
    driver.get("https://github.com/ud-shankar?tab=repositories")
    driver.execute_script("window.open('');")
    # Switch to the new window
    driver.switch_to.window(driver.window_handles[1])
    driver.get("https://oslash.com/")
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[2])
    driver.get("https://www.google.com/")
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[3])
    driver.get("https://www.facebook.com/")


@when("User navigates to the popup frame of the extension")
def saka_frame():
    time.sleep(2)
    keyboard.send('ctrl+space', do_press=True, do_release=True)


@when("User enter word and search for the tab opened")
def search_tab():
    time.sleep(2)
    driver.switch_to.frame(driver.find_element_by_id("saka"))
    driver.find_element_by_id("search-bar").send_keys("oslash")
    driver.find_element_by_id("search-bar").send_keys(Keys.ENTER)
    time.sleep(2)


@then("User verify the tab has been switched successfully")
def verification():
    driver.switch_to.window(driver.window_handles[1])
    oslash = driver.find_element_by_xpath("//h1[@class='mr-20 text-6xl font-semibold leading-tight']").text
    if "Get what’s important" in oslash:
        print(oslash)
        pass


@pytest.fixture(scope="session", autouse=True)
def posttest(request):
    yield driver
    driver.quit()
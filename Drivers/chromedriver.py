from selenium import webdriver
from selenium.webdriver.chrome.options import Options


chromedriver = 'C:/Selenium/chromedriver.exe'               #path where your local chrome driver is saved in the system
# popup_window_url = "chrome-extension://mgijmajocgfcbeboacabfgobmjgjcoja/browser_action.html"        #Copy the path to your popup html file
# options_url = "chrome-extension://mgijmajocgfcbeboacabfgobmjgjcoja/options.html"        #Copy path to your options .html file
crx_path = r"C:\Saka\Drivers\Saka_extension.crx"                      #absolute path to your .crx file in your local project


chrome_options = Options()
chrome_options.add_argument("start-maximized")
chrome_options.add_extension(crx_path)
driver = webdriver.Chrome(executable_path=chromedriver, options=chrome_options)

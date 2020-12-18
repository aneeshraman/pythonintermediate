# Selenium is really very fast.

# Importing the selenium webdriver.
from selenium import webdriver

# Creating a test browser.
driver = webdriver.Chrome()

# Maximizing the browser.
driver.maximize_window()

# Getting the url for the browser
url = "https://rahulshettyacademy.com/#/index"
driver.get(url)

# Printing out the title of the current page.
print(driver.title)

# Printing out the current url.
print(driver.current_url)

# Getting another url for more practice in selenium.
url = "https://rahulshettyacademy.com/AutomationPractice/"
driver.get(url)

# Minimizing the window.
driver.minimize_window()

# Getting back to the previous window, i.e. the "https://rahulshettyacademy.com/#/index"
driver.back()

# Refreshing the screen.
driver.refresh()

# Closing the current window. To quit all the windows use driver.quit()
driver.close()

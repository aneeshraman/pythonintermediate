# Importing webdriver from selenium (This webdriver package is used for
# invoking browser etc.)
from selenium import webdriver

# Creating a chrome browser.
driver = webdriver.Chrome()

# Creating a firefox browser.
# driver = webdriver.Firefox()

# Creating a Microsoft Edge browser.
# driver = webdriver.Edge()

# Maximizing the window.
driver.maximize_window()

# Getting the url in the browser.
driver.get("https://rahulshettyacademy.com/#/index")

# Extracting the title of the webpage and printing it.
print(driver.title)

# As sometimes cyber attacks can occur so we would check the current url of the page and would print it.
print(driver.current_url)

# Now getting another url.
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# Minimizing the window.
driver.minimize_window()

# Going to the previous url.
driver.back()

# Refreshing the page.
driver.refresh()

# Closing the chrome window.
driver.close()

# Quitting all the windows.
# driver.quit()

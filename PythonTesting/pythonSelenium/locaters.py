# Importing the webdriver from selenium.
from selenium import webdriver
# Also importing the By class (This class is used for locating elements)
from selenium.webdriver.common.by import By

# Creating the chrome browser.
driver = webdriver.Chrome()

# Getting the url for the site.
driver.get("https://rahulshettyacademy.com/angularpractice/")

# So the methods to locate a element are as follows:
# 1. Id
# 2. Name
# 3. Xpath
# 4. CSS
# 5. Class Name
# 6. Link Text

# But 3. Xpath,
#     4. CSS
#     6. Link Text
# Are a little different so we would leave them aside for now.

# To create a web element in python we need the value of one of those methods given above. We should also know
# that which method is available. Sometimes there are many elements have the same value of the same method.
# In that case the selenium doesn't get confused and picks the first element but if your element is second or
# third in such lists then to verify that this does not happen we can use the Xpath, CSS which are special
# because we can check if they would work well.

# Creating the name value for the name text box.
name_value = "name"

# Now creating the web element for the name text box.
name_text_box = driver.find_element(By.NAME, name_value)

# Now typing the name in the text box.
name_text_box.send_keys("Aneesh")

# Creating the name value for the email text box.
email_value = "email"

# Now creating the web element for the email text box.
email_text_box = driver.find_element(By.NAME, email_value)

# Now typing the email in the text box.
email_text_box.send_keys("aneeshraman17mar@gmail.com")

# Creating the id value for the password text box.
password_value = "exampleInputPassword1"

# Now creating the web element for the password text box.
password_text_box = driver.find_element(By.ID, password_value)

# Now typing the password in the password text box.
password_text_box.send_keys("aneeshti123")

# Creating the id value for the love icecreams check box.
love_icecreams_value = "exampleCheck1"

# Now creating the web element for the love icecreams check box.
love_icecreams_check_box = driver.find_element(By.ID, love_icecreams_value)

# Now clicking the check box if I love icecreams.
love_icecreams = True
if love_icecreams:
    love_icecreams_check_box.click()

# Starting will Xpath and CSS.
# These are special because they do not depend on what attribute has the developer used.
# We can use these with any property. In these we have a syntax.

# The syntax for CSS is.
# tagname[attribute='value']

# Importing webdriver from selenium
from selenium import webdriver

# Importing By from selenium.
from selenium.webdriver.common.by import By

# Creating a chrome browser.
driver = webdriver.Chrome()

# Getting the url.
driver.get("https://login.salesforce.com/")

# Creating a css selector for the username.
username = "input[id='username']"

# Creating the web element for the username.
username_text_box = driver.find_element(By.CSS_SELECTOR, username)

# Typing my username into the text box.
username_text_box.send_keys("aneeshraman")

# Creating a css selector for the password.
password = "input[id='password']"

# Creating the web element for the password.
password_text_box = driver.find_element(By.CSS_SELECTOR, password)

# Typing my password into the text box.
password_text_box.send_keys("aneeshti123")

# Note: To clear the input of a text box use the clear method.
# Clearing the password text box.
password_text_box.clear()

# Note: If their is a link text in your page then you can grab the whole element using the link text. This is the
# easiest of all.

# Creating the link text for the 'forgot your password'.
forgot_password = "Forgot Your Password?"

# Creating the web element using the link text.
forgot_password_link = driver.find_element(By.LINK_TEXT, forgot_password)

# Clicking on the link.
forgot_password_link.click()

# Note: Their is a great feature in xpath, which is not in CSS. This feature is that we can find elements using
# the text written in them.
# Example.
# Syntax //tagname[text()='whatever text you have']

# Creating the xpath for the cancel button in forgot password link.
cancel_forget_password = "//a[text()='Cancel']"

# Creating the web element for the cancel forget password.
cancel_forget_password_check_box = driver.find_element(By.XPATH, cancel_forget_password)

# Clicking on cancel forget password.
cancel_forget_password_check_box.click()

# Very Important
# If there are no such tags you rely on. Then you can take the parent tags help. That means that first you can
# reach the destination of the parent tag and then you can reach the destination of the tag you wanted to reach.
# Note: We can use grandparents for the above situation. In that you can just replace all the parent stuff with
# the grandparent stuff.

# The syntax for the above is (xpath_of_the_parent)/tagname. Better way is
# //parent_tagname[@parent_attribute='parent_value']/child_tagname
# The syntax for the above is (css_of_the_parent) tagname. Better way is
# parent_tagname[parent_attribute='parent_value'] child_tagname

# Using the above syntax for getting the word username.
word_user_name = "//div[@id='usernamegroup']/label"

# Also creating the css for this so that I can practice.
word_user_name = "div[id='usernamegroup'] label"

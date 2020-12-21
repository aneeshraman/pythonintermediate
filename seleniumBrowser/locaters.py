# Importing the webdriver required for automation.
from selenium import webdriver
# Importing the By required for automation.
from selenium.webdriver.common.by import By

# Creating the chrome window.
driver = webdriver.Chrome()

# Now getting the url.
driver.get("https://rahulshettyacademy.com/angularpractice/")

# Now maximizing the window.
driver.maximize_window()

# Very Important note.
# To create the css locator the syntax is "tagname[attribute='value']"

# Creating the css locator for name.
name = "input[name='name']"

# Now creating the element for the name text box.
name_text_box = driver.find_element(By.CSS_SELECTOR, name)

# Now typing my name into the name_text_box that is "Aneesh"
name_text_box.send_keys("Aneesh")

# Creating the name locator for email.
email = "email"

# Now creating the element for the email text box.
email_text_box = driver.find_element(By.NAME, email)

# Now typing my email id into the email_text_box that is "aneeshraman17mar@gmail.com"
email_text_box.send_keys("aneeshraman17mar@gmail.com")

# Creating a css locator for the password.
password = "input[id='exampleInputPassword1']"

# Now creating the element for the password text box.
password_text_box = driver.find_element(By.CSS_SELECTOR, password)

# Now typing my password into the password_text_box that is "aneeshti123"
password_text_box.send_keys("aneeshti123")

# Creating the id for ice_cream check box.
ice_cream = "exampleCheck1"

# Now creating teh element for the iceCream check box.
ice_cream_check_box = driver.find_element(By.ID, ice_cream)

# Now clicking the ice_cream check box.
ice_cream_check_box.click()

# Creating the css selector for student check box.
student = "input[id='inlineRadio1']"

# Now creating a web element for the student check box.
student_check_box = driver.find_element(By.CSS_SELECTOR, student)

# Now clicking on the student element.
student_check_box.click()

# Creating the css selector for submitting.
# Now I am always using css selector because we can use it in console by command $("css_selector").
# Creating the xpath for submitting.
# Now this is just in case if I don't want to use css selector for some reason else css selector is the best.
# So the format of xpath is. //tagname[@attribute='value']
# The xpath can be accessed in the console using the command $x("xpath")
submit = "//input[@type='submit']"

# Now creating a web element for the submit button.
submit_button = driver.find_element(By.XPATH, submit)

# Now clicking on the submit button.
submit_button.click()

# Now verifying whether our text was valid.
# To do that we have to get success text. Now creating the css selector for the following text box showing up.
text_check = "div[class='alert alert-success alert-dismissible']"

# Now creating the web element.
text_check_box = driver.find_element(By.CSS_SELECTOR, text_check)

# Now printing out the text.
print(text_check_box.text)

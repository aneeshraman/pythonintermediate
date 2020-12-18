# Importing the selenium webdriver and other import libraries.
from selenium import webdriver
# This is so that we can search for text boxes.
from selenium.webdriver.common.by import By


# Creating a browser window.
driver = webdriver.Chrome()

# Loading the practice url.
driver.get("https://rahulshettyacademy.com/angularpractice/")

# Maximizing the window.
driver.maximize_window()

# Finding out the textbox by name and as our objective is to type a name so I would
# use the send_keys function to type the name.
name = driver.find_element(By.NAME, "name")
name.send_keys("Aneesh")


# In the same way finding out the email.
email = driver.find_element(By.NAME, "email")
email.send_keys("aneeshraman17mar@gmail.com")

# In the same way finding out the password.
password = driver.find_element(By.ID, "exampleInputPassword1")
password.send_keys("aneeshti123")

# In the same way finding out the iceCream button.
iceCream = driver.find_element(By.ID, "exampleCheck1")
iceCream.click()

# Very Important.
# CSS Selector format with usage. tagname[attribute='value']
# Xpath Selector format with usage. //tagname[@attribute='value']


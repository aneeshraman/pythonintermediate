from teamsSelenium import webdriver
from teamsSelenium.webdriver.common.by import By
import keyboard
import pyautogui

# Set webdriver to use
driver = webdriver.Chrome()
driver.maximize_window()

# Go to the site and get ready to type
driver.get("https://www.keybr.com/multiplayer")


# This is where the magic happens
def type(text_class):
    text = driver.find_element(By.CLASS_NAME, text_class).text

    for char in text:
        # Keybr uses ␣ for spaces. So if ␣ occurs, type a space. Otherwise, write
        if char == "␣":
            pyautogui.hotkey('space')

        elif char == "↵":
            pyautogui.hotkey("enter")
        else:
            pyautogui.typewrite(char)


print("Press alt+z to start the bot")

# Call the type() function upon hitting the hotkey
while 1:
    keyboard.wait('alt+z')
    type("TextInput-fragment")

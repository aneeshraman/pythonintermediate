# Importing the pyautogui library.
import pyautogui

print("To take max coordinates, open your python and type pyautogui.displayMousePosition()")
print("After that, you can take your cursor to the down-right corner of your screen and enter them"
      "in the below prompt.")
max_coordinates = input("Please enter the max-coordinates of your screen with "
                        "x and y separated with space: ").split()

x, y = max_coordinates
x, y = int(x) / 1365, int(y) / 767


class DesktopWhatsappBot:
    pass


# Creating the web whatsapp function
class WebWhatsappBot:
    def __init__(self, browser_name):
        self.current_rgb = pyautogui.screenshot().getpixel(pyautogui.position())

        # Please give the browser name.
        self.browser_name = browser_name

        # Opening the browser
        pyautogui.hotkey("win")
        pyautogui.typewrite(f"apps: {self.browser_name}")
        pyautogui.hotkey("enter")
        pyautogui.sleep(1)
        pyautogui.typewrite("web.whatsapp.com")
        pyautogui.hotkey("enter")

    def automate(self, phone_numbers, message):
        """
        This method sends text messages to any whatsapp recipient.
        """
        for self.phone_number in phone_numbers:
            pyautogui.click(77 * x, 154 * y)
            if self.current_rgb != (255, 255, 255):
                pyautogui.typewrite(self.phone_number)
                pyautogui.hotkey("enter")
                pyautogui.click(535, 696)
                if self.current_rgb != (255, 255, 255) and isinstance(message, int):
                    pyautogui.typewrite(message)
                    pyautogui.hotkey("enter")

                elif isinstance(message, list) and self.current_rgb != (255, 255, 255):
                    for line in message:
                        pyautogui.typewrite(line)
                        if line != message[-1]:
                            pyautogui.hotkey("alt", "enter")
                    pyautogui.hotkey("enter")

            else:
                print("Something blocked the automation")
                break

    def automate_image(self, phone_numbers, message):
        """Please copy the image before using this function"""
        for self.phone_number in phone_numbers:
            pyautogui.click(77 * x, 154 * y)
            if self.current_rgb != (255, 255, 255):
                pyautogui.typewrite(self.phone_number)
                pyautogui.hotkey("enter")
                pyautogui.click(535, 696)
                if self.current_rgb != (255, 255, 255) and isinstance(message, int):
                    pyautogui.typewrite(message)

                elif isinstance(message, list) and self.current_rgb != (255, 255, 255):
                    for line in message:
                        pyautogui.typewrite(line)
                        if line != message[-1]:
                            pyautogui.hotkey("alt", "enter")

                pyautogui.hotkey("ctrl", "v")
                pyautogui.sleep(3)
                pyautogui.hotkey("enter")


            else:
                print("Something blocked the automation")
                break

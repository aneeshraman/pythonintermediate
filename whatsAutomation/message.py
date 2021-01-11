import pyautogui

chosen_option = pyautogui.confirm("Choose from the options below",
                                  buttons=["Whatsapp", "Whatsapp Desktop", "Whatsapp "
                                                                           "Web"])
phone_number = pyautogui.prompt("Enter the phone number whom you want to send the message to")

max_coordinates = pyautogui.prompt("Enter the max coordinates separated with space").split()


def one_message_web(phone_num, max_coord, message):
    iter(max_coord)
    max_x, max_y = max_coord
    number_x, number_y = (86 / 1365) * max_x, (245 / 767) * max_y
    pyautogui.click(number_x, number_y)


def one_message_whatsapp_desktop(phone_num, max_coord, message):
    iter(max_coord)
    max_x, max_y = max_coord
    number_x, number_y = (79 / 1365) * max_x, (109 / 767) * max_y
    pyautogui.click(number_x, number_y)
    pyautogui.typewrite(phone_num)


def main():
    if chosen_option == "Whatsapp Desktop":
        one_message_whatsapp_desktop(phone_number, max_coordinates, message)

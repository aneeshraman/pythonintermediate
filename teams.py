# Importing the selenium library and By class. I am also importing pyautogui because I wanted to automate everything.
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui
import numpy as np

driver = webdriver.Chrome()

driver.maximize_window()

# Please enter the url.
driver.get(
    "https://teams.microsoft.com/l/meetup-join/19%3ab0319b3a113e4337bf741a36dccec885%40thread.tacv2/1608051239754"
    "?context=%7b%22Tid%22%3a%225fd10a7a-9625-46f7-b7f9-551a2760c887%22%2c%22Oid%22%3a%22ebde4543-5cd9-4f91-9054"
    "-0ef96de57685%22%7d")

pyautogui.hotkey("esc")

pyautogui.sleep(1)

pyautogui.click(925, 415)

pyautogui.sleep(17)

pyautogui.click(308, 188)

pyautogui.sleep(3)

pyautogui.click(655, 717)

pyautogui.sleep(5)

pyautogui.click(548, 379)

pyautogui.typewrite("ANEESHRAMAN.W11017.VIIIC@dpsrohini.onmicrosoft.com")

pyautogui.hotkey("enter")

pyautogui.sleep(2)

pyautogui.click(523, 417)

pyautogui.typewrite("lordganesha@1")

pyautogui.hotkey("enter")

pyautogui.sleep(3)

pyautogui.hotkey("enter")

pyautogui.sleep(10)

pyautogui.click(502, 716)

pyautogui.sleep(10)

pyautogui.click(877, 575)

pyautogui.sleep(5)

pyautogui.click(1132, 681)

pyautogui.sleep(5)

pyautogui.click(306, 165)

pyautogui.sleep(10)

# noinspection SpellCheckingInspection
nominal = [
    "AANYA JAIN",
    "AARAV DUA",
    "AAYUSH GUPTA",
    "AKSHITA PURI",
    "ANEESH RAMAN",
    "ANSHIKA",
    "ARNAV SHARMA",
    "AROUSH SETH",
    "ARSHIA KHAUND",
    "ARYAN WALIA",
    "AVNI AGGARWAL",
    "BHAVYA ARORA",
    "BHAVYA SHARMA",
    "DREESHTI KAPOOR",
    "DIPIN PANDEY",
    "DEVANSH PANDEYA",
    "EKAANSH GABA",
    "ISHANI JHA",
    "IHINA ROY",
    "LAKSHAY MALHOTRA",
    "KASHIKA TAYAL",
    "JIAH BAJAJ",
    "MAHI WADHWA",
    "PANKAJ",
    "PARTH GUPTA",
    "PRATHAM SHARMA",
    "RANVEER SOLANKI",
    "RENNIE GUPTA",
    "RIHIT RAI",
    "RISHABH SINGH",
    "ROUNAK BISWAS",
    "RUDRA VIJ",
    "SANYAM MATHUR",
    "SASHVI SINGLA",
    "SHARVI SINGHAL",
    "SUMAN",
    "UNNABH BHALLA",
    "VANSHIKA ARYA",
    "YANA VIG",
    "YUVRAJ MALIK"
]

present = []
absentees = []

for attendee in driver.find_elements(By.CLASS_NAME, "ts-user-name"):
    present.append(attendee.text)

for classmate in nominal:
    if classmate not in present:
        absentees.append(classmate)

df = pd.DataFrame(data={"Absentees": absentees}, index=np.arange(1, len(absentees) + 1))

df.to_excel("Attendance.xlsx")

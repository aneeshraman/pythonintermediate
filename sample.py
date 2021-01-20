from WhatsAutomation import message
import time

Bot = message.WebWhatsappBot("Chrome")
time.sleep(5)
Bot.automate(["+7011040802"], ["Automated Message", "Hello"])

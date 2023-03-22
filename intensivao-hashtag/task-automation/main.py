import pyautogui as auto
import pyperclip
import pandas as pd
import time

# mainly functions of pyautogui
#
#pyautogui.click # click mouse
#pyautogui.write # write text
#pyautogui.press # press key
#pyautogui.hotkey("ctrl", "t") # press key commands

# Open the file for reading
with open('./infos.txt', 'r', encoding='utf-8') as file:
    # Read the contents of the file into a variable
    file_contents = file.read()
# Save the contents of the file in separeted lines
infos = file_contents.splitlines()

# Saves the From e-mail
email_from = infos[1]
password_from = infos[2]

# Saves the To e-mail
email_to = infos[5]

# Saves e-mail content
email_title = infos[8]
email = ''.join([line+'\n' for line in infos[10:]])

# Read data base, 'sep' sets the separator character
table = pd.read_csv(r'./dataBase/Compras.csv', sep=';')

# Select a collum and sum they values
total_spent = table["ValorFinal"].sum()
amount = table["Quantidade"].sum()
average_price = total_spent/amount

# Init
auto.PAUSE = 1
time.sleep(2)

## Open a new incognito window in Chrome (so that pages come without any previously added information) through a new normal Chrome window ##

# Open new normal Chrome window
auto.press("win")
auto.write("chrome")
auto.press('enter')
time.sleep(2)

# Open new incognito Chrome window
auto.hotkey("ctrl", "shift", "n")
time.sleep(2)
# Make it fullsize
auto.hotkey("alt", "space")
auto.hotkey("x")

# Go to gmail
auto.hotkey("ctrl", "l")
auto.write("https://www.google.com/intl/pt-BR/gmail/about/")
auto.press("enter")
time.sleep(2)

# Do login
auto.click(x=1430, y=125)
time.sleep(2)
pyperclip.copy(email_from)
auto.hotkey("ctrl", "v")
auto.click(x=1090, y=725)
time.sleep(2)
pyperclip.copy(password_from)
auto.hotkey("ctrl", "v")
auto.click(x=1090, y=710)
time.sleep(6)

# Write E-mail
auto.click(x=90, y=200)
pyperclip.copy(email_to)
auto.hotkey("ctrl", "v")
auto.hotkey("tab")
pyperclip.copy(email_title)
auto.hotkey("ctrl", "v")
auto.hotkey("tab")
pyperclip.copy(email)
auto.hotkey("ctrl", "v")
auto.write(f"\nTotal spent: {total_spent:,.2f}")
auto.write(f"\nAmount: {amount:,.2f}")
auto.write(f"\nAverage price: {average_price:,.2f}")

# Send
auto.hotkey("ctrl", "enter")
time.sleep(2)

# Close the two previously opened Chrome windows.
auto.hotkey("ctrl", "w")
auto.hotkey("ctrl", "w")
#!/usr/bin/env python3

#import pyautogui
import smtplib
import time

confirm = False
phone_carriers = {'A':'@mms.att.net', 'B':'@tmomail.net', 'C':'@vtext.com','D':'@pm.sprint.com\n'}
#pyautogui.FAILSAFE = True

# time.sleep(2)
# print(pyautogui.position())

# pyautogui.click(454, 718)
# pyautogui.click(454, 718)

print("program will not run if these are incorrect")

email = input("please enter email: ")

passW = input("please enter pass: ")



while confirm == False:
    number = input("Please enter their phone number (no spaces or dashes) ")

    while number == ' ':
        print("try again")

        number = input("Please enter their phone number (no spaces or dashes) ")

    carrier = carrier = input('\nA)At&t\nB)T-Mobile\nC)Verizon\nD)Sprint\nWhat is your phone carrier? ').upper()

    for k,v in phone_carriers.items():
        if carrier == k:
            user_carrier = v

    ans = input("Is the number: " + number + ".\nIs the carrier: " + carrier + ". (y / n)" ).upper()

    if ans == 'N':
        continue
    else:
        confirm = True

rec = number + user_carrier

print("Program will run shortly. Close out window to stop the program or press ctrl + c.")

with open('shrek.txt', 'r') as file:
    for line in file:
        for word in line.split():
            server = smtplib.SMTP("smtp.gmail.com", 587)

            server.starttls()

            server.login(email, passW)

            server.sendmail('LOL', rec, word)

            # pyautogui.typewrite(word, interval=0)
            #
            # time.sleep(0.2)
            #
            # pyautogui.typewrite(['enter'], interval=0)

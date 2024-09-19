import pyfiglet
import os
import time
import re
from telethon.sync import TelegramClient
from cfonts import render, say

Z = '\033[1;31m'
F = '\033[2;32m'
B = '\033[2;36m'
X = '\033[1;33m'
C = '\033[2;35m'

def JOK(text, delay, add_new_line=True):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    if add_new_line:
        print("\n", end="", flush=True)

logo1 = pyfiglet.figlet_format('            eva ')
logo2 = pyfiglet.figlet_format('         		&  ')
logo3 = pyfiglet.figlet_format('            SCRAPER ')

print(Z + logo1)
print(B + logo2)
print(F + logo3)

JOK(C + "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━", 0.07, True)

print(X + '━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

api_id = '29744282'
api_hash = '2316be0479f28606fd8969f3d660d70c'

channel_username = input("Enter the channel name: ")

file_name = input("Enter the file name to save the scraped messages: ")

bin_to_scrape = input("Enter the BIN to scrape (press 'n' to skip): ")

num_messages = int(input("Enter the number of messages to save: "))

client = TelegramClient('session_name', api_id, api_hash)

client.start()

entity = client.get_entity(channel_username)

with open(file_name, 'a', encoding='utf-8') as file:
    count = 0
    for message in client.iter_messages(entity):
        if message.text:
            if bin_to_scrape.lower() == 'n' or bin_to_scrape.lower() in message.text.lower():
                matches = re.findall(r'(\d+\|\d+\|\d+\|\d+)', message.text)
                if matches:
                    # Write the extracted text to the file
                    file.write(matches[0] + '\n')

                    count += 1
                    if count == num_messages:
                        break

client.disconnect()

logo = pyfiglet.figlet_format('PADI_CC')
print(logo)


#made by @xx_Anon_xx
#support @paid_cc

import requests
import time
import random
from bs4 import BeautifulSoup
from colorama import Fore
from colorama import Style

number = random.choice(range(2, 148))
if number < 10:
    number = f"00{number}"
elif number < 100:
    number = f"0{number}"

fable = requests.get(f"http://read.gov/aesop/{number}.html")
soup = BeautifulSoup(fable.text, "html.parser")

text = []
contents = soup.find_all("p")
for section in contents:
    text.append(section.text)
text = " ".join(text)

print(f"{Fore.LIGHTBLUE_EX}{text}{Style.RESET_ALL}")

start_time = time.time()

user_text = input(f"{Style.BRIGHT}[Type:]->{Style.RESET_ALL}")

total_time = time.time() - start_time

wrong_count = 0
for i in range(len(user_text.split(" "))):
    try:
        if text.split(" ")[i] != user_text.split(" ")[i]:
            wrong_count += 1
    except IndexError:
        wrong_count += 1

accuracy = (len(user_text.split(" "))-wrong_count)/len(user_text.split(" ")) * 100

print(f"{Fore.YELLOW}Time spent (seconds): {Style.BRIGHT}{round(total_time)}{Style.RESET_ALL}")
print(f"{Fore.YELLOW}Accuracy (%): {Style.BRIGHT}{round(accuracy)}{Style.RESET_ALL}")
print(f"{Fore.YELLOW}Words per minute (wpm): {Style.BRIGHT}{round(len(user_text.split(' '))/total_time * 60)}\
        {Style.RESET_ALL}")
print(f"{Fore.YELLOW}Fable: {Style.BRIGHT}{soup.find('h1').text}{Style.RESET_ALL}")




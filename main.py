import requests
import time
import random
from bs4 import BeautifulSoup

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

print(f'\033[94m{text}\033[0m')

start_time = time.time()

user_text = input("\033[1m[Type:]->\033[0m")

total_time = time.time() - start_time

print(f"\033[93mTime spent (seconds): {round(total_time)}")

wrong_count = 0

for i in range(len(user_text.split(" "))):
    try:
        if text.split(" ")[i] != user_text.split(" ")[i]:
            wrong_count += 1
    except IndexError:
        wrong_count += 1

accuracy = (len(user_text.split(" "))-wrong_count)/len(user_text.split(" ")) * 100

print(f"{round(accuracy)}% accuracy")
print(f"{round(len(user_text.split(' '))/total_time * 60)} words per minute (wpm)\033[0m")




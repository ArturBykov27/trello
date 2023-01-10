import requests
import datetime


ARTUR = "58b6e5d80ae235709ceefab5"
MARINA = "5c80e967c19bbc148fafa2b4"
YULIA = "5e33d4d6cbea3223847106ff"
KSENIA = "5c20beeae434c930084af5aa"
VIKA = "5ddcf34e36599986c8988839"
DIMA = "5f0c4f9757297d65c50a0cf7"

# with open("text.txt", "r") as q:
#     lines = q.readlines()
# lines.pop(0)
# with open("text.txt", "w") as q:
#     q.writelines(lines)



tab =requests.get(url="https://api.sheety.co/7dc395588fff5901e0d17afdfffa07a5/1CQueue/лист1")
print(tab.json())

today = datetime.date.today().strftime("%d%m%Y")



for name in tab.json()['лист1']:
    with open("text.txt", "a") as queue:
        queue.write(name[f"{today}"])
        queue.write("\n")
        print(name[f"{today}"])
# list = []
# for v in new_q:
#     list.append(globals()[v])
#
#
# print(list)
# def remove_m():
#
import time
import random
import json
import os

data = {}

print("This program is made by Mateitzu")
time.sleep(2)
os.system("cls")
answer = input("You need this program, now, for : StatusOrganiser, other: ")
if answer.lower() == "statusorganiser":
    while True:
        user = input("Enter user(type format.... for generating the file): ")
        if user.lower() != "format....":
            if user not in data:
                data[user] = {"banned": False}
                print("User saved in memory")
            else:
                print("Cannot add 2 users with the same username!")
        else:
            name = input("Enter the file's name: ")
            with open(name + ".json", "w") as file:
                json.dump(data, file, indent=2)
                print("file generated, quitting...")
                time.sleep(2)
                quit()

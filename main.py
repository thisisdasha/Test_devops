import functions
import time
import os

arr = []  # an array in which directory lines are stored
with open("file.txt") as file:
    arr = [row.strip() for row in file]

# checking the file for emptiness
if os.stat("file.txt").st_size == 0:  # if empty
    print("Phone book is empty")
    print("Please choose the number of the desired operation:")
    fl = True
    while (fl):
        command = input("1 - Add new record to the phonebook\n2 - exit\n")
        if command == '1':
            line = input("Enter name and surname:\n")
            line = line.strip()
            line = line + " " + input("Enter phone number:\n")
            line = line.strip()
            line = line + " " + input("Enter date of birth:\n")
            line = line.strip()
            functions.add(line, arr)
            fl = False
        elif command == '2':
            quit()
        elif command != '1' and command != '2':
            print("Unknown command")

# file is not empty
if os.stat("file.txt").st_size != 0:
    while (True):
        print("Please choose the number of the desired operation:)")
        print("1 - Add new record\n"
              "2 - Introduce some change to the records\n"
              "3 - Delete")
        print(
            "4 - Search phonebook entries\n"
            "5 - Show all phonebook entries\n"
            "6 - Find out the age of a person\n"
            "7 - View contacts by age\n8 -Exit")
        command = input()
        if command == '1':
            line = input("Enter name and surname:\n")
            line = line.strip()
            line = line + " " + input("Enter phone number:\n")
            line = line.strip()
            line = line + " " + input("Enter date of birth:\n")
            line = line.strip()
            print(functions.add(line, arr))
        if command == '2':
            functions.change(arr)
        if command == '3':
            functions.delete(arr)
        if command == '4':
            functions.find(arr)
        if command == '5':
            functions.show(arr)
        if command == '6':
            functions.age(arr)
        if command == '7':
            functions.viewAge(arr)
        if command == '8':
            quit()

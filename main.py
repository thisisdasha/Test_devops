import time
import os


class Contact(object):
    name = None
    surname = None
    phoneNumber = None
    dateOfBirth = None

    def __init__(self, line):
        tmp = line.split()
        self.name = tmp[0]
        self.surname = tmp[1]
        self.phoneNumber = tmp[2]
        self.dateOfBirth = tmp[3]

    def showContact(self):
        print(self.name + "\t\t" + self.surname + "\t\t" + self.phoneNumber + "\t\t" + self.dateOfBirth)


arr = []  # an array in which directory lines are stored
with open("file.txt") as file:
    arr = [row.strip() for row in file]


# phone book features
def add(line):
    tmpline = line.split()
    sizetmpline = len(tmpline)
    if (sizetmpline != 4):
        print("Invalid input")
        return
    line = line.title()  # first letter uppercase
    newContact = Contact(line)  # check for record existence
    date = newContact.dateOfBirth  # date validation
    try:
        valid_date = time.strptime(date, '%d/%m/%Y')
    except ValueError:
        print('Invalid date!')
        return

    contName = len(newContact.name)  # name validation
    for i in range(contName):
        if (not ((newContact.name[i] >= 'A' and newContact.name[i] <= 'Z') or (
                newContact.name[i] >= 'a' and newContact.name[i] <= 'z') or (
                         newContact.name[i] <= '9' and newContact.name[i] >= '0'))):
            print("Invalid name")
            return
    contName = len(newContact.surname)  # surname verification
    for i in range(contName):
        if (not ((newContact.surname[i] >= 'A' and newContact.surname[i] <= 'Z') or (
                newContact.surname[i] >= 'a' and newContact.surname[i] <= 'z') or (
                         newContact.surname[i] >= '0' and newContact.surname[i] <= '9'))):
            print("Invalid surname")
            return
    if (len(newContact.phoneNumber) == 11):  # checking the correctness of the phone number

        for i in range(11):
            if (not (newContact.phoneNumber[i] <= '9' and newContact.phoneNumber[i] >= '0')):
                print("Invalid phone number")
                return
    if (len(newContact.phoneNumber) == 12):

        if (newContact.phoneNumber[0] != '+'):
            print("Invalid phone number")
            return
        if (newContact.phoneNumber[1] != '7'):
            print("Invalid phone number")
            return
        for i in range(2, 12):
            if (not (newContact.phoneNumber[i] <= '9' and newContact.phoneNumber[i] >= '0')):
                print("Invalid phone number")
                return
        # AutoCorrect +7 to 8
        newContact.phoneNumber = '8' + newContact.phoneNumber[2:]
        line = newContact.name + " " + newContact.surname + " " + newContact.phoneNumber + " " + newContact.dateOfBirth

    if (len(newContact.phoneNumber) != 11 and len(newContact.phoneNumber) != 12):
        print("Invalid phone number")
        return

    for i in arr:
        contact = Contact(i)
        # if the contact with the entered first and last name is already in the directory
        if (contact.name == newContact.name and contact.surname == newContact.surname):
            print("Warning\nA contact with the same name already exists!")
            command = 0
            while (command != '2' or command != '1'):
                print("Please choose the number of the desired operation:")
                command = input("1 - If you want to make changes\n2 - To return to the main menu\n")
                if command == '1':
                    change()
                    return
                if command == '2':
                    return
                if (command != '1' and command != '2'):
                    print("Unknown command")

    arr.append(line)
    f = open('file.txt', 'w')
    for item in arr:
        f.write("%s\n" % item)
    f.close()


def show():
    print("////////////////////////////////////////////////////////////////")
    for i in arr:
        contact = Contact(i)
        contact.showContact()
    print("////////////////////////////////////////////////////////////////")


def find():
    print("Enter Please select your search criteria:")
    command = input("1 - name\n2 - surname\n3 - name and surname\n4 - date of birth\n")
    if command == '1':
        name = input("Enter name\n")
        name = name.strip()
        name = name.title()

        for i in arr:
            contact = Contact(i)
            if name == contact.name:
                contact.showContact()
    if command == '2':
        surname = input("Enter surname\n")
        surname = surname.strip()
        surname = surname.title()
        for i in arr:
            contact = Contact(i)
            if surname == contact.surname:
                contact.showContact()
    if command == '3':
        name = input("Enter name\n")
        name = name.strip()
        name = name.title()
        surname = input("Enter surname\n")
        surname = surname.strip()
        surname = surname.title()
        for i in arr:
            contact = Contact(i)
            if (name == contact.name and surname == contact.surname):
                contact.showContact()
    if command == '4':
        dateb = input("Enter date (dd/mm)\n")
        dateb = dateb.strip()
        if (len(dateb) != 5):
            print("Invalid date\n")
            return
        for num in range(2):
            if (not (dateb[num] >= '0' and dateb[num] <= '9')):
                print("Invalid date\n")
                return
        if (dateb[2] != '/'):
            print("Invalid input of date\n")
            return
        for num in range(3, 5):
            if (not (dateb[num] >= '0' and dateb[num] <= '9')):
                print("Invalid date\n")
                return

        for i in arr:
            contact = Contact(i)
            dbcontact = contact.dateOfBirth[:5]
            if (dateb == dbcontact):
                contact.showContact()
    if (command != '1' and command != '2' and command != '3' and command != '4'):
        print("Unknown command")
        return


def delete():
    name = input("Enter name\n")
    name = name.strip()
    name = name.title()
    surname = input("Enter surname\n")
    surname = surname.strip()
    surname = surname.title()
    for i in arr:
        contact = Contact(i)
        if (name == contact.name and surname == contact.surname):
            arr.remove(i)
            f = open('file.txt', 'w')
            for item in arr:
                f.write("%s\n" % item)
            f.close()
            return


def change():
    print("Please enter the contact information you want to change")
    delete()
    print("Please enter new data")
    line = input("Enter name and surname:\n")
    line = line.strip()
    line = line + " " + input("Enter phone number:\n")
    line = line.strip()
    line = line + " " + input("Enter date of birth:\n")
    line = line.strip()
    line = line.title()
    add(line)


def age():
    name = input("Enter name\n")
    name = name.strip()
    name = name.title()
    surname = input("Enter surname\n")
    surname = surname.strip()
    surname = surname.title()
    for i in arr:
        contact = Contact(i)
        if (name == contact.name and surname == contact.surname):
            from datetime import datetime, date
            dob = datetime.strptime(contact.dateOfBirth, '%d/%m/%Y')
            ageContact = date.today().year - dob.year
            print("Age", ageContact)
            return


def viewAge():
    print("Please select a search criteria by age")
    command = input("1 - younger than ...\n2 - so many years now\n3 - older than...\n")
    agefind = input("Enter the age at which we compare\n")
    sizeage = len(agefind)
    for num in range(sizeage):
        if(not(agefind[num]>='0'and agefind[num]<='9')):
            print("Invalid input\n")
            return
    agefind = int(agefind)
    if command == '1':
        for i in arr:
            contact = Contact(i)
            from datetime import datetime, date
            dob = datetime.strptime(contact.dateOfBirth, '%d/%m/%Y')
            ageContact = date.today().year - dob.year
            if (ageContact < agefind):
                contact.showContact()
    if command == '2':
        for i in arr:
            contact = Contact(i)
            from datetime import datetime, date
            dob = datetime.strptime(contact.dateOfBirth, '%d/%m/%Y')
            ageContact = date.today().year - dob.year
            if (ageContact == agefind):
                contact.showContact()
    if command == '3':
        for i in arr:
            contact = Contact(i)
            from datetime import datetime, date
            dob = datetime.strptime(contact.dateOfBirth, '%d/%m/%Y')
            ageContact = date.today().year - dob.year
            if (ageContact > agefind):
                contact.showContact()
    if (command != '1' and command != '2' and command != '3'):
        print("Invalid input")
        return


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
            add(line)
            fl = False
        elif command == '2':
            quit()
        elif command != '1' and command != '2':
            print("Unknown command")

# file is not empty
if os.stat("file.txt").st_size != 0:
    while (True):
        print("Please choose the number of the desired operation:")
        print("1 - Add new record to the phonebook\n2 - Introduce some change to the records\n3 - Delete a record")
        print(
            "4 - Search phonebook entries\n5 - Show all phonebook entries\n6 - Find out the age of a person\n7 - View contacts by age\n8 -Exit")
        command = input()
        if command == '1':
            line = input("Enter name and surname:\n")
            line = line.strip()
            line = line + " " + input("Enter phone number:\n")
            line = line.strip()
            line = line + " " + input("Enter date of birth:\n")
            line = line.strip()
            add(line)
        if command == '2':
            change()
        if command == '3':
            delete()
        if command == '4':
            find()
        if command == '5':
            show()
        if command == '6':
            age()
        if command == '7':
            viewAge()
        if command == '8':
            quit()

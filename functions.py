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


# phone book features
def add(line, arr):
    tmpline = line.split()
    sizetmpline = len(tmpline)
    if (sizetmpline != 4):
        return "Invalid input"
    line = line.title()  # first letter uppercase
    newContact = Contact(line)  # check for record existence
    date = newContact.dateOfBirth  # date validation
    try:
        valid_date = time.strptime(date, '%d/%m/%Y')
    except ValueError:
        return "Invalid date!"

    contName = len(newContact.name)  # name validation
    for i in range(contName):
        if (not ((newContact.name[i] >= 'A' and newContact.name[i] <= 'Z') or (
                newContact.name[i] >= 'a' and newContact.name[i] <= 'z') or (
                         newContact.name[i] <= '9' and newContact.name[i] >= '0'))):
            return "Invalid name"
    contName = len(newContact.surname)  # surname verification
    for i in range(contName):
        if (not ((newContact.surname[i] >= 'A' and newContact.surname[i] <= 'Z') or (
                newContact.surname[i] >= 'a' and newContact.surname[i] <= 'z') or (
                         newContact.surname[i] >= '0' and newContact.surname[i] <= '9'))):
            return "Invalid surname"
    if (len(newContact.phoneNumber) == 11):  # checking the correctness of the phone number

        for i in range(11):
            if (not (newContact.phoneNumber[i] <= '9' and newContact.phoneNumber[i] >= '0')):
                return "Invalid character in phone number"
    if (len(newContact.phoneNumber) == 12):

        if (newContact.phoneNumber[0] != '+'):
            return "Invalid phone number"
        if (newContact.phoneNumber[1] != '7'):
            return "Invalid phone number"
        for i in range(2, 12):
            if (not (newContact.phoneNumber[i] <= '9' and newContact.phoneNumber[i] >= '0')):
                return "Invalid phone number"
        # AutoCorrect +7 to 8
        newContact.phoneNumber = '8' + newContact.phoneNumber[2:]
        line = newContact.name + " " + newContact.surname + " " + newContact.phoneNumber + " " + newContact.dateOfBirth
        return line

    if (len(newContact.phoneNumber) != 11 and len(newContact.phoneNumber) != 12):
        return "Invalid phone number"

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


def show(arr):
    print("////////////////////////////////////////////////////////////////")
    for i in arr:
        contact = Contact(i)
        contact.showContact()
    print("////////////////////////////////////////////////////////////////")


def find(arr):
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


def delete(arr):
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


def change(arr):
    print("Please enter the contact information you want to change")
    delete(arr)
    print("Please enter new data")
    line = input("Enter name and surname:\n")
    line = line.strip()
    line = line + " " + input("Enter phone number:\n")
    line = line.strip()
    line = line + " " + input("Enter date of birth:\n")
    line = line.strip()
    line = line.title()
    add(line, arr)


def age(arr):
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


def viewAge(arr):
    print("Please select a search criteria by age")
    command = input("1 - younger than ...\n2 - so many years now\n3 - older than...\n")
    agefind = input("Enter the age at which we compare\n")
    sizeage = len(agefind)
    for num in range(sizeage):
        if (not (agefind[num] >= '0' and agefind[num] <= '9')):
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

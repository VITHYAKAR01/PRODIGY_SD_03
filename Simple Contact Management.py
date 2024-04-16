import os

class Contact:
    def __init__(self):
        self.ph = 0
        self.name = ""
        self.add = ""
        self.email = ""

    def create_contact(self):
        self.ph = int(input("Phone: "))
        self.name = input("Name: ")
        self.add = input("Address: ")
        self.email = input("Email address: ")

    def show_contact(self):
        print("\nPhone #:", self.ph)
        print("Name:", self.name)
        print("Address:", self.add)
        print("Email Address:", self.email)

def save_contact():
    with open("contactBook.txt", "a") as fp:
        contact.create_contact()
        fp.write(f"{contact.ph},{contact.name},{contact.add},{contact.email}\n")
    print("\nContact Has Been Successfully Created...")

def show_all_contacts():
    print("\n\t\t================================\n\t\t\tLIST OF CONTACTS\n\t\t\t================================\n")
    with open("contactBook.txt", "r") as fp:
        for line in fp:
            contact_info = line.strip().split(",")
            print("\nPhone #:", contact_info[0])
            print("Name:", contact_info[1])
            print("Address:", contact_info[2])
            print("Email Address:", contact_info[3])
            print("=================================================\n")

def display_contact(num):
    found = False
    with open("contactBook.txt", "r") as fp:
        for line in fp:
            contact_info = line.strip().split(",")
            if int(contact_info[0]) == num:
                print("\n\t\tContact Found\n")
                print("Phone #:", contact_info[0])
                print("Name:", contact_info[1])
                print("Address:", contact_info[2])
                print("Email Address:", contact_info[3])
                found = True
    if not found:
        print("\nNo record found...")

def edit_contact():
    num = int(input("Edit contact\n===============================\n\nEnter the number of contact to edit: "))
    updated_contact = Contact()
    with open("contactBook.txt", "r") as fp:
        lines = fp.readlines()
    with open("contactBook.txt", "w") as fp:
        for line in lines:
            contact_info = line.strip().split(",")
            if int(contact_info[0]) == num:
                updated_contact.create_contact()
                fp.write(f"{updated_contact.ph},{updated_contact.name},{updated_contact.add},{updated_contact.email}\n")
                print("\nContact Successfully Updated...")
            else:
                fp.write(line)

def delete_contact():
    num = int(input("Please Enter The contact #: "))
    with open("contactBook.txt", "r") as fp:
        lines = fp.readlines()
    with open("contactBook.txt", "w") as fp:
        for line in lines:
            contact_info = line.strip().split(",")
            if int(contact_info[0]) != num:
                fp.write(line)
    print("\nContact Deleted...")

if __name__ == "__main__":
    while True:
        print("\n\t ==== Contact Management System ====")
        print("\n\n\n\t\t\tMAIN MENU\n\t\t=====================")
        print("\t\t[1] Add Contact\n\t\t[2] Display all Contacts\n\t\t[3] Search contact\n\t\t[4] Update Contact\n\t\t[5] Delete Contact\n\t\t[0] Exit\n\t\t=================")
        ch = int(input("\t\tEnter the choice: "))

        if ch == 0:
            print("\n\n\t\tThank you for using CMS...")
            break
        elif ch == 1:
            contact = Contact()
            save_contact()
        elif ch == 2:
            show_all_contacts()
        elif ch == 3:
            num = int(input("\n\n\tPhone: "))
            display_contact(num)
        elif ch == 4:
            edit_contact()
        elif ch == 5:
            delete_contact()

        opt = int(input("\n\n\n..::Enter the Choice:\n\n\t[1] Main Menu\t\t[0] Exit\n"))
        if opt == 0:
            break
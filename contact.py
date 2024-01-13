import sys

def save_contact():
    filer.seek(0, 2)
    class addNum:
        def __init__(self, phone, name, email):
            self.phone = phone
            self.name = name
            self.email = email
    try:
        country = int(input("Country code: "))
        phone2 = int(input("Phone number (no parathensis or dashes please): "))
    except ValueError:
        print("Invalid input. Exiting...")
        return
    name = input("Enter contact name: ")
    email = input("Enter email: ")

    phone = "+" + str(country) + str(phone2)

    contactInfo = addNum(phone, name, email)
    filer.write("\n" + contactInfo.name + "," + contactInfo.phone + "," + contactInfo.email)
    print("Contact added")
    filer.close()

def view_list(filer):
    print("Format: Name, Phone # with country code, E-mail")
    for line in filer:
        entry = line.strip().split(',')
        print(", ".join(entry))
    filer.close()


def del_contact(filera):
    # for some ducking reason entering a blank name deletes everything
    query = input("Enter name of contact you want to delete: ")
    if (query == ""):
        confirm = input("Type DELETE in all caps to erase the entire contact list: ")
        if (confirm == "DELETE"):
            query = ""
        else:
            print("Either you didn't type DELETE or you forgor to enter your contact to delete.")
            return
    lines = filer.readlines()
    filer.seek(0)
    for line in lines:
        if query not in line:
            filer.write(line)
    filer.truncate()
    if (query == ""):
        print("Reset the list.")
    else:
        print("Contact deleted if it existed")
    filer.close()
    

def sort_and_exit(filer):
    lines = filer.readlines()
    lines.sort(key=lambda line: line.split(",")[0])
    filer.seek(0)
    for line in lines:
        filer.write(line + "\n")
    filer.truncate()
    filer.close()
    sys.exit()

while True:
    try:
        filer = open("contacts.csv", "r+")
    except FileNotFoundError:
        filer = open("contacts.csv", "x")
    print("What would you like to do?")
    print("(1) View contact list")
    print("(2) Add a contact")
    print("(3) Delete an entry in contact list")
    print("(4) Exit program")
    select = input()
    if select == "1":
        view_list(filer)
    elif select == "2":
        save_contact()
    elif select == "3":
        del_contact(filer)
    elif select == "4":
        sort_and_exit(filer)
    else:
        print("Invalid option")
        continue
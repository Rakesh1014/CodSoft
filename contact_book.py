contacts = []
def addcontact(name, mobile_num, email, address):
    contact = {
        "name": name,
        "mobile_num": mobile_num,
        "email": email,
        "address": address,
    }
    contacts.append(contact)
    print("Contact added successfully.")
def viewcontact():
    if not contacts:
        print("No contacts found...")
    else:
        for contact in contacts:
            print(f"Name: {contact['name']}, Phone: {contact['mobile_num']}")
def searchcontact(searchable_contact):
    found_contacts = [contact for contact in contacts if
                      searchable_contact.lower() in contact['name'].lower() or searchable_contact == contact[
                          'mobile_num']]
    if not found_contacts:
        print("No contacts found...")
    else:
        for contact in found_contacts:
            print(
                f"Name: {contact['name']}, Phone: {contact['mobile_num']}, Email: {contact['email']}, Address: {contact['address']}")
def updatecontact(name, new_mobile_num=None, new_mail=None, new_addr=None):
    updated = False
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            if new_mobile_num:
                contact['mobile_num'] = new_mobile_num
            if new_mail:
                contact['email'] = new_mail
            if new_addr:
                contact['address'] = new_addr
            updated = True
            print("Contact updated successfully...")
            break
    if not updated:
        print("Contact not found...")
def deletecontact(name):
    global contacts
    initlen = len(contacts)
    contacts = [contact for contact in contacts if contact['name'].lower() != name.lower()]
    if len(contacts) < initlen:
        print("Contact deleted successfully.")
    else:
        print("Contact not found.....")
def main():
    while True:
        print("\n------- CONTACT BOOK -------")
        print("1. ADD Contact")
        print("2. VIEW Contacts")
        print("3. SEARCH Contact")
        print("4. UPDATE Contact")
        print("5. DELETE Contact")
        print("6. Exit")
        choice = input("Enter your choice: ").strip()
        if choice == '1':
            name = input("Enter name: ").strip()
            mobile_num = input("Enter mobile number: ").strip()
            email = input("Enter email: ").strip()
            address = input("Enter address: ").strip()
            addcontact(name, mobile_num, email, address)
        elif choice == '2':
            viewcontact()
        elif choice == '3':
            searchable_contact = input("Enter name or mobile number to search: ").strip()
            searchcontact(searchable_contact)
        elif choice == '4':
            name = input("Enter name of the contact to update: ").strip()
            new_mobile_num = input("Enter new mobile number : ").strip()
            new_mail = input("Enter new email-ID : ").strip()
            new_addr = input("Enter new address: ").strip()
            updatecontact(name, new_mobile_num, new_mail, new_addr)
        elif choice == '5':
            name = input("Enter the contact name that you want to delete: ").strip()
            deletecontact(name)
        elif choice == '6':
            break
        else:
            print("Invalid Choice. Please try again....")
if __name__ == "__main__":
    main()
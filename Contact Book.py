#!/usr/bin/env python
# coding: utf-8

# In[ ]:


contacts = []

def add_contact():
    name = input("Enter Name: ")
    phone_number = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")
    contact = {"Name": name, "Phone Number": phone_number, "Email": email, "Address": address}
    contacts.append(contact)
    print("Contact Added Successfully!")

def view_contact_list():
    if not contacts:
        print("Contact list is empty.")
    else:
        for contact in contacts:
            print(f"{contact['Name']} - {contact['Phone Number']}")

def search_contact():
    search_query = input("Enter Name or Phone Number: ")
    search_results = [contact for contact in contacts if search_query.lower() in contact['Name'].lower() or search_query in contact['Phone Number']]
    
    if search_results:
        for result in search_results:
            print(f"{result['Name']} - {result['Phone Number']}")
    else:
        print("No matching contacts found.")

def delete_contact():
    search_query = input("Enter Name or Phone Number to Delete: ")
    contact_to_delete = next((contact for contact in contacts if search_query.lower() in contact['Name'].lower() or search_query in contact['Phone Number']), None)

    if contact_to_delete:
        contacts.remove(contact_to_delete)
        print("Contact Deleted Successfully!")
    else:
        print("Contact not found!")

def main():
    while True:
        print("--------------------------")
        print("  CONTACT MANAGEMENT APP")
        print("--------------------------")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")
        print("--------------------------")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contact_list()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()


# In[ ]:





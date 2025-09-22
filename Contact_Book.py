
contact_list={}



def add_contact(name,no):
    if name in contact_list:
        print("contact is already saved")
        return
    
    contact_list.update({name:no})
    print("Contact is Saved successfully")


def delete_contact(name):
    if name not in contact_list:
        print("No contact found")
        return

    option=int(input("""Do you want to delete the contact?
                    1 : Yes    2 : No
                 Enter you choice :"""))
    if option==1:
        del contact_list[name]
        print("contact is deleted Successfully")
    else:
        print("Delete cancelled")


def search_contact(name):

    if name not in contact_list:
        print("No contact found")
        return
    
    print(f"{name}:{contact_list.get(name)}")

def display_contacts():
    if not contact_list:
        print("No contacts to display")
        return
    print("--- contact list ---")
    for name, number in contact_list():
        print(f"{name} : {number}")




while True:
    print("1 : Add contact")
    print("2 : delete constact")
    print("3 : serach contact")
    print("4 : Display all the contacts")
    print("5 : To end the program")

    choice=int(input("Enter your choice :"))

    if choice==1:
        name=input("Enter name: ")
        no=int(input("enter number: "))
        add_contact(name,no)
    elif choice==2:
        name=input("enter name to delete: ")
        delete_contact(name)
    elif choice==3:
        name=input("enter name to search:")
        search_contact(name)
    elif choice==4:
        display_contacts()
    elif choice==5:
        print("program over")
        break
    else:
        print("Invalid choice.. Try again !!!")
        
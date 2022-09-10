
class AddressBook:
    def __init__(self,name,phone_num,email):  
        self.name = name
        self.phone_num = phone_num
        self.email = email
        
    def print_list(self): 
        print("Name : ",self.name)
        print("Phone Number : ",self.phone_num)
        print("Email Address : ",self.email)


def add_contact():
    name= input("Name?  ")
    phone_num= input("Phone Number?  ")
    email= input("Email Address?  ")
    
    print("=== Contact Info Registered! ===")
    
    contact = AddressBook(name,phone_num,email)
    return contact


def delete_contact(contact_list, name):
    for i, contact in enumerate(contact_list):
        if contact.name == name :
            del contact_list[i]    
            
            print("=== Successfully Deleted! ===")

def print_contact(contact_list):
    print("====================<Contacts>=====================\n")
    for contact in contact_list:
        contact.print_list()
        print("======================================================")
        


def load(contact_list):
    r = open("contact_db.txt", "rt")
    lines = r.readlines()
    num = len(lines) / 4
    num = int(num)

    for i in range(num):
        name = lines[4*i].rstrip('\n')
        phone = lines[4*i+1].rstrip('\n')
        email = lines[4*i+2].rstrip('\n')
        
        contact = AddressBook(name, phone, email)
        contact_list.append(contact)
    r.close()


def save_contact(contact_list):
    w = open("./contact_db.txt","wt")
    for contact in contact_list:
        w.write(contact.name + '\n')
        w.write(contact.phone_num +'\n')
        w.write(contact.email +'\n')
    w.close


# In[7]:


def show_menu():
    print("1. Add new contact")
    print("2. View all contacts")
    print("3. Delete contact")
    print("4. End")
    
    menu = input("Choose Action: ")
    return int(menu)


def run():
    contact_list = []
        #load(contact_list)
        
    while 1:
        menu = show_menu()
        if menu == 1:
            contact = add_contact()
            contact_list.append(contact)
        elif menu == 2: 
            print_contact(contact_list)
        elif menu == 3:
            name = input("Name to be deleted : ")
            delete_contact(contact_list,name)
        elif menu == 4:
            save_contact(contact_list)
            break



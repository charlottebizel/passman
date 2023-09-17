"""notice and error fonction outside of their fonctions to edit with color
ect for later"""

def notice(text: str):
    print(f"notice: {text}")

def error (text: str):
    print(f"error: {text}")

"""first ask input of the user
    test if the user is in data base
    if yes error 
    else create user
    """

def create_user():

    user_login = input("enter your new user name: ")

    if user_login in users:
        error("this user name already exists")

    else: 
        users[user_login] = []
        notice("user created.")

"""ask for the user input on what to delete
    if the login is in the DB users ask confirmation 
    and delete if yes
    else error notice"""

def remove_user():
    user_login = input("enter a user to delete: ")

    if user_login in users.keys():
        rep=input("are you sure Y/N?")
        if rep.upper() == "Y":
            del users[user_login]
            notice("user successfully removed.")
    else:
        error("user not found ! ")

"""input to choose in the options inside the vault
    ask for choice and direct to the chosen opt """

def ask_for_number2() -> int:
    choice :str = input("your choice: ")
    if choice.isdigit():
        return int(choice)
    else:
        error("not a number")
        return -1
    
"""ask for the user login if the login exist in users open the user asked
and show a welcom message and the table of choice witch a return to the first table for 
zero else message error"""

def login():

    login = input("enter your user name : ")

    if login in users.keys():
        global active_vault
        active_vault = users[login]
        choice : int

    print("welcome to your vault ".center(100,"-"))

    choice : int
    while choice := -1 != 0 :

        print("""
        \r1. create item
        \r2. remove item
        \r3. list items
        \r4. show items
        \r5. search by name
        \r0 exit.      
        """)

        choice = ask_for_number2() #int(input("your choice:"))

        match choice:
            case 0:
                main()
            case 1:
                create_item()
            case 2:
                remove_item()
            case 3:
                list_items()
            case 4 : 
                show_items()
            case 5 : 
                search_by_name()
            case 6 :
                edit_items()
            case _: #le _: signifie TOUT les cas sauf ceux au dessu
                error("warning")   

    else:
        error("this user name does not exist")

"""ask what item theh client wants to add
if the item is already in the vault ->error else save new item
"""

def create_item():
    new_item = input("what you want to add:")
    
    if new_item in active_vault:
            error("item already in vault")
    
    else:
                active_vault.append(new_item)
                notice("item added successfully")
    """ask wich item to delete test if existe if existe delete 
    if not --> error"""

def remove_item():
    item = input("tell me what you want to delete: ")
    if item in active_vault:
            active_vault.remove(item)
            notice("item deleted successfully")
    else:
            error("this item does not exist")

"""fonction to list all the items in the vault"""

def list_items():
    for item in active_vault: 
        print(item)

"""show an specific item 
ask for the item , test if exist in vault 
if exisst ->shaw
if not -> error"""

def show_items():
    what = input("tell me what do you want to see: ")
    if what in active_vault:
        print(what)
    else:
        error("this item does not exist")

"""let us surch an item with his first letter 
test if existe in vault print item """

def search_by_name():
    query = input("what are you looking for?:")
    for item in active_vault:
        
        if item.startswith(query):
            print(item)

"""change an item by delete and add a new item
test if item to change existe in vault if yes change 
if not ->error """

def edit_items():
    query2 = ("wich item do you want to change?: ")
    query3 = ("by what?: ")
    if query2 in active_vault:
            active_vault.remove(query2)
            active_vault.append(query3)
            print("your new item is: ")
            print(query3)
    else:
        error("the item you want to change does not exist in the vault")

"""confirm if you want to exit yes -> close """   

def exit():
        rep=input("are you sure  you want to exit Y/N?")
        if rep.upper() == "Y":
            notice("good bye.")
            print(quit())

"""
    ask if the choice is a number and answer the choice if ok or -1
    """
           
def ask_for_number() -> int:
    choice :str = input("your choice: ")
    if choice.isdigit():
        return int(choice)
    else:
        error(" not a number")
        return -1

"""first table to show in the app and the cases you can choose"""

def main():
    choice : int

    print("welcome to passman !!".center(100,"-"))

    choice : int
    while choice := -1 != 0 :

        print("""
        \r1. create User
        \r2. remove user
        \r3. login

        \r0 exit.      
        """)

        choice = ask_for_number() #int(input("your choice:"))

        match choice:
            case 0:
                exit()
            case 1:
                create_user()
            case 2:
                remove_user()
            case 3:
                login()
            case _: #le _: signifie TOUT les cas sauf ceux au dessu
                error("warning")

# entry point
if __name__ == "__main__":
    #some variables
    users: dict[str,list[str]] = {} #key :str, value:list of tuples
    active_vault:list[str] = []
    # variable pour l'apelle du vault dans login qui utile dans d'autre fonct
    main()

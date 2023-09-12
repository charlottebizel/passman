def notice(text: str):
    print(f"notice: {text}")

def error (text: str):
    print(f"error: {text}")

def create_user():

    user_login = input("enter your new user name: ")

    if user_login in users.keys():
        error("this user name is already exists")

    else: 
        users[user_login] = []
        notice("user created.")


def remove_user():
    user_login = input("enter a user to delete: ")

    if user_login in users.keys():
        rep=input("are you sure Y/N?")
        if rep.upper() == "Y":
            del users[user_login]
            notice("user successfully removed.")
        else:
            error(" user not found ! ")

def ask_for_number2() -> int:
    choice :str = input("your choice: ")
    if choice.isdigit():
        return int(choice)
    else:
        error(" not a number")
        return -1

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
                exit()
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



def create_item():
    new_item = input("tell me the adress of the site you want to add:")
    
    if new_item in active_vault:
            print("item already in vault")
    
    else:
                active_vault.append(new_item)
                print("item added successfully")
    

def remove_item():
    item = input("tell me what site you want to delete:")
    if item in active_vault:
            active_vault.remove(item)
            print("item deleted successfully")
    else:
            print("this item does not exist")

def list_items():
    for item in active_vault:
        item_name,_,_ = item 
        print(item_name)


def show_items():
    what = input("tell me what do you want to see: ")
    if what in active_vault:
        print(what)
    else:
        print("this item does not exist")

    


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

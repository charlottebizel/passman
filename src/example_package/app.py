def create_user():

    user_login = input("enter your new user name: ")

    if user_login in users.keys():
        print("this user name is already exists")

    else: 
        users[user_login] = []
        print("notice: user created.")



def remove_user():
    user_login = input("enter a user to delete: ")

    if user_login in users.keys():
        rep=input("are you sure Y/N?")
        if rep.upper() == "Y":
            del users[user_login]


def login():
    pass


def create_item():
    pass


def remove_item():
    pass


def list_items():
    pass


def show_items():
    pass


def search_by_name():
    pass
    """
    ask if the choice is a number and answer the choice if ok or -1
    """

def ask_for_number() -> int:
    choice :str = input("your choice: ")
    if choice.isdigit():
        return int(choice)
    else:
        print("error: not a number")
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
                print("warning")

# entry point
if __name__ == "__main__":
    #some variables
    users: dict[str,list[tuple[str,str,str]]] = {} #key :str, value:list of tuples

    main()

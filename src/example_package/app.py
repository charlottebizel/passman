def create_user():
    pass


def remove_user():
    pass


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

def main():
    print("welcome to passman !!".center(100,"-"))

    while choice := -1 != 0 :

        print("""
        \r1. create User
        \r2. remove user
        \r3. login

        \r0 exit.      
        """)

        choice = int(input("your choice:"))

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
                print("erreur")





# entry point
if __name__ == "__main__":
    #some variables
    users: dict[str,list[tuple[str,str,str]]] = {} #key :str, value:list of tuples

    main()
from pathlib import Path

from colorama import Fore, Style, init
from data import Item, User, Vault


class App:
    vault: Vault #lazy

    def __init__(self):

        self.users: dict[User,Vault] = {} #varible de stockage/déclariation = initialisation
        self.path: Path = Path("data.dat")
        self.items: list[Item] = []


    def create_user(self):
        user_name = input("enter your login: ")
        user_password = input("enter your password: ")

        user = User(user_name,user_password)

        if user in self.users:
            self.error("user already exists")
        else:
            self.users[user] = Vault()
            self.notice("User created")

    def get_user(self,login:str) -> User|None:
        for user in self.users:
            if login == user.login:
                return user
            else:
                return None
            
    def remove_user(self):
        user_login = input("enter the user to delete: ")
        user_password = input("enter your password")

        user = self.get_user(user_login)
        if user and user.check_password(user_password):
                del self.users[user]
                self.notice("user successfully removed.")
        else:
            self.error("user not found ! ")


    def change_password(self):
        pass

    def password_is_valid(self):
        pass
    
    def login(self,login:str,login_password:str):
        
        user = User(login,login_password)

        self.vault = self.users[user]
        
        login = input("enter your user name : ")
        login_password = input("enter your password: ")

 
        if user in self.users and user.check_password(login_password):
            self.vault_menu
        else:
            self.warning("login or password invalid")



    def logout(self):
        self.notice("you are loging out of passman")
        #logout


    def vault_menu(self,user:User):
        self.vault = self.users[user]

        init(autoreset=True) #initialisation de colorama obligatoire
        print(Style.BRIGHT + "bienvenue dans votre vault".center(80," "))
        
        while choice :=-1 !=0: #preset a -1 pour etre different de 0
            print ("""
            \r1. List items
            \r2. show item
            \r3. ad item
            \r4. update item
            \r5. remove
                   
            \r0. Quit
            """)

        choice = self.ask_number()

        match choice: 
            case 1:
                self.list_items()
            case 2:
                self.show_item()  
            case 3:
                self.create_item()
            case 4:
                self.update_item()
            case 5:
                self.delete_item()
            case 0:
                return
            case _:
                self.warning("invalid choice")

    def create_item(self):

        new_name = input("what name do you want to add?:")
        new_website = input("what website do you want to add?:")
        new_login = input("login you want to add?: ")
        new_password = input("what password you want to add? :")

        item = Item(new_name,new_website,new_login,new_password)
    
        if self.vault.add_item(item) is True:
            self.notice("item added successfully")
        else:
            self.error


    def list_items(self,name:str,website:str,login:str,password:str):
            items =(name,website,login,password)
            print(items) 

    
    def get_item(self,name:str) -> Item|None:

        for item in self.items:
            if name == item.name:
                return item
            else:
                return None     
              
    def delete_item(self):

        name = input("enter the item to delete: ")

        item = self.get_item(name)
        if item :
                
                self.notice("item successfully removed.")
        else:
            self.error("item not found ! ")


    def update_item(self):
        #demander quoi update
        #demander avec quoi update
        #montré l'update
        pass


    def show_item(self):

        for item in self.vault.list_items():
            print(item)
    

    def search(self,query:str) -> list[Item]:
        #demander quoi chercher?
        #chercher

        pass


    def main(self):
        init(autoreset=True) #initialisation de colorama obligatoire
        print(Style.BRIGHT + "passman".center(80," "))
        
        while choice :=-1 !=0: #preset a -1 pour etre different de 0
            print ("""
            \r1. Create user
            \r2. Login
            \r3. Change Password
            \r4. Logout
                   
            \r0. Quit
            """)

        choice = self.ask_number()

        match choice: 
            case 1:
                self.create_user()
            case 2:
                self.login()
            case 3:
                self.change_password()
            case 4:
                self.logout()
            case 0:
                exit()
            case _:
                self.warning("invalid choice")

    
    @staticmethod
    def ask_number() ->int:
        # TODO refactor later

        choice :str = input("Enter your choice: ")
        if choice.isdigit():
            return int(choice)
        else:
            return -1
            #pas besoin de mettre error notice car deja dans le menu case _warning pour 
            # une reponse autre que les case



    @staticmethod    
    def warning(message:str):
         print(Fore.YELLOW + Style.BRIGHT +f"warning:{message}")



    @staticmethod
    def error(message:str):
        print(Fore.RED + Style.BRIGHT +f"error:{message}")



    @staticmethod
    def notice(message:str):
        print(Fore.BLUE + Style.BRIGHT +f"warning:{message}")



    def load(self) -> dict[User,Vault]:
        #import os
        import pickle

        # TODO REFACTOR LATER 
        from pathlib import Path
           
        if self.path.exists():
            with self.path.open("rb") as file:
                return pickle.load(file)
    
        else:
            return {}


    def save(self):
        import pickle
        pickle.dump(self.users,self.path)
   

if __name__=='__main__': #code lancement python
    pass

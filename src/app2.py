import os
import pickle

from colorama import Fore, Style, init
from data import User, Vault


class App:
    active_user:User #typing

    def __init__(self):
        init(autoreset=True) #colorama
        self.users:dict[User,Vault] = self.load()
        self.active_user :User
        

    def load(self) -> dict[User,Vault]:
        if os.path.exists("data.dat"):
            with open("data.dat","rb",encoding = "utf8") as file:
                return pickle.load(file)
        else:
            return {}

    def save(self,users:str):
        with open("data.dat","wb",encoding="utf8") as file:
          pickle.dump(users,file)

    def exit (self):
        pass

    def main(self):
        print(Style.BRIGHT +"welcome to passman !!".center(100,"-"))

    
        while choice := -1 != 0 :
            print("""
            \r1. create User
            \r2. remove user
            \r3. login

            \r0 exit.      
            """)

            choice = ask_for_number() 

        match choice:
            case 0:
                save()
                exit()
            case 1:
                create_user()
            case 2:
                remove_user()
            case 3:
                login()
            case _: 
                error("warning")

    
    @staticmethod
    def error(text: str):
        print(Fore.LIGHTRED_EX + f"error: {text}")

    @staticmethod
    def notice(text:str):
        print(Fore.LIGHTBLUE_EX + f"notice: {text}")

    @staticmethod
    def warning (text:str):
        print(Fore.RED + f"warning: {text}")

    def ask_for_number(self)-> int:
        #ask choice
        #test if choice is digit
        #else error
        pass

    def create_user(self):

        user_login = input("Enter your login:")
        user_psw = input("Enter your psw:")
        user = User(login=user_login,password=user_psw)

        if user in self.users:
            self.users[user] = Vault()
            self.notice("user created")
        else:
            self.warning("user already existe")

    def login(self):

        user_login = input("Enter your login:")
        user_psw = input("Enter your psw:")
        password = Password(login=user_login,password=user_psw)

        if user_login in self.users and user_psw == password:
            global active_users
            active_users = self.users[user_login]
            main()
        else:
            self.warning("user does not existe")  
    

    def remove_user(self):

        user_login = input("Enter the login you want to delete:")
        if user_login in self.users:
            user_psw = input("Enter your password to delete this user:")
            if user_psw == password #??
                del user_login
            else:
                self.warning("incorect password")
        else:
            self.warning("the user you want to delete does not exist")

        #if ok del user ?? and vault ??
        pass

    def vault_menu(self):

        print(Style.BRIGHT + f"{self.active_user.login}'s vault ".center(100,"-"))

        while choice := -1 != 0 :
            print("""
            \r1. create item
            \r2. remove item
            \r3. list items
            \r4. show items detail
            \r5. search by name 
            \r0 exit.      
            """)

            choice = ask_for_number() 

        match choice:
            case 0:
                return
            case 1:
                item_name = input("Enter your name:")
                item_psw = input("Enter your password:")
                item_website = input("Enter the website you want to save :")
                user_login = input("Enter your login:")
                #check if name existe
                #creat item??
                #->def ##refactor??
                self.users[self.active_user].create_item()

            case 2:
                self.users[self.active_user].remove_item()
            case 3:
                self.users[self.active_user].show_item()
            case 4 : 
                self.users[self.active_user].show_detail()
            case 5 : 
                self.users[self.active_user].search_by_name()
            case 6 :
                self.users[self.active_user].edit_items()
            case _: 
                pass


if __name__ == "__main__":
    app = App()
    app.main()
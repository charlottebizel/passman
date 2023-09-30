class User:
    def __init__(self,login:str ,password:str): #constructor
        self.login:str = login #property
        self.password: str = password 
        self.vault: Vault = Vault()

    def _check_password(self,password:str) -> bool:
        return self.password == password

    def modify_password(self,old_psw:str,new_psw:str):
        if self._check_password(old_psw):
            self.password = new_psw

    def __str__(self) ->str:
        return self.login + "" + self.password

    def __hash__(self)-> int:
        "unicity test"
        return hash(self.login)

class Vault:
    def __init__(self):
        self.items: dict[str,Item] = {}

    def create_item(self,name:str,password:str,website:str,login:str)->bool:

        """create any item
        params:
        name:unic name of item
        password:non encrypted password returns
        website:website
        login:login
            true is sucess
        """
        item = Item(name,password,website,login) #creation de l'objet
        if name not in self.items:
            self.items[name] = item #creation de l'item item a la clef name en faisant un dict
            return True
        else:
            return False

    def show_item(self):
        "show items"
        for item in self.items.values():
            print(item)
        
    def show_detail(self,key:str):
        "show a specific collumn in the items"
        if key in self.items:
            print(self.items[key])
        else:
            pass #TODO

    def remove_item(self,name:str,password:str,website:str,login:str)->bool:
        "test if item exist and delete"
        item = Item(name,password,website,login)
        if item in self.items:
            del (self.items[name])
            return True
        else:
            return False

    def update_item(self,name:str,password:str,website:str,login:str):
        item = Item(name,password,website,login)
        "test if item existe and modifies the item "

        if name in self.items:
            self.items.update(self.items)
            return True
        else:
            return False

    def search_by_name(self,query:str):
        for item in self.items:
            if query == (item):
                print(item)
    
    def edit_items(self,query2:str,query3:str,name:str,password:str,website:str,login:str):
        item = Item(name,password,website,login)
        #query2?
        #query3?
        if query2 in self.items:
            del(self.items[query2])
            self.items[query3] = item
            print("your new item is: ")
            print(query3)
        else:
            
class Item:  

    def __init__(self,login:str,password:str,name:str,website:str):
            self.login:str = login
            self.password:str = password
            self.name:str = name
            self.website:str = website

    def __hash__(self)-> int:
        return hash(self.name)
    
    def __str__(self) -> str:
        return f"Name: {self.name} \nWebsite: {self.website} \nLogin: {self.login} \nPassword: {self.password}"

        

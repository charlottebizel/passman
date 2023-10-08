from dataclasses import dataclass


class User:
    def __init__(self,login:str,password:str):
        self.login = login
        self.password = password

    
    def check_password(self,pass_to_check :str) -> bool:
        return pass_to_check == self.password
    
    def __eq__(self,other:object):
        if isinstance(other,User): #verifie que deux objet sont les même 
            return self.login == other.login

    def __ash__(self): #donne l'unicité
        return hash(self.login)

    def __repr__(self):#affiche si besoin de list ou show
        return f"User: login: {self.login},pass:{self.password}"

@dataclass
class Item:
    name: str
    website: str
    login: str
    password: str

class Vault:
    def __init__(self):  
        self.items: list[Item] = []
    
    def add_item(self,item:Item) -> bool:

        if item in self.items:
            return False
        else:
            self.items.append(item)
            return True
    
    def list_items(self) ->list[Item]:
        return self.items
    
    def get_item(self,name:str) -> Item|None:

        for item in self.items:
            if name == item.name:
                return item
            else:
                return None
            
    def del_item(self,item:Item) -> bool:
        
        if  item == self.get_item :
                self.items.remove(item)
                return True
        else:
            return False
        
    def serach(self,query:str) -> list[Item]:
        return [item for item in self.items if query in item.name or query in item.website]  #generateur de list
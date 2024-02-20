class Recipe:
    def __init__(self, id,title, img, prep, cook):
        self.id = id
        self.title = title
        self.img = img
        self.prep = prep
        self.cook = cook

class User:
    def __init__(self, id, username, password, profilepic):
        self.id = id
        self.username = username
        self.password = password

class Review:
    def __init__(self, id, header,recipeid, description, rating) -> None:
        self.id = id
        self.header = header
        self.recipeid = recipeid
        self.description = description
        self.rating = rating

class GroceryList:
    def __init__(self,id, itemname, quantity, recipeid) -> None:
            self.id = id
            self.itemname = itemname
            self.quantity = quantity
            self.recipeid = recipeid
            


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

        

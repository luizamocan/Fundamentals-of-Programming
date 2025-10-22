class Driver:
    def __init__(self, name,x,y):
        self.name = name
        self.x = x
        self.y = y

    def __str__(self):
        return f"Name: {self.name}, X: {self.x}, Y: {self.y}"


class Address:
    def __init__(self, id, name, x, y):
        self.id = id
        self.name = name
        self.x = x
        self.y = y

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, X: {self.x}, Y: {self.y}"




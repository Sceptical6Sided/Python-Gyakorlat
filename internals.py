class Car:
    def __init__(self, maker, model, color, maxspeed, numofseats,):
        self.maker = maker
        self.model = model
        self.color = color
        self.maxspeed = maxspeed
        self.numofseats = numofseats

    def __str__(self):
        return f"{self.maker} {self.model}"

    def getcardata(self):
        return f"This car is a(n) {self.model} made by {self.maker}, in the color of {self.color}" \
               f". It has a max speed of {self.maxspeed} with {self.numofseats} amount of seats."

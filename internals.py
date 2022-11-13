class Car:
    def __init__(self, maker, model, color, max_speed, num_of_seats, ):
        self.maker = maker
        self.model = model
        self.color = color
        self.max_speed = max_speed
        self.num_of_seats = num_of_seats

    def __str__(self):
        return f"{self.maker} {self.model}"

    def getcardata(self):
        return f"This car is a(n) {self.model} made by {self.maker}, in the color of {self.color}" \
               f". It has a max speed of {self.max_speed} with {self.num_of_seats} amount of seats."

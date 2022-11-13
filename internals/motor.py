class Motor:
    def __int__(self, type, horsepower):
        self.type = type
        self.horsepower = horsepower


    def __str__(self):
        return f"This motor is a {self.type} motor with {self.horsepower} horsepower"


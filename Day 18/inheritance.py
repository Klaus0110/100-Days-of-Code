class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers,"

    def show_speed(self):
        return f"And the top speed is {self.max_speed}kmph with a mileage of {self.mileage}kmpl."

class Mustang(Vehicle):
    def seating_capacity(self, capacity=2):
        return super().seating_capacity(capacity=2)

class Sclass(Vehicle):
    def seating_capacity(self, capacity=4):
        return super().seating_capacity(capacity=4)

car1 = Mustang("Ford Mustang", 250, 4)
car2 = Sclass("Mercedes S-class", 200, 12)
print(car1.seating_capacity())
print(car1.show_speed())
print(car2.seating_capacity())
print(car2.show_speed())
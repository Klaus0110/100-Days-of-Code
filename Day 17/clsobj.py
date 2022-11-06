class dodge:
    type = "Muscle Car"

    def __init__(self, name):
        self.name = name

challenger = dodge("Challenger")
charger = dodge("Charger")

print("Challernger is a {}".format(challenger.__class__.type))
print("Charger is also a {}".format(charger.__class__.type))

print("{}'s manufacturer is Dodge".format(challenger.name))
print("{}'s manufacturer is Dodge".format(charger.name))
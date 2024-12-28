class SpecialPlace:
    def __init__(self, name, action):
        self.name = name
        self.action = action

    def trigger_action(self, player):
        if self.action:
            self.action(player)

    def __str__(self):
        return f"SpecialPlace {self.name}"

    def __repr__(self):
        return self.__str__()

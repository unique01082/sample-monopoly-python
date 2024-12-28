class Property:
    def __init__(self, name, cost, rent, upgrade_cost_ratio=0.5, upgrade_rent_ratio=1.5):
        self.name = name
        self.cost = cost
        self.rent = rent
        self.owner = None
        self.upgrade_cost_ratio = upgrade_cost_ratio
        self.upgrade_rent_ratio = upgrade_rent_ratio
    
    def calculate_upgrade_cost(self):
        return self.cost * self.upgrade_cost_ratio

    def calculate_upgrade_rent(self):
        return self.rent * self.upgrade_rent_ratio
    
    def calculate_sell_price(self):
        return self.cost * 0.5 + self.rent * 2

    def purchase(self, player):
        if player.cash >= self.cost and self.owner is None:
            player.cash -= self.cost
            player.assets += self.cost
            self.owner = player
            return True
        return False

    def pay_rent(self, player):
        if self.owner and self.owner != player and player.cash >= self.rent:
            player.cash -= self.rent
            self.owner.cash += self.rent
            return True
        return False
    
    def upgrade(self, player):
        if self.owner == player and player.cash >= self.calculate_upgrade_cost():
            player.cash -= self.calculate_upgrade_cost()
            self.rent = self.calculate_upgrade_rent()
            return True
        return False
    
    def sell(self):
        previous_owner = self.owner
        self.owner = None
        previous_owner.cash += self.calculate_sell_price()

    def __str__(self):
        return f"Property {self.name}: Cost = {self.cost}, Rent = {self.rent}, Owner = {self.owner.name if self.owner else None}"

    def __repr__(self):
        return self.__str__()

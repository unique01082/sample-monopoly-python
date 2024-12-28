class GamePlayer:
    bankruptcy = False

    def __init__(self, name, assets, cash, current_position):
        self.name = name
        self.assets = assets
        self.cash = cash
        self.current_position = current_position
        
    def __str__(self):
        return f"Player {self.name}: Cash = {self.cash}, Assets = {self.assets}, Current Position = {self.current_position}"
    
    def __repr__(self):
        return self.__str__()

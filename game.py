import random
from game_player import GamePlayer
from property import Property
from special_place import SpecialPlace

class Game:
    players = []
    current_player = None
    
    def __init__(self, initial_cash, map):
        self.initial_cash = initial_cash
        self.map = map
    
    def add_player(self, name):
        self.players.append(GamePlayer(name, 0, self.initial_cash, self.map.get_property(0)))
        
    def random_player_order(self):
        random.shuffle(self.players)

    def start(self):
        self.current_player = self.players[0]
        
    def move_player(self, player, steps):
        print(f"{player.name} moved {steps} steps.")
        
        current_position_index = self.map.get_index(player.current_position)
        new_position_index = (current_position_index + steps) % self.map.get_size()
        player.current_position = self.map.get_property(new_position_index)
        
        if isinstance(player.current_position, Property):
            print(f"{player.name} landed on Property {player.current_position.name}")
            if player.current_position.owner is None:
                # Implement logic to purchase
                print(f"Property {player.current_position.name} is available for purchase.")
                print(f"Price: {player.current_position.cost}, Rent: {player.current_position.rent}, Player Cash: {player.cash}")
                
                choice = input("Do you want to buy this property? (y/n): ").strip().lower()
                if choice == 'y':
                    result = player.current_position.purchase(player)
                    if result:
                        print(f"{player.name} purchased {player.current_position.name}")
                    else:
                        print(f"{player.name} does not have enough cash to purchase {player.current_position.name}")
                else:
                    print(f"{player.name} decided not to purchase {player.current_position.name}")
            else:
                # Implement logic to pay rent
                if player.current_position.owner != player:
                    print(f"{player.name} has to pay rent to {player.current_position.owner.name}")
                    # pay rent
                    result = player.current_position.pay_rent(player)
                    if result:
                        print(f"{player.name} paid rent ({player.current_position.rent}) to {player.current_position.owner.name}. Cash: {player.cash}")
                    else:
                        print(f"{player.name}({player.cash}) does not have enough cash to pay rent ({player.current_position.rent}) to {player.current_position.owner.name}")
                        # sell properties or bankrupt
                        # get player properties
                        player_properties = self.map.get_properties_by_owner(player)
                        total_sell_price = sum([property.calculate_sell_price() for property in player_properties])
                        # check if ...
                        if len(player_properties) == 0 or total_sell_price < player.current_position.rent:
                            print(f"{player.name} does not have any property to sell or total sell price ({len(player_properties)} properties, total {total_sell_price}) is less than rent")
                            player.bankruptcy = True
                            # sell all player properties
                            for property in player_properties:
                                property.sell()
                            # transfer all cash to owner
                            print(f"{player.name} went bankrupt. All cash ({player.cash}) transferred to {player.current_position.owner.name}")
                            player.current_position.owner.cash += player.cash
                            player.cash = 0
                        else:
                            # print player properties
                            for i, property in enumerate(player_properties):
                                print(f"{i + 1}: {property.name} (Sell Price: {property.calculate_sell_price()})")
                            # let player choose properties to sell
                            while True:
                                choose_properties = [int(x) for x in input(f"Choose properties to sell (separated by comma): ").strip().split(",")]
                                choose_properties_sell_price = sum([property.calculate_sell_price() for i, property in enumerate(player_properties) if i + 1 in choose_properties])
                                if choose_properties_sell_price < player.current_position.rent:
                                    print(f"Total sell price is less than rent. Please choose again.")
                                    continue
                                
                                for index in choose_properties:
                                    index = int(index)
                                    property = player_properties[index - 1]
                                    property.sell()

                                # pay rent
                                player.current_position.pay_rent(player)
                                break
                else:
                    print(f"{player.name} owns {player.current_position.name}")
                    # upgrade property
                    choice = input(f""" Do you want to upgrade this property? (y/n): 
 Cost: {player.current_position.cost}, Rent: {player.current_position.rent}, Player Cash: {player.cash}
 Upgrade Cost: {player.current_position.calculate_upgrade_cost()}, New Rent: {player.current_position.calculate_upgrade_rent()}
""").strip().lower()
                    if choice == 'y':
                        result = player.current_position.upgrade(player)
                        if result:
                            print(f"{player.name} upgraded {player.current_position.name}")
                            print(f"New Rent: {player.current_position.rent}")
                        else:
                            print(f"{player.name} does not have enough cash to upgrade {player.current_position.name}")
                    else:
                        print(f"{player.name} decided not to upgrade {player.current_position.name}")
                pass
                
        elif isinstance(player.current_position, SpecialPlace):
            print(f"{player.name} landed on Special Place {player.current_position.name}")
            player.current_position.trigger_action(player)
        
    def next_turn(self):
        self.players.append(self.players.pop(0))
        self.current_player = self.players[0]
        
    def get_active_players(self):
        return [player for player in self.players if not player.bankruptcy]
        
    def is_finished(self):
        return len(self.get_active_players()) <= 1
    
    def get_winner(self):
        return self.get_active_players()[0]

    def __str__(self):
        player_info = "\n".join([f"Player {player.name}: Cash = {player.cash}, Assets = {player.assets}" for player in self.players])
        return f"Game with {len(self.players)} players:\n{player_info}\n{self.map}"

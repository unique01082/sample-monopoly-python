
import random
from map import Map
from game import Game

print(type(Map.vietnam_theme_map))

# prepare the game
game = Game(initial_cash=20000, map=Map.vietnam_theme_map)
game.add_player("Alice")
game.add_player("Bob")
game.add_player("Charlie")
game.add_player("David")

game.random_player_order()

#start the game
game.start()

while not game.is_finished():
    # start the turn
    if game.current_player.bankruptcy:
        print(f"{game.current_player.name} is bankrupt. Skip turn.")
        game.next_turn()
        continue
    
    print(f"Player {game.current_player.name} turn")
    input("Enter to roll the dice")
    dice = random.randint(1, 6)
    print(f"Player {game.current_player.name} rolled {dice}")
    
    # move the player
    game.move_player(game.current_player, dice)
    
    # end the turn

    game.next_turn()

# print game info
print("Game Over!")
print(f"The winner is {game.get_winner().name}")

print("Players Statistics:")
for player in game.players:
    print(f"Player {player.name}:")
    print(f"  Cash: {player.cash}")
    print(f"  Properties: {[property for property in game.map.get_properties_by_owner(player)]}")

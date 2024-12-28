import random

START_CASH = 1000

def start_action(player):
    print(f"{player.name} landed on Start. Collect ${START_CASH}.")
    player.cash += START_CASH

def prison_action(player):
    print(f"{player.name} landed in Prison. Lose a turn.")
    #TODO Implement logic to lose a turn

def airport_action(player):
    print(f"{player.name} landed on Airport. Move to any property.")
    #TODO Implement logic to move to any property

def lottery_action(player):
    prize = random.randint(1, 10) * 1000
    print(f"{player.name} won the lottery! Collect ${prize}.")
    player.cash += prize

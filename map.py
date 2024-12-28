from property import Property
from special_place import SpecialPlace
from game_functions import start_action, prison_action, airport_action, lottery_action
import random

class Map:
    def __init__(self, initial_properties = []):
        self.properties = initial_properties
    
    def add_property(self, property):
        self.properties.append(property)
    
    def get_property(self, index):
        if index < len(self.properties):
            return self.properties[index]
        else:
            return None
    
    def get_properties_by_owner(self, player):
        return [property for property in self.properties if type(property) == Property and property.owner == player]
    
    def get_index(self, property):
        return self.properties.index(property)
        
    def get_size(self):
        return len(self.properties)
    
    def __str__(self):
        return "\n".join([str(property) for property in self.properties])
    
    def __repr__(self): 
        return self.__str__()

Map.vietnam_theme_map = Map([
    SpecialPlace("Go!", start_action),
    # SpecialPlace("Lottery", lottery_action),
    Property("Hanoi", 1000, 500, random.uniform(0, 1), random.randint(1, 5)),
    Property("Hue", 2000, 1000, random.uniform(0, 1), random.randint(1, 5)),
    Property("Saigon", 3000, 1500, random.uniform(0, 1), random.randint(1, 5)),
    SpecialPlace("Lottery", lottery_action),
    Property("Danang", 4000, 400, random.uniform(0, 1), random.randint(1, 5)),
    Property("Halong", 5000, 500, random.uniform(0, 1), random.randint(1, 5)),
    Property("Nhatrang", 6000, 600, random.uniform(0, 1), random.randint(1, 5)),
    SpecialPlace("Prison", prison_action),
    Property("Phuquoc", 7000, 700, random.uniform(0, 1), random.randint(1, 5)),
    Property("Dalat", 8000, 800, random.uniform(0, 1), random.randint(1, 5)),
    Property("Vungtau", 9000, 900, random.uniform(0, 1), random.randint(1, 5)),
    SpecialPlace("Airport", airport_action),
    Property("Cantho", 10000, 1000, random.uniform(0, 1), random.randint(1, 5)),
    Property("Quangninh", 11000, 1100, random.uniform(0, 1), random.randint(1, 5)),
    Property("Quangtri", 12000, 1200, random.uniform(0, 1), random.randint(1, 5))
]) # static variable

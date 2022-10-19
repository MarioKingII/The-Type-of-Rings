from arcade import Vector
from data_classes.game_data import game_data
from data_classes.level_data import level_data

class data_manager:
    def __init__(self):
        pass

    def load_game_data(self) -> game_data:
        return game_data(["0","1","2"])
    
    def load_level_data(self,level_id : str):
        return data_manager.level_dummy_data()
    
    def level_dummy_data() -> level_data:
        level_id = "0"
        route = []
        towers = []
        enemies = 7
        word_data = ["Coconuts","Make","Me","Giggle"]
        for x in range(10):
            route.append((9 * 50,(9 - x) * 50))
            towers.append((350,x * 50))
            enemies = 5
            

        return level_data(level_id=level_id,route=route,towers=towers,enemies=enemies,word_data=word_data)
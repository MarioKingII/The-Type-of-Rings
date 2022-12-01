from typing import NamedTuple
from arcade import Vector
from ..data_classes.game_data import game_data
from ..data_classes.level_data import level_data

class Vector2(NamedTuple):
    x : float
    y : float

class data_manager:
    def __init__(self):
        pass

    def load_game_data(self) -> game_data:
        return game_data(["0", "1", "2"])

    def load_level_data(self, level_id: str):
        dummy_data = data_manager.level_dummy_data()
        dummy_data.level_id = level_id
        return dummy_data
    
    def save_data(self, data: dict):
        pass

    def level_dummy_data() -> level_data:
        level_id = "0"
        route = [Vector2(0,500),Vector2(100,100),Vector2(500,500),Vector2(500,100)]
        towers = [(100,50),(200,50),(300,50),(400,50)]
        enemies = 20
        word_data = ["Coconuts", "Make", "Me", "Giggle"]
        # for x in range(10):
        #     # route.append((9 * 50, (9 - x) * 50))
        #     towers.append((350, 150))
        #     # enemies = 5

        return level_data(
            level_id=level_id,
            route=route,
            towers=towers,
            enemies=enemies,
            word_data=word_data,
        )

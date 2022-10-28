from arcade import SpriteList
from entities.entity import entity


class enemy(entity):

    # TODO: make filepath be data-driven. Different tower types can have a different filepath. I guess this would be filepath_data? Or something like that.
    def __init__(
        self,
        filename: str = ":resources:images/enemies/slimeBlock.png",
        position: tuple[float, float] = (0, 0),
    ):
        super().__init__(filename=filename, position=position)

        # initialization logic goes here.

    def on_update(self, delta_time: float = 1 / 60):
        super().on_update(delta_time)
        # implement logic

    def draw(self, *, filter=None, pixelated=None, blend_function=None):
        super().draw(filter=filter, pixelated=pixelated, blend_function=blend_function)
        # implement any sprite-specific rendering you'd want.

    def getListFromData(positions: int):
        enemies = SpriteList()
        for a in range(positions):
            enemies.append(enemy(position=(0, 0)))
        return enemies
    
    # establishing a starting position always in the same place.
    def startPosition(position):
        start = (0,0)
        position = start
        return position
   
    # here is where we will create and populate the path that the enemies follow.
    positions = {}

    def nextPosition(positions):
        for i in positions:
            position = positions
            

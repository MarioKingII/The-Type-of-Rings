from arcade import SpriteList
from entities.entity import entity


class tower(entity):

    # TODO: make filepath be data-driven. Different tower types can have a different filepath. I guess this would be filepath_data? Or something like that.
    def __init__(
        self,
        filename: str = "images/towerImg.png",
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

    def getListFromData(positions: list[tuple[float, float]]):
        towers = SpriteList()
        for a in positions:
            towers.append(tower(position=a))
        return towers

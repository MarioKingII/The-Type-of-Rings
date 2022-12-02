from arcade import Vector


class level_data:
    def __init__(
        self,
        level_id: str,
        route: list[tuple[float, float]] = list[tuple[float, float]](),
        towers: list[tuple[float, float]] = list[tuple[float, float]](),
        enemies: int = 0,
        word_data: list[str] = list[str](),
    ):
        self.level_id = level_id
        self.route = route
        self.towers = towers
        self.enemies = enemies
        self.word_data = word_data

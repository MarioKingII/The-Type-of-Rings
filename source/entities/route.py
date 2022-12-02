from .entity import Entity


class Route:
    def __init__(self, path: list[tuple[float, float]]) -> None:
        self.path = path

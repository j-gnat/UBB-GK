class Coordinate:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    @property
    def x(self) -> float:
        return self._coordinateX

    @x.setter
    def x(self, value: float) -> None:
        if isinstance(value, (int, float)):
            self._coordinateX = float(value)
        else:
            self.x = None

    @property
    def y(self) -> float:
        return self._coordinateY

    @y.setter
    def y(self, value: float) -> None:
        if isinstance(value, (int, float)):
            self._coordinateY = float(value)
        else:
            self.y = None

    @property
    def coordinates(self) -> tuple[float, float]:
        return (self._coordinateX, self._coordinateY)

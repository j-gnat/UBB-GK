from typing import Optional

class Coordinate:
    def __init__(self, coordinateX, coordinateY):
        self.coordinateX = coordinateX
        self.coordinateY = coordinateY

    @property
    def coordinateX(self) -> Optional[float]:
        return self._coordinateX

    @coordinateX.setter
    def coordinateX(self, value: float) -> None:
        if isinstance(value, (int, float)):
            self._coordinateX = float(value)
        else:
            self.coordinateX = None

    @property
    def coordinateY(self) -> Optional[float]:
        return self._coordinateY

    @coordinateY.setter
    def coordinateY(self, value: float) -> None:
        if isinstance(value, (int, float)):
            self._coordinateY = float(value)
        else:
            self.coordinateY = None

    @property
    def coordinates(self) -> Optional[tuple[Optional[float], Optional[float]]]:
        return (self._coordinateX, self._coordinateY)
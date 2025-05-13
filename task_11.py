class Dessert:
    def __init__(self, name: str = "", calories: int | float = 0):
        self._name = name if isinstance(name, str) and name else ""
        self._calories = calories

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, data) -> None:
        self._name = data if isinstance(data, str) and data else self._name

    @property
    def calories(self):
        return self._calories

    @calories.setter
    def calories(self, data) -> None:
        self._calories = data

    def is_healthy(self) -> bool:
        if isinstance(self._calories, (int,float)):
            return float(self._calories) < 200
        return True

    def is_delicious(self) -> bool:
        return True

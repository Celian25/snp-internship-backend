class Dessert:
    def __init__(self, name: str = "", calories: int | float = 0):
        self._name = name
        self._calories = calories

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, data) -> None:
        self._name = data if isinstance(data, str) and data else self._name

    @property
    def calories(self) -> int | float:
        return self._calories

    @calories.setter
    def calories(self, data) -> None:
        self._calories = data if isinstance(data, (int, float)) else self._calories

    def is_healthy(self) -> bool:
        return float(self._calories) < 200

    def is_delicious(self) -> bool:
        return True

class Dessert:
    def __init__(self, name: str = "", calories: int | float | str = 0):
        self.name = name
        self.calories = calories

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, data) -> None:
        self._name = data if isinstance(data, str) else ""

    @property
    def calories(self) -> int | float | str:
        return self._calories

    @calories.setter
    def calories(self, data) -> None:
        self._calories = data if isinstance(data, (int,float,str)) else 0

    def is_healthy(self) -> bool:
        if isinstance(self._calories, (int,float)) and self._calories < 200:
            return True
        return False

    def is_delicious(self) -> bool:
        return True
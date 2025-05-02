class Dessert:
    def __init__(self, name: str = '', calories: int | float = 0):
        self._name = name
        self._calories = calories

    def get_name(self) -> str:
        return self._name

    def set_name(self, data) -> None:
        self._name = data if isinstance(data, str) and data else self._name

    def get_calories(self) -> int | float:
        return self._calories

    def set_calories(self, data) -> None:
        self._calories = data if isinstance(data, (int, float)) else self._calories

    def is_healthy(self) -> bool:
        return self._calories < 200

    def is_delicious(self) -> bool:
        return True


dessert = Dessert()
# dessert.set_name('Cookie')
# print(dessert.get_name())
print(dessert.is_delicious())

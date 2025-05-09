from task_11 import Dessert


class JellyBean(Dessert):
    def __init__(self, name: str = "", calories: int | float = 0, flavor: str = ""):
        super().__init__(name, calories)
        self._flavor = flavor

    @property
    def flavor(self) -> str:
        return self._flavor

    @flavor.setter
    def flavor(self, data) -> None:
        self._flavor = data if isinstance(data, str) and data else self._flavor

    def is_delicious(self):
        if self._flavor == "black licorice":
            return False
        return True

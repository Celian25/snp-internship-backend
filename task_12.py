from task_11 import Dessert


class JellyBean(Dessert):
    def __init__(self, name: str = "", calories: int | float | str = 0, flavor: str = ""):
        super().__init__(name, calories)
        self.flavor = flavor

    @property
    def flavor(self) -> str:
        return self._flavor

    @flavor.setter
    def flavor(self, data) -> None:
        self._flavor = data if isinstance(data, str) and data else ""

    def is_delicious(self) -> bool:
        if self._flavor.lower().strip() == "black licorice":
            return False
        return True


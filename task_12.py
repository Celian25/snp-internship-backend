from task_11 import Dessert


class JellyBean(Dessert):
    def __init__(self, name: str = '', calories: int | float = 0, flavour: str = ''):
        super().__init__(name, calories)
        self._flavour = flavour

    def get_flavour(self) -> str:
        return self._flavour

    def set_flavour(self, data) -> None:
        self._flavour = data if isinstance(data, str) and data else self._flavour

    def is_delicious(self):
        if self._flavour == 'black licorice':
            return False
        return True


print(JellyBean(flavour='black licorice').is_delicious())

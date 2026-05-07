class Plant:
    def __init__(
        self,
        name: str,
        height: float,
        old: int,
        growrate: float,
    ) -> None:
        self.name = name
        self._height = height
        self._old = old
        self.growth = 0.0
        self.growrate = float(growrate)

    def grow(self) -> None:
        self._height += self.growrate
        self.growth += self.growrate

    def age(self) -> None:
        self._old += 1

    def get_height(self) -> float:
        return round(self._height, 2)

    def get_age(self) -> int:
        return self._old

    def set_height(self, n: float) -> None:
        if n < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height Update rejected\n")
        else:
            self._height = n
            print(f"Height updated: {self._height}cm\n")

    def set_age(self, n: int) -> None:
        if n < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age Update rejected\n")
        else:
            self._old = n
            print(f"Age updated: {self._old} days\n")

    def show(self) -> str:
        return f"{self.name}: {self.get_height()}cm, \
{self.get_age()} days old"


class Flower(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        old: int,
        growrate: float,
        color: str,
        bloomtime: int,
    ) -> None:
        super().__init__(name, height, old, growrate)
        self.bloom = bloomtime
        self.color = color
        self._blooming = False

    def bloom_flower(self) -> str:
        if self._old >= self.bloom:
            self._blooming = True
            return f"{self.name} is blooming beautifully!"
        else:
            return f"{self.name} has not bloomed yet"

    def show(self) -> str:
        base = super().show()
        return f"{base}\n Color: {self.color}\n {self.bloom_flower()}"


class Tree(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        old: int,
        growrate: float,
        trunk: float,
    ) -> None:
        super().__init__(name, height, old, growrate)
        self.trunk = trunk

    def shade(self) -> str:
        return f"Tree {self.name} now produces a shade of \
{self._height}cm long and {self.trunk}cm wide"

    def show(self) -> str:
        base = super().show()
        return f"{base}\n Trunk diameter: {self.trunk}cm"


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        old: int,
        growrate: float,
        harvest: str,
    ) -> None:
        super().__init__(name, height, old, growrate)
        self.harvest = harvest
        self.nutrients = 0

    def grow(self) -> None:
        super().grow()

    def age(self) -> None:
        super().age()
        self.nutrients += 1

    def show(self) -> str:
        base = super().show()
        return f"{base}\n Harvest: {self.harvest}\n \
Nutritional Value: {self.nutrients}"


def main() -> None:
    print("=== Garden Plant Types ===")
    rose = Flower("Rose", 15.0, 10, 1.5, "red", 20)
    oak = Tree("Oak", 200.0, 365, 1, 5.0)
    tomato = Vegetable("Tomato", 5, 10, 2.1, "April")

    print("=== Flower")
    print(f"{rose.show()}")
    print("[asking the rose to bloom]")
    rose.bloom = 10
    print(f"{rose.show()}")

    print("\n=== Tree")
    print(f"{oak.show()}")
    print("[asking the oak to produce shade]")
    print(f"{oak.shade()}")

    print("\n=== Vegetable")
    print(f"{tomato.show()}")
    print("[make tomato grow and age for 20 days]")
    for x in range(20):
        tomato.grow()
        tomato.age()
    print(f"{tomato.show()}")


if __name__ == "__main__":
    main()

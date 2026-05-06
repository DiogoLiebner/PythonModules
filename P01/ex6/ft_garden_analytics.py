class Plant:
    class Stats:
        def __init__(self) -> None:
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0

        def display(self) -> None:
            print(f"Stats: {self._grow_calls} grow, {self._age_calls} age, \
{self._show_calls} show")

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
        self._stats = Plant.Stats()

    @staticmethod
    def is_older_than_year(age):
        return age > 365

    @classmethod
    def anonymous(cls):
        return cls("Unkown Plant", 0, 0, 0.0)

    def grow(self) -> None:
        self._stats._grow_calls += 1
        self._height += self.growrate
        self.growth += self.growrate

    def age(self) -> None:
        self._stats._age_calls += 1
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
        self._stats._show_calls += 1
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

    @classmethod
    def anonymous(cls):
        return cls("Unknown", 0, 0, 0.0, "unknown", 0)

    def bloom_flower(self) -> str:
        if self._old >= self.bloom:
            self._blooming = True
            return f"{self.name} is blooming beautifully!"
        else:
            return f"{self.name} has not bloomed yet"

    def show(self) -> str:
        base = super().show()
        return f"{base}\n Color: {self.color}\n {self.bloom_flower()}"


class Seed(Flower):
    def __init__(
            self,
            name: str,
            height: float,
            old: int,
            growrate: float,
            color: str,
            bloomtime: int,
            seed_count: int = 0,
    ) -> None:
        super().__init__(name, height, old, growrate, color, bloomtime)
        self._seed_count = seed_count
        self._stats = Flower.Stats()

    @classmethod
    def anonymous(cls) -> "Seed":
        return cls("Unknown", 0, 0, 0.0, "unknown", 0, 0)

    def bloom_flower(self) -> str:
        result = super().bloom_flower()
        if self._blooming:
            self._seed_count = 42
        return result

    def show(self) -> str:
        base = super().show()
        return f"{base}\n Seeds: {self._seed_count}"


class Tree(Plant):
    class Stats(Plant.Stats):
        def __init__(self) -> None:
            super().__init__()
            self._shade_calls = 0

        def display(self) -> None:
            super().display()
            print(f"{self._shade_calls} shade")

    _stats: "Tree.Stats"

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
        self._stats = Tree.Stats()

    @classmethod
    def anonymous(cls) -> "Tree":
        return cls("Unknown", 0, 0, 0.0, 0)

    def shade(self) -> str:
        return f"Tree {self.name} now produces a shade of \
{self._height}cm long and {self.trunk}cm wide"

    def produce_shade(self) -> str:
        self._stats._shade_calls += 1
        return f"{self._stats._shade_calls} shade"

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
        self._stats = Vegetable.Stats()

    def grow(self) -> None:
        super().grow()

    def age(self) -> None:
        super().age()
        self.nutrients += 1

    def show(self) -> str:
        base = super().show()
        return f"{base}\n Harvest: {self.harvest}\n \
Nutritional Value: {self.nutrients}"


def display_stats(plant):
    print(f"[statistics for {plant.name}]")
    plant._stats.display()


def main() -> None:
    print("=== Garden statistics ===")
    rose = Flower("Rose", 15.0, 10, 8, "red", 20)
    oak = Tree("Oak", 200.0, 365, 1, 5.0)
    sunflower = Seed("Sunflower", 80.0, 45, 30, "yellow", 50, 0)

    print("\n=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older_than_year(400)}")

    print("\n=== Flower")
    print(rose.show())
    display_stats(rose)
    print("[asking the rose to grow and bloom]")
    rose.bloom = 10
    rose.grow()
    print(rose.show())
    display_stats(rose)

    print("\n=== Tree")
    print(oak.show())
    display_stats(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print(oak.shade())
    display_stats(oak)

    print("\n=== Seed")
    print(sunflower.show())
    print("[make sunflower grow, age and bloom]")
    sunflower._old = 64
    sunflower.age()
    sunflower.grow()
    print(sunflower.show())
    display_stats(sunflower)

    print("\n=== Anonymous")
    anon = Plant.anonymous()
    print(anon.show())
    display_stats(anon)


if __name__ == "__main__":
    main()

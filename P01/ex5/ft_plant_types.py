class Plant:
    def __init__(self, name, height, old, growrate):
        self.name = name
        self._height = int(height)
        self._old = int(old)
        self.growth = 0
        self.growrate = float(growrate)

    def grow(self):
        self._height += self.growrate
        self.growth += self.growrate

    def age(self):
        self._old += 1

    def get_height(self):
        return self._height

    def get_age(self):
        return self._old

    def set_height(self, n):
        if n < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected\n")
        else:
            self._height = n
            print(f"Height updated: {self._height}cm\n")

    def set_age(self, n):
        if n < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected\n")
        else:
            self._old = n
            print(f"Age updated: {self._old} days\n")

    def show(self):
        return f"{self.name}: {self._height:.1f} cm, {self._old:.0f} days old"


class Flower(Plant):
    def __init__(self, name, height, old, growrate, color, bloomtime):
        super().__init__(name, height, old, growrate)
        self.bloom = bloomtime
        self.color = color
        self._blooming = False

    def bloom_flower(self):
        if self._old >= self.bloom:
            self._blooming = True
            print("f{self.name} is now blooming!\n")
        else:
            days_left = self.bloom - self._old
            print(f"{self.name} is not ready to bloom yet ({days_left} days left)\n")

    def show(self):
        base = super().show()
        status = "blooming" if self._blooming else "not blooming"
        return f"{base}, color: {self.color}, bloom at: {self.bloom} days [{status}]"


class Tree(Plant):
    def __init__(self, name, height, old, growrate, trunk, shade):
        super().__init__(name, height, old, growrate)
        self.trunk = trunk
        self.shade = trunk * height

    def grow(self):
        super().grow()
        self.shade = self.trunk * self._heightheight

    def show(self):
        base = super().show()
        return f"{base}, trunk: {self.trunk:.1f} cm, shade: {self.shade:.1f} m2"


class Vegetable(Plant):
    def __init__(self, name, height, old, growrate, harvest, nutrients):
        super().__init__(name, height, old, growrate)
        self.harvest = harvest
        self.nutrients = 0

    def grow(self):
        super().grow()
        self.nutrients += 2

    def age(self):
        super().age()
        self.nutrients += 1

    def show(self):
        base = super().show()
        return f"{base}, harvest: {self.harvest} days, nutrients: {self.nutrients}"


def main():
    print("=== Garden Plant Types ===")
    rose = Flower("Rose", 30, 10, 1.5, "red", 20)
    oak = Tree("Oak", 500, 3650, 10.0, 80, 3)
    carrot = Vegetable("Carrot", 15, 5, 0.8, 30, 0)

    print(rose.show())
    print(oak.show())
    print(carrot.show())

    # --- Flower blooming ---
    print("\n" + "=" * 50)
    print("         FLOWER BLOOMING")
    print("=" * 50)

    rose.bloom_flower()

    print("Aging rose until bloom time...")
    for _ in range(10):
        rose.age()

    print(rose.show())
    rose.bloom_flower()

    # --- Vegetable nutrients ---
    print("=" * 50)
    print("      VEGETABLE NUTRIENTS")
    print("=" * 50)

    print(f"Carrot nutrients at start: {carrot.nutrients}")

    print("\nGrowing carrot 3 times...")
    for _ in range(3):
        carrot.grow()
    print(carrot.show())

    print("\nAging carrot 3 times...")
    for _ in range(3):
        carrot.age()
    print(carrot.show())

    # --- Tree grows and shade updates ---
    print("\n" + "=" * 50)
    print("         TREE GROWING")
    print("=" * 50)

    print(f"Before: {oak.show()}")
    oak.grow()
    oak.grow()
    print(f"After:  {oak.show()}")


if __name__ == "__main__":
    main()

class Plant:
    def __init__(self, name, height, old, growrate):
        self.name = name
        self.height = int(height)
        self.old = int(old)
        self.growth = 0
        self.growrate = float(growrate)

    def grow(self):
        self.height += self.growrate
        self.growth += self.growrate

    def age(self):
        self.old += 1

    def set_height(self, n):
        if n < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected\n")
        else:
            self.height = n
            print(f"Height updated: {self.height}cm\n")

    def set_age(self, n):
        if n < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected\n")
        else:
            self.old = n
            print(f"Age updated: {self.old} days\n")

    def get_height(self):
        print(f"{self.name} Height: {self.heigh} cm")

    def get_ate(self):
        print(f"{self.name} Age: {self.old} Days")

    def show(self):
        return f"{self.name}: {self.height:.1f} cm, {self.old:.0f} days old"


class Flower(Plant):
    def __init__(self, name, height, old, growrate, color, bloomtime):
        super().__init__(name, height, old, growrate)
        self.bloom = bloomtime
        self.color = color


class Tree(Plant):
    def __init__(self, name, height, old, growrate, trunk, shade):
        super().__init__(name, height, old, growrate)
        self.trunk = trunk
        self.shade = trunk * height


class Vegetable(Plant):
    def __init__(self, name, height, old, growrate, harvest, nutrients):
        super().__init__(name, height, old, growrate)
        self.harvest = harvest
        self.nutrients = nutrients


def main():
    

if __name__ == "__main__":
    main()

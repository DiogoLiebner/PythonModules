class Plant:

    class Stats:
        def __init__(self):
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0

        def display(self):
            print(f"    grow() calls : {self._grow_calls}")
            print(f"    age()  calls : {self._age_calls}")
            print(f"    show() calls : {self._show_calls}")

    def __init__(self, name, height, old, growrate):
        self.name = name
        self._height = int(height)
        self._old = int(old)
        self.growth = 0
        self.growrate = float(growrate)
        self._stats = Plant.Stats()          # each plant gets its own Stats

    @staticmethod
    def is_older_than_year(age):                # no self or cls needed
        return age > 365

    @classmethod
    def anonymous(cls):                         # alternative constructor
        return cls("Unknown", 0, 0, 0.0)

    def grow(self):
        self._stats._grow_calls += 1
        self._height += self.growrate
        self.growth += self.growrate

    def age(self):
        self._stats._age_calls += 1
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
        self._stats._show_calls += 1
        return f"{self.name}: {self._height:.1f} cm, {self._old:.0f} days old"


# ── Flower ─────────────────────────────────────────────────────────────
class Flower(Plant):
    def __init__(self, name, height, old, growrate, color, bloomtime):
        super().__init__(name, height, old, growrate)
        self.color = color
        self.bloom = bloomtime
        self._blooming = False

    @classmethod
    def anonymous(cls):
        return cls("Unknown", 0, 0, 0.0, "unknown", 0)   # extra fields for Flower

    def bloom_flower(self):
        if self._old >= self.bloom:
            self._blooming = True
            print(f"{self.name} is now blooming!\n")
        else:
            days_left = self.bloom - self._old
            print(f"{self.name} is not ready to bloom yet ({days_left} days left)\n")

    def show(self):
        base   = super().show()
        status = "blooming" if self._blooming else "not blooming"
        return f"{base}, color: {self.color}, bloom at: {self.bloom} days [{status}]"


# ── Seed ───────────────────────────────────────────────────────────────
class Seed(Flower):
    def __init__(self, name, height, old, growrate, color, bloomtime, seed_count=0):
        super().__init__(name, height, old, growrate, color, bloomtime)
        self._seed_count = seed_count               # 0 until flower has bloomed

    @classmethod
    def anonymous(cls):
        return cls("Unknown", 0, 0, 0.0, "unknown", 0, 0)

    def bloom_flower(self):
        super().bloom_flower()                      # run Flower's bloom logic
        if self._blooming:
            self._seed_count = 10                   # seeds appear once bloomed

    def show(self):
        base = super().show()                       # Flower → Plant output
        return f"{base}, seeds: {self._seed_count}"


# ── Tree ───────────────────────────────────────────────────────────────
class Tree(Plant):

    # extends Plant.Stats with an extra counter
    class Stats(Plant.Stats):
        def __init__(self):
            super().__init__()
            self._shade_calls = 0

        def display(self):
            super().display()                       # show base stats first
            print(f"    produce_shade() calls : {self._shade_calls}")

    def __init__(self, name, height, old, growrate, trunk, shade):
        super().__init__(name, height, old, growrate)
        self.trunk = trunk
        self.shade = trunk * self._height
        self._stats = Tree.Stats()                  # override with Tree's Stats

    @classmethod
    def anonymous(cls):
        return cls("Unknown", 0, 0, 0.0, 0, 0)

    def grow(self):
        super().grow()
        self.shade = self.trunk * self._height      # recalculate shade after growing

    def produce_shade(self):
        self._stats._shade_calls += 1
        return f"{self.name} produces {self.shade:.1f} m² of shade"

    def show(self):
        base = super().show()
        return f"{base}, trunk: {self.trunk:.1f} cm, shade: {self.shade:.1f} m²"


# ── Vegetable ──────────────────────────────────────────────────────────
class Vegetable(Plant):
    def __init__(self, name, height, old, growrate, harvest, nutrients):
        super().__init__(name, height, old, growrate)
        self.harvest = harvest
        self.nutrients = 0                          # always starts at 0

    @classmethod
    def anonymous(cls):
        return cls("Unknown", 0, 0, 0.0, 0, 0)

    def grow(self):
        super().grow()
        self.nutrients += 2

    def age(self):
        super().age()
        self.nutrients += 1

    def show(self):
        base = super().show()
        return f"{base}, harvest: {self.harvest} days, nutrients: {self.nutrients}"


# ── Standalone stats display function ─────────────────────────────────
def display_stats(plant):
    print(f"  Stats for [{plant.name}]:")
    plant._stats.display()


# ── Main ───────────────────────────────────────────────────────────────
def main():
    print("=" * 55)
    print("            CREATING PLANTS")
    print("=" * 55)

    rose = Flower("Rose", 30, 10, 1.5, "red", 20)
    oak = Tree("Oak", 500, 3650, 10.0, 80, 3)
    carrot = Vegetable("Carrot", 15, 5, 0.8, 30, 0)
    tulip = Seed("Tulip", 20, 5, 1.0, "yellow", 15)

    print(rose.show())
    print(oak.show())
    print(carrot.show())
    print(tulip.show())

    # --- Anonymous plants ---
    print("\n" + "=" * 55)
    print("          ANONYMOUS PLANTS")
    print("=" * 55)

    anon_plant = Plant.anonymous()
    anon_flower = Flower.anonymous()
    anon_tree = Tree.anonymous()
    print(anon_plant.show())
    print(anon_flower.show())
    print(anon_tree.show())

    # --- Static method ---
    print("\n" + "=" * 55)
    print("          AGE CHECKS")
    print("=" * 55)

    print(f"Is oak older than a year?    {Plant.is_older_than_year(oak.get_age())}")
    print(f"Is carrot older than a year? {Plant.is_older_than_year(carrot.get_age())}")

    # --- Flower blooming / Seed ---
    print("\n" + "=" * 55)
    print("         BLOOMING & SEEDS")
    print("=" * 55)

    tulip.bloom_flower()                        # not ready yet
    for _ in range(10):
        tulip.age()
    tulip.bloom_flower()                        # now blooms and gets seeds
    print(tulip.show())

    # --- Vegetable nutrients ---
    print("\n" + "=" * 55)
    print("        VEGETABLE NUTRIENTS")
    print("=" * 55)

    print(f"Carrot nutrients at start: {carrot.nutrients}")
    for _ in range(3):
        carrot.grow()
    for _ in range(3):
        carrot.age()
    print(carrot.show())

    # --- Tree shade ---
    print("\n" + "=" * 55)
    print("           TREE SHADE")
    print("=" * 55)

    print(oak.produce_shade())
    oak.grow()
    oak.grow()
    print(oak.produce_shade())

    # --- Statistics ---
    print("\n" + "=" * 55)
    print("           STATISTICS")
    print("=" * 55)

    display_stats(rose)
    display_stats(oak)          # will also show produce_shade() calls
    display_stats(carrot)
    display_stats(tulip)


if __name__ == "__main__":
    main()

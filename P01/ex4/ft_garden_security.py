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


def main():
    print("=== Garden Secutity System ===")
    rose = Plant("Rose", 15, 10, 0.8)
    print(f"Plant created: {rose.show()}\n")
    rose.set_height(60)
    rose.set_age(-3)
    print(f"Current state: {rose.show()}")


if __name__ == "__main__":
    main()

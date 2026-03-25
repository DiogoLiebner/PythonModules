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

    def show(self):
        return f"{self.name}: {self.height:.1f} cm, {self.old:.0f} days old"


def main():
    print("=== Garden Secutity System ===")
    rose = Plant("Rose", 15, 10, 0.8)
    print(f"Plant created: {rose.show()}\n")
    rose.set_height(60)
    rose.set_age(-3)
    print(f"Current state: {rose.show()}")


if __name__ == "__main__":
    main()

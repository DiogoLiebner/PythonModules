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

    def show(self):
        print(f"{self.name}: {self.height:.1f} cm, {self.old:.0f} days old")


def main():
    rose = Plant("Rose", 25, 30, 0.8)
    weekday = 1
    for x in range(weekday, weekday+7):
        print(f"=== Day {weekday} ===")
        weekday += 1
        rose.show()
        if weekday == 8:
            break
        rose.grow()
        rose.age()
    print(f"Growth this week: {rose.growth:.1f}cm")


if __name__ == "__main__":
    main()

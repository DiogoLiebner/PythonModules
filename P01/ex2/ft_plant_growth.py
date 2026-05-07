class Plant:
    def __init__(
        self,
        name: str,
        height: int,
        old: int,
        growrate: float,
    ) -> None:
        self.name = name
        self.height = float(height)
        self.old = int(old)
        self.growth = 0.0
        self.growrate = float(growrate)

    def grow(self) -> None:
        self.height += self.growrate
        self.growth += self.growrate

    def age(self) -> None:
        self.old += 1

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 2)}cm, {self.old} days old")


def main() -> None:
    rose = Plant("Rose", 25, 30, 0.8)
    weekday = 1
    print("=== Garden Plant Growth ===")
    rose.show()
    for x in range(weekday, weekday+7):
        print(f"=== Day {weekday} ===")
        weekday += 1
        rose.grow()
        rose.age()
        rose.show()
    print(f"Growth this week: {rose.growth} cm")


if __name__ == "__main__":
    main()

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

    def show(self) -> str:
        return f"{self.name}: {round(self.height, 2)}cm, {self.old} days old"


def main() -> None:
    rose = Plant("Rose", 25, 30, 0.8)
    oak = Plant("Oak", 200, 365, 0.7)
    cactus = Plant("Cactus", 5, 90, 0.1)
    sunflower = Plant("Sunflower", 90, 45, 2)
    fern = Plant("Fern", 15, 120, 0.2)
    print("=== Plant Factory Output ===")
    print(f"Created: {rose.show()}")
    print(f"Created: {oak.show()}")
    print(f"Created: {cactus.show()}")
    print(f"Created: {sunflower.show()}")
    print(f"Created: {fern.show()}")


if __name__ == "__main__":
    main()

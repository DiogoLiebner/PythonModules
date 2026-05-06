class Plant:
    def __init__(
        self,
        name: str,
        height: int,
        old: int,
        growrate: float,
    ) -> None:
        self.name = name
        self._height = float(height)
        self._old = int(old)
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


def main() -> None:
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15, 10, 0.8)
    print(f"Plant created: {rose.show()}\n")
    rose.set_height(-5)
    rose.set_height(60)
    rose.set_age(-3)
    rose.set_age(40)
    print(f"Current state: {rose.show()}")


if __name__ == "__main__":
    main()

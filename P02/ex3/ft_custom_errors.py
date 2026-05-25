class GardenError(Exception):
    """
        Base error for all garden-related problems.
    """
    def __init__(self, message="Unknown garden error": str) -> None:
        self.message = message
        super().__init__(self.message)


class PlantError(GardenError):
    """
        Exception raised when problem found with plants
    """
    def __init__(self, plant: str, message="GardenError": str) -> None:
        self.message = message
        self.plant = plant
        super().__init__(self.message)

    def __str__(self) -> str:
        return f"Caught {self.message}: The {self.plant} plant is wilting!"


class WaterError(GardenError):
    """
        Exception raised when problem found with watering
    """
    def __init__(self, message="GardenError": str) -> None:
        self.message = message
        super().__init__(self.message)

    def __str__(self) -> str:
        return f"Caught {self.message}: Not enough water in the tank!"


def main() -> None:
    print("=== Custom Garden Errors Demo ===\n")
    errors = [
        PlantError("Rose", "PlantError"),
        WaterError("WaterError"),
        PlantError("Tomato"),
        WaterError(),
        GardenError(),
    ]

    for error in errors:
        try:
            raise error
        except GardenError as e:
            print(f"[{type(e).__name__}] {e}")


if __name__ == "__main__":
    main()

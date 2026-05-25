class GardenError(Exception):
    """
        Base error for all garden-related problems.
    """
    def __init__(self, message="Unknown garden error": str) -> None:
        self.message = message
        super().__init__(self.message)


class WaterError(GardenError):
    """
        Exception raised when problem found with watering
    """
    def __init__(self, plant, message="GardenError") -> None:
        self.message = message
        self.plant = plant
        super().__init__(self.message)

    def __str__(self) -> str:
        return f"Caught {self.message}: Invalid plant name to water:\
'{self.plant}'"


def water_plant(plant_name: str) -> None:
    try:
        if plant_name != str.capitalize(plant_name):
            raise WaterError(plant_name, "WaterError")
        print(f"Watering {plant_name}: [OK]")
    except WaterError as e:
        print(e)
        print(".. ending tests and returning to main")
    finally:
        pass


def test_watering_system() -> None:
    print("Testing valid plants...")
    print("Opening watering system")
    plants = [
        "Tomato",
        "Lettuce",
        "Carrots",
    ]
    for plant in plants:
        water_plant(plant)
    print("Closing watering systems")

    print("\nTesting invalid plants...")
    print("Opening watering system")
    invalid_plants = [
        "Tomato",
        "lettuce",
    ]
    for invalid_plant in invalid_plants:
        water_plant(invalid_plant)
    print("Closing watering systems")

    print("\nCleanup always happens, even with errors!")


def main() -> None:
    print("=== Garden Watering System ===\n")
    test_watering_system()


if __name__ == "__main__":
    main()

class GardenError(Exception):
    """
        Base error for all garden-related problems.
    """
    def __init__(self, message="Unknown garden error"):
        self.message = message
        super().__init__(self.message)


class WaterError(GardenError):
    """
        Exception raised when problem found with watering
    """
    def __init__(self, plant, message="GardenError"):
        self.message = message
        self.plant = plant
        super().__init__(self.message)

    def __str__(self):
        return f"Caught {self.message}: Invalid plant name to water:\
'{self.plant}'"


def water_plant(plant_name):
    """
        Function calling the try/except/finally block to test for
        uncapitalized plants
    """
    try:
        if plant_name != str.capitalize(plant_name):
            raise WaterError(plant_name, "WaterError")
        print(f"Watering {plant_name}: [OK]")
    except WaterError as e:
        print(e)
        print(".. ending tests and returning to main")
    finally:
        pass


def test_watering_system():
    # Testing Valid Plants with correct capitalization
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

    # Testing Invalid Plants with some incorrect capitalization
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


def main():
    print("=== Garden Watering System ===\n")
    test_watering_system()


if __name__ == "__main__":
    main()

def water_plant(plant_name):


def test_watering_system():
    # Testing Valid Plants with correct capitalization
    print("Testing valid plants...")
    print("Opening watering system")
    plants = [
        "Tomato",
        "Lettuce",
        "Carrots",
    ]
    water_plant("Tomato")
    water_plant("Lettuce")
    water_plant("Carrots")

    # Testing Invalid Plants with some incorrect capitalization
    print("Testing invalid plants...")
    print("Opening watering system")
    water_plant("Tomato")
    water_plant("lettuce")


def main():
    print("=== Garden Watering System ===\n")
    test_watering_system()


if __name__ == "__main__":
    main()

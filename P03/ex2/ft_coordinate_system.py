import math


def get_player_pos():
    while True:
        raw_coords = input("Enter new coordinates as floats in format \
'x,y,z':")
        coords = raw_coords.split()

        if len(coords) != 3:
            print("Invalid Syntax")
            continue

        try:
            x, y, z = float(coords[0]), float(coords[1]), float(coords[2])
            return x, y, z

        except ValueError:
            print(f"Error on parameter '{coords}'")


def main():
    print("=== Game Coordinate System ===")

    print("Get a first set of coordinates")
    x, y, z = get_player_pos()
    print(f"Got a first tuple: {x}, {y}, {z}")
    print(f"It includes: X={x}, Y={y}, Z={z}")
    dist = math.sqrt(x**2 + y**2 + z**2)
    print(f"Distance to center: {round(dist, 4)}")

# MAKE SECOND SET OF COORDINATES THE NEW CENTER
    print("Get a second set of coordinates")
    x, y, z = get_player_pos()
    print(f"Got a second tuple{x}, {y}, {z}")
    print(f"It includes: X={x}, Y={y}, Z={z}")
    dist = math.sqrt(x**2 + y**2 + z**2)
    print(f"Distance to center: {round(dist, 4)}")


if __name__ == "__main__":
    main()

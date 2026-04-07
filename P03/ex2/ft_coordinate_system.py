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
    x1, y1, z1 = get_player_pos()
    print(f"Got a first tuple: {x1}, {y1}, {z1}")
    print(f"It includes: X={x1}, Y={y1}, Z={z1}")
    dist = math.sqrt(x1**2 + y1**2 + z1**2)
    print(f"Distance to center: {round(dist, 4)}")

    print("Get a second set of coordinates")
    x2, y2, z2 = get_player_pos()
    print(f"Got a second tuple: {x2}, {y2}, {z2}")
    print(f"It includes: X={x2}, Y={y2}, Z={z2}")
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    print(f"Distance to center: {round(dist, 4)}")


if __name__ == "__main__":
    main()

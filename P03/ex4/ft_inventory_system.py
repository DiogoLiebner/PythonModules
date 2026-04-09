import sys


def main() -> None:
    print("=== Inventory System Analysis ===\n")
    items = {}

    for entry in sys.argv[1:]:
        if ":" not in entry:
            print(f"Error - invalid parameter '{entry}'")
        else:
            try:
                name, quantity = entry.split(":")
                if name not in items:
                    items[name] = int(quantity)
                else:
                    print(f"Redundant item '{entry}' - discarding")
            except ValueError:
                print(f"Quantity error for '{name}':\
invalid literal for int() with base 10: 'value'")

    print(f"Got inventory: {items}")
    print(f"Item list: {list(items.keys())}")
    print(f"Total quantity of the {len(items)} items: {sum(items.values())}")
    for name, quantity in items.items():
        print(f"Item {name} represents\
 {(quantity / sum(items.values()))*100:.1f}%")

    maxvalue = 0
    maxname = " "
    minvalue = 2147483647
    minname = " "
    for name, quantity in items.items():
        if maxvalue < quantity:
            maxvalue = quantity
            maxname = name
        if minvalue > quantity:
            minvalue = quantity
            minname = name

    print(f"Item most abundant: {maxname} with quantity {maxvalue}")
    print(f"Item lest abundant: {minname} with quantity {minvalue}")
    items.update({"magic_item": 1})
    print(f"Updated inventory: {items}")


if __name__ == "__main__":
    main()

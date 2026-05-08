import alchemy


def main() -> None:
    print("=== Distillation 1 ===")
    print("Using: 'import alchemy' structure to access potions")
    print(f"Testing strength_potion: {alchemy.strength_potion()}")
    print(f"Testing healing potion: {alchemy.healing_potion()}")


if __name__ == "__main__":
    main()

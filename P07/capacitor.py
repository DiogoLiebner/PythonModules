import ex1.creaturefactoryevolved as cfe


def main() -> None:
    flame_factory = cfe.FlameFactory()
    aqua_factory = cfe.AquaFactory()

    flame_base = flame_factory.create_base()
    flame_evolved = flame_factory.create_evolved(flame_base)
    aqua_base = aqua_factory.create_base()
    aqua_evolved = aqua_factory.create_evolved(aqua_base)

    print("Testing factory")
    print(flame_base.describe())
    print(flame_base.attack())
    print(flame_evolved.describe())
    print(flame_evolved.attack())

    print("\nTesting factory")
    print(aqua_base.describe())
    print(aqua_base.attack())
    print(aqua_evolved.describe())
    print(aqua_evolved.attack())

    print("\nTesting battle")
    print(flame_base.describe())
    print(" vs.")
    print(aqua_base.describe())
    print(" fight!")
    print(flame_base.attack())
    print(aqua_base.attack())


if __name__ == "__main__":
    main()

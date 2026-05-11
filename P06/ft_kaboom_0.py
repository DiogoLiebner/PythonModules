from alchemy.grimoire import light_spell_record


def main() -> None:
    print("=== Kaboom 0 ===")
    print("Using grimoire module directly")
    print(f"Testing record_light_spell: {light_spell_record('Fantasy', 'Earth ,fire, air')}")


if __name__ == "__main__":
    main()
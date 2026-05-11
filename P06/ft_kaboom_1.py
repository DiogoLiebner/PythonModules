from alchemy.grimoire.dark_spellbook import dark_spell_record


def main() -> None:
    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directly")
    print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")
    print(f"{dark_spell_record('Dark Blast', 'bats, frogs, arsenic')}")


if __name__ == "__main__":
    main()

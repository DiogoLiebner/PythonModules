from . import dark_validator


def dark_spell_allowed_ingredients() -> list:
    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    validation_result = dark_validator.validate_ingredients(ingredients)

    if "VALID" in validation_result:
        msg = f"Spell recorded: {spell_name} ({ingredients} - VALID)"
        return msg
    else:
        invalid_msg = "Spell '{}' rejected. Invalid ingredients: {}"
        return invalid_msg.format(spell_name, ingredients)

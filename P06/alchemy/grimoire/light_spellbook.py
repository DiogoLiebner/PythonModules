import light_validator


def light_spell_allowed_ingredients() -> list:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    validation_result = light_validator.validate_ingredients(ingredients)

    if "VALID" in validation_result:
        msg = f"Spell '{spell_name}' recorded with ingredients: {ingredients}"
        return msg
    else:
        invalid_msg = "Spell '{}' rejected. Invalid ingredients: {}"
        return invalid_msg.format(spell_name, ingredients)

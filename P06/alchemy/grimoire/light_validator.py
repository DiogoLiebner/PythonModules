from . import light_spellbook


def validate_ingredients(ingredients: str) -> str:
    allowed = light_spellbook.light_spell_allowed_ingredients()
    if ingredients.lower() in allowed:
        return f"{ingredients.lower()} VALID"
    else:
        return f"{ingredients.lower()} INVALID"

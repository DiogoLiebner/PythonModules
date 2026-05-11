from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed = dark_spell_allowed_ingredients()
    if ingredients.lower() in allowed:
        return f"{ingredients.lower()} VALID"
    else:
        return f"{ingredients.lower()} INVALID"

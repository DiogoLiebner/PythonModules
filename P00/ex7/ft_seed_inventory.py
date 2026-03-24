def ft_seed_inventory(seeds: str, quant: int, unit: str) -> None:
    if unit == "packets":
        print(f"{seeds} seeds: {quant} {unit} available")
    elif unit == "grams":
        print(f"{seeds} seeds: {quant} {unit} total")
    elif unit == "area":
        print(f"{seeds} seeds: covers {quant} square meters")
    else:
        print("Unknown unit type")

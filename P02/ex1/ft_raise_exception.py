def input_temperature(temp_str: str) -> None:
    print(f"Input data is '{temp_str}'")
    try:
        intstr = int(temp_str)
        if (intstr > 40):
            print(f"Caught input_temperature error: \
{intstr}°C is too hot for plants (Max 40°C)\n")
        elif (intstr < 0):
            print(f"Caught input_temperature error: \
{intstr}°C is too cold for plants (Min 0°C)\n")
        else:
            print(f"Temperature is now {intstr}°C\n")
    except ValueError:
        print(f"Caught input_temperature error: \
invalid literal for int() with base 10: '{temp_str}'\n")


def test_temperature() -> None:
    input_temperature('25')
    input_temperature('abc')
    input_temperature('100')
    input_temperature('-50')
    print("All tests completed - program didn't crash!\n")


def main() -> None:
    print("=== Garden Temperature ===\n")
    test_temperature()


if __name__ == "__main__":
    main()

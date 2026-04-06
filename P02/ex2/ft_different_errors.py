def test_error_types(operation_number):
    """
        Testing different Error types
    """
    a = "42Porto"
    b = 42
    try:
        if operation_number == 0:
            int('abc')
        elif operation_number == 1:
            9 / 0
        elif operation_number == 2:
            open('Hello_world.txt')
        elif operation_number == 3:
            a = "42Porto"
            b = 42
            print(a + b + a)
        else:
            print("Operation completed successfully\n")
    except (ValueError, ZeroDivisionError, FileNotFoundError,
            TypeError) as error:
        match error:
            case ValueError():
                print("Caught ValueError: invalid literal for \
int() with base 10: 'abc'\n")
            case ZeroDivisionError():
                print("Caught ZeroDivisionError: division by zero\n")
            case FileNotFoundError():
                print("Caught FileNotFoundError: [Hello_World.txt] \
No such file or directory: '/non/existent/file'\n")
            case TypeError():
                print("Caught TypeError: can only concatenate str \
(not 'int') to str\n")


def garden_operations(operation_number):
    test_error_types(operation_number)


def main():
    i = 0
    print("=== Garden Error Types Demo ===\n")
    while (i < 5):
        print(f"Testing operation {i}...")
        garden_operations(i)
        i += 1
    print("All error types tested successfully!")


if __name__ == "__main__":
    main()

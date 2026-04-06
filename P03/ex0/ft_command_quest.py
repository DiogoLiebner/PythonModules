import sys


def main():
    print("=== Command Quest ===")
    arg_count = 1
    total_args = len(sys.argv)
    print(f"Program name: {sys.argv[0]}")
    while arg_count < total_args:
        if total_args != 1:
            print(f"Argument {arg_count}: {sys.argv[arg_count]}")
        else:
            print("No arguments provided!")
        arg_count += 1
    print(f"Total arguments: {total_args}")


if __name__ == "__main__":
    main()

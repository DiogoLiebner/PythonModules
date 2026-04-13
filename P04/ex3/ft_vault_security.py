def secure_archive(
    filename: str,
    action: str = "read",
    content: str | None = None) 
    -> tuple[bool, str]:

    if action == "read":
        try:
            with open(filename, "r") as fh:
                return True, fh.read()
        except FileNotFoundError:
            print(f"Error opening file '{filename}': [Errno 2]\
 No file ordirectory: '{filename}'")
        except PermissionError:
            print(f"Error opening file '{filename}': [Errno 13]\
 Permission denied: '{filename}'")

    if content is None:
        return False, "No content provided for write operation"

    try:
        with open(filename, "w") as fh:
            fh.write(content)
        return True, "Content successfully written to file"
    except FileNotFoundError:
        print(f"Error opening file '{filename}': [Errno 2]\
 No file ordirectory: '{filename}'")
    except PermissionError:
        print(f"Error opening file '{filename}': [Errno 13]\
 Permission denied: '{filename}'")


def main() -> None:
    print("=== Cyber Archives Security ===\n")
    secure_archive()


if __name__ == "__main__":
    main()

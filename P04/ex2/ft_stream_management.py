import sys
import typing


def main() -> None:
    print("=== Cyber Archives ===\n")
    filename = sys.argv[1]

    print(f"Accessing file '{filename}'")
    try:
        f = open(filename)
        print("---\n")
        print(f.read())
        print("---\n")
        f.close()
        print(f"File '{filename}' closed.")
    except (FileNotFoundError, PermissionError) as error:
        match error:
            case FileNotFoundError():
                print(f"[STDERR] Error opening file '{filename}': [Errno 2]\
 No file ordirectory: '{filename}'", file=sys.stderr)
                return
            case PermissionError():
                print(f"[STDERR] Error opening file '{filename}': [Errno 13]\
 Permission denied: '{filename}'", file=sys.stderr)
                return

    print("Transformm data:")
    print("---\n")
    with open(filename, "r") as f:
        for line in f:
            line = line.rstrip("\n")
            print(line + "#")

    print("---\n")

    print("Enter new file name (or empty): ")
    output_filename = sys.stdin.readline().strip()
    if output_filename == "":
        print("Not Saving Data.")
    else:
        try:
            print(f"Saving data to '{output_filename}.'")
            fout = open(output_filename, "w")
            fin = open(filename, "r")
            for line in fin:
                line = line.rstrip("\n")
                fout.write(line + "#\n")
            fin.close()
            fout.close()
            print(f"Data saved in file '{output_filename}.'")
        except PermissionError:
            print(f"[STDERR] Error opening file '{filename}': [Errno 13]\
 Permission denied: '{filename}'", file=sys.stderr)
            return


if __name__ == "__main__":
    main()

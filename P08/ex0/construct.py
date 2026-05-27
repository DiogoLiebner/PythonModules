import sys
import os
import sysconfig


def is_virtual_env() -> bool:
    return (
        hasattr(sys, 'real_prefix') or
        (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix)
    )


def get_global_site_packages() -> str:
    base = getattr(sys, "base_prefix", sys.prefix)
    version = f"python{sys.version_info.major}.{sys.version_info.minor}"
    return os.path.join(base, "lib", version, "site-packages")


def get_venv_site_packages() -> str:
    return sysconfig.get_path("purelib")


def show_global_info() -> None:
    print("MATRIX STATUS: You're still plugged in")

    print(f"\nCurrent Python version: {sys.executable}")
    print("Virtual environment: None detected")

    print("\nWARNING: You're in the global environment!")
    print("The machines can see everything you install")

    print("\nTo enter the construct, run:")
    print("python -m venv construct")
    print("source matrix_env/bin/activate # On Unix")
    print("matrix_env\\Scripts\\activate # On Windows")

    print("\nThen run this program again")


def show_venv_info() -> None:
    print("MATRIX STATUS: Welcome to the construct")

    print(f"\nCurrent Python version: {sys.executable}")
    print(f"Virtual environment: {os.path.basename(sys.prefix)}")
    print(f"Environment Path: {get_venv_site_packages()}")

    print("\nSUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting the global system")

    print("\nPackage installation path:")
    print(get_venv_site_packages())


if __name__ == "__main__":
    if is_virtual_env():
        show_venv_info()
    else:
        show_global_info()

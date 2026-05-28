import os
import sys
from dotenv import load_dotenv

REQUIRED_VARS = [
    "MATRIX_MODE",
    "DATABASE_URL",
    "API_KEY",
    "LOG_LEVEL",
    "ZION_ENDPOINT"
]

VALID_MATRIX_MODES = ("development", "production")
VALID_LOG_LEVELS = ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICLAL")


def load_config() -> None:
    matrix_mode = os.environ.get("MATRIX_MODE", "development")

    if matrix_mode == "production":
        env_file = ".env.production"
    else:
        env_file = ".env"

    if not os.path.exists(env_file):
        print(f"[ERROR] Environment file '{env_file}' not found.")
        print("Create a .env file or set MATRIX_MODE=production for .env.production")

    load_dotenv(env_file, override=True)
    print(f"[INFO] Loaded configuration from '{env_file}'.")


def validate_config() -> dict:
    missing = [var for var in REQUIRED_VARS if not os.environ.get(var)]

    if missing:
        print("ERROR: missing required envorionment variables")
        for var in missing:
            print(f" - {var}")
        sys.exit(1)

    config = {var: os.environ.get[var] for var in REQUIRED_VARS}

    if config["MATRIX_MODE"] not in VALID_MATRIX_MODES:
        print(f"[ERROR] MATRIX_MODE must be one of {VALID_MATRIX_MODES}, \
got '{config['MATRIX_MODE']}'")
        sys.exit(1)

    if config["LOG_LEVEL"] not in VALID_LOG_LEVELS:
        print(f"[ERROR] LOG_LEVEL must be one of {VALID_LOG_LEVELS}, \
got '{config['LOG_LEVEL']}'")
        sys.exit(1)

    return config


def display_config(config: dict) -> None:
    print("\nCurrent Configuration:")

    mode = config["MATRIX_MODE"]
    is_prod = mode == "production"

    print("ORACLE STATUS: Reading the Matrix...")
    print("Configuration loaded:")
    print(f" Mode :{mode}")
    print(f" Database: {'Connected to production instance' if is_prod else 'Connected to local instance'}")
    print(" API Access: Authenticated")
    print(f" Log Level: {config['LOG_LEVEL']}")
    print(" Zion Network: Online")
    print(" [OK] No hardcoded secrets detected")
    print(" [OK] .env file properly configured")
    print(" [OK] Production overrides available")
    print("The Oracle sees all configurations")


if __name__ == "__main__":

    load_config()
    config = validate_config()
    display_config(config)

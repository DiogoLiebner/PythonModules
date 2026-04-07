import random


def gen_player_achievements() -> None:
    achievements = [
        "Crafting Genius",
        "Strategist",
        "World Saviour",
        "Speed Runner",
        "Survivor",
        "Master Explorer",
        "Treasure Hunter",
        "Unstoppable",
        "First Steps",
        "Collector Supreme",
        "Untouchable",
        "Sharp Mind",
        "Boss Slayer",
    ]

    alice = random.sample(achievements, random.randint(1, len(achievements)))
    bob = random.sample(achievements, random.randint(1, len(achievements)))
    charlie = random.sample(achievements, random.randint(1, len(achievements)))
    dylan = random.sample(achievements, random.randint(1, len(achievements)))

    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}\n")

    distinct = set(alice + bob + charlie + dylan)
    print(f"All distinct achievements: {distinct}\n")

    common = set.intersection(set(alice), set(bob), set(charlie), set(dylan))
    print(f"Common achievements: {common}\n")

    alice_missing = set(set(achievements) - set(alice))
    bob_missing = set(set(achievements) - set(bob))
    charlie_missing = set(set(achievements) - set(charlie))
    dylan_missing = set(set(achievements) - set(dylan))

    print(f"Alice is missing : {alice_missing}\n")

    print(f"Bob is missing : {bob_missing}\n")

    print(f"Charlie is missing : {charlie_missing}\n")

    print(f"Dylan is missing : {dylan_missing}\n")


def main() -> None:
    print("=== Achievement Tracker System ===\n")
    gen_player_achievements()


if __name__ == "__main__":
    main()

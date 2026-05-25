import random


def main() -> None:
    print("=== Game Data Alchemist ===\n")

    initiallist = [
        "incineroar",
        "Excadrill",
        "Tyranitar",
        "Milotic",
        "sneasler",
        "Sinistcha",
    ]
    caplist = []
    allcaplist = []
    scoredict = {}

    print(f"Initial list of Pokemon: {initiallist}")
    for e in initiallist:
        if str.capitalize(e) == e:
            caplist.append(e)

    for i in initiallist:
        allcaplist.append(str.capitalize(i))

    print(f"New list of capitalized names only: {caplist}")
    print(f"New list of all names capitalized: {allcaplist}")

    for name in allcaplist:
        scoredict[name] = random.randint(0, 252)

    print(f"Score dict: {scoredict}")
    average = sum(scoredict.values()) / len(initiallist)
    print(f"Score average: {average:.2f}")

    highscore = {}
    for name, score in scoredict.items():
        if score > average:
            highscore[name] = score

    print(f"High scores: {highscore}")


if __name__ == "__main__":
    main()

import random
# import typing


players = ["Excadrill", "Ttar", "Incin", "Sneasler", "Primarina", "Farigiraf"]
actions = ["Fake Out", "Protect", "Attack", "Switch", "use item", "Trick"]


def gen_event():
    while True:
        name = random.choice(players)
        action = random.choice(actions)
        yield (name, action)


def consume_event(action_list):
    while action_list:
        event = random.choice(action_list)
        action_list.remove(event)
        yield event


def main() -> None:
    print("=== Game Data Stream Processor ===\n")

    g = gen_event()
    for e in range(1000):
        name, action = next(g)
        print(f"Event {e}: Player {name} did action {action}")

    action_list = []
    for i in range(10):
        action_list.append(next(g))
    print(f"\nBuilt list of 10 events: {action_list}")

    for event in consume_event(action_list):
        name, action = event
        print(f"Got even from list: {event}")
        print(f"Remains in list: {action_list}")


if __name__ == "__main__":
    main()

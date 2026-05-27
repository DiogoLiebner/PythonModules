import ex2.battletournament as bt
from itertools import combinations


def battle(
            opponents: list[tuple[bt.CreatureFactory, type[bt.BattleStrategy]]]
        ) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    combatants: list[tuple[bt.Creature, bt.BattleStrategy]] = []
    for factory, strategy_cls in opponents:
        creature = factory.create_base()
        strategy = strategy_cls(creature)
        combatants.append((creature, strategy))

    for (creat_a, strat_a), (creat_b, strat_b) in combinations(combatants, 2):
        print("\n* Battle *")
        print(creat_a.describe())
        print("vs.")
        print(creat_b.describe())
        print("now fight!")
        try:
            strat_a.act()
            strat_b.act()
        except bt.InvalidStrategyError as e:
            print(f"Battle error, aborting tournament: {e}")
            return


def main() -> None:
    print("Tournament 0(basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    battle([
        (bt.FlameFactory(), bt.NormalStrategy),
        (bt.GrassFactory(), bt.DefensiveStrategy),
    ])

    print()
    print("Tournament 1(error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    battle([
        (bt.FlameFactory(), bt.AggressiveStrategy),
        (bt.GrassFactory(), bt.DefensiveStrategy),
    ])

    print()
    print("Tournament 2(multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive)], (Transform+Aggressive) ]")
    battle([
        (bt.AquaFactory(), bt.NormalStrategy),
        (bt.GrassFactory(), bt.DefensiveStrategy),
        (bt.TransformCreatureFactory(), bt.AggressiveStrategy),
    ])


if __name__ == "__main__":
    main()

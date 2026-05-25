import sys


def main() -> None:
    print("=== Player Score Analytics ===\n")
    if len(sys.argv) == 1:
        print("No scores provided. Usage: python3 \
ft_score_analytics.py <score1> <score2> ...")
        return

    scores = []
    invalid = []

    for arg in sys.argv[1:]:
        try:
            scores.append(int(arg))
        except (ValueError):
            invalid.append(arg)
            print(f"Invalid parameter: '{arg}'")

    if not scores:
        print("No scores provided. Usage: python3 \
ft_score_analytics.py <score1> <score2> ...")
        return

    print(f"Total players: {len(scores)}")
    print(f"Total score: {sum(scores)}")
    print(f"Average score: {(sum(scores)/len(scores)):.1f}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")


if __name__ == "__main__":
    main()

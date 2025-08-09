import argparse
import time


def countdown(seconds: int) -> None:
    """Count down from the given number of seconds."""
    for remaining in range(seconds, 0, -1):
        print(f"{remaining}...")
        time.sleep(1)
    print("Time's up!")


def main() -> None:
    parser = argparse.ArgumentParser(description="Simple command-line timer.")
    parser.add_argument("seconds", type=int, help="Number of seconds to count down.")
    args = parser.parse_args()
    countdown(args.seconds)


if __name__ == "__main__":
    main()

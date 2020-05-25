from datetime import datetime
from pathlib import Path


def main():
    with Path(__file__).resolve().parent.joinpath('demo.txt').open("w") as fh:
        fh.write(f'Hello world! It\'s {datetime.now()}!')


if __name__ == "__main__":
    main()

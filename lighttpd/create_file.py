#!/usr/bin/python3

import os

SIZE = 1000000 * 600

def main():
    with open("file", "w+b") as f:
        count = 1
        while True:
            f.write(str.encode(f"Line {count}\n"))
            if (count % 10) == 0:
                f.flush()
                stats = os.stat("file")
                if stats.st_size >= SIZE:
                    break
            count += 1


if __name__ == "__main__":
    main()

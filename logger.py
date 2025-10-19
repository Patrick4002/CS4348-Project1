#!/usr/bin/env python3
import sys
from datetime import datetime

def main():
    if len(sys.argv) != 2:
        print("Usage: logger.py <logfile>")
        sys.exit(1)

    log_filename = sys.argv[1]

    with open(log_filename, "a") as log:
        while True:
            line = sys.stdin.readline().rstrip()
            if not line:
                continue
            if line == "QUIT":
                break

            parts = line.split(maxsplit=1)
            action = parts[0]
            message = parts[1] if len(parts) > 1 else ""
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
            log.write(f"{timestamp} [{action}] {message}\n")
            log.flush()

if __name__ == "__main__":
    main()
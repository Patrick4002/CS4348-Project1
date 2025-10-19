import sys
import subprocess

def ask_history_or_new(history):
    """Ask user to use history or a new string."""
    if history:
        print("\nHistory:")
        for i, val in enumerate(history, 1):
            print(f"{i}. {val}")
        sel = input("Select number or 0 for new: ").strip()
        if sel.isdigit() and 1 <= int(sel) <= len(history):
            return history[int(sel)-1].upper()
    return input("Enter new string: ").strip().upper()

def main():
    if len(sys.argv) != 2:
        print("Usage: driver.py <logfile>")
        sys.exit(1)

    logfile = sys.argv[1]
    logger = subprocess.Popen([sys.executable, "logger.py", logfile], stdin=subprocess.PIPE, text=True)
    encryptor = subprocess.Popen([sys.executable, "encryption.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)

    history = []
    logger.stdin.write("START Driver started.\n")
    logger.stdin.flush()

    while True:
        print("\nCommands: password, encrypt, decrypt, history, quit")
        cmd = input("> ").strip().lower()

        if cmd == "password":
            pwd = input("Enter new password: ").strip().upper()
            if not pwd.isalpha():
                print("Error: Password must contain only letters.")
                continue
            encryptor.stdin.write(f"PASS {pwd}\n")
            encryptor.stdin.flush()
            resp = encryptor.stdout.readline().strip()
            print(resp)
            logger.stdin.write(f"{resp}\n")
            logger.stdin.flush()

        elif cmd == "encrypt":
            text = ask_history_or_new(history)
            if not text.isalpha():
                print("Error: Input must contain only letters.")
                continue
            encryptor.stdin.write(f"ENCRYPT {text}\n")
            encryptor.stdin.flush()
            resp = encryptor.stdout.readline().strip()
            print(resp)
            logger.stdin.write(f"{resp}\n")
            logger.stdin.flush()
            if resp.startswith("RESULT "):
                history.append(resp.split(" ", 1)[1])

        elif cmd == "decrypt":
            text = ask_history_or_new(history)
            if not text.isalpha():
                print("Error: Input must contain only letters.")
                continue
            encryptor.stdin.write(f"DECRYPT {text}\n")
            encryptor.stdin.flush()
            resp = encryptor.stdout.readline().strip()
            print(resp)
            logger.stdin.write(f"{resp}\n")
            logger.stdin.flush()
            if resp.startswith("RESULT "):
                history.append(resp.split(" ", 1)[1])

        elif cmd == "history":
            if not history:
                print("(No history yet)")
            else:
                for i, val in enumerate(history, 1):
                    print(f"{i}. {val}")

        elif cmd == "quit":
            encryptor.stdin.write("QUIT\n")
            encryptor.stdin.flush()
            logger.stdin.write("QUIT\n")
            logger.stdin.flush()
            print("Exiting...")
            break

        else:
            print("Unknown command.")

    encryptor.wait()
    logger.wait()

if __name__ == "__main__":
    main()
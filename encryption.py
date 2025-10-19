import sys

def vigenere_encrypt(text, key):
    result = []
    key = key.upper()
    text = text.upper()
    for i, c in enumerate(text):
        if not c.isalpha():
            return None
        shift = ord(key[i % len(key)]) - ord('A')
        result.append(chr(((ord(c) - ord('A') + shift) % 26) + ord('A')))
    return ''.join(result)

def vigenere_decrypt(text, key):
    result = []
    key = key.upper()
    text = text.upper()
    for i, c in enumerate(text):
        if not c.isalpha():
            return None
        shift = ord(key[i % len(key)]) - ord('A')
        result.append(chr(((ord(c) - ord('A') - shift) % 26) + ord('A')))
    return ''.join(result)

def main():
    current_key = None
    while True:
        line = sys.stdin.readline().strip()
        if not line:
            continue
        parts = line.split(maxsplit=1)
        cmd = parts[0].upper()
        arg = parts[1].strip() if len(parts) > 1 else ""

        if cmd == "QUIT":
            break
        elif cmd == "PASS":
            if not arg.isalpha():
                print("ERROR Passkey must contain only letters.", flush=True)
            else:
                current_key = arg.upper()
                print("RESULT", flush=True)
        elif cmd == "ENCRYPT":
            if current_key is None:
                print("ERROR Password not set", flush=True)
            elif not arg.isalpha():
                print("ERROR Input must only contain letters", flush=True)
            else:
                encrypted = vigenere_encrypt(arg, current_key)
                print(f"RESULT {encrypted}", flush=True)
        elif cmd == "DECRYPT":
            if current_key is None:
                print("ERROR Password not set", flush=True)
            elif not arg.isalpha():
                print("ERROR Input must only contain letters", flush=True)
            else:
                decrypted = vigenere_decrypt(arg, current_key)
                print(f"RESULT {decrypted}", flush=True)
        else:
            print("ERROR Unknown command", flush=True)

if __name__ == "__main__":
    main()
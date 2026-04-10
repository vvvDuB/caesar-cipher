def encrypt(text: str, key: int) -> str:
    shift = key % 26
    result = []

    for c in text:
        if ("A" <= c <= "Z") or ("a" <= c <= "z"):
            base = ord("A") if c.isupper() else ord("a")
            shifted = (ord(c) - base + shift) % 26
            result.append(chr(base + shifted))
        else:
            result.append(c)

    return "".join(result)

def main()-> None:
    choise = 0 if input("Vuoi cifrare o decifrare? [c/d]: ") == 'c' else 1 
    text = input("Dammi una frase: ")
    key = int(input("Dammi una chiave: "))

    if choise:
        key *= -1

    result = encrypt(text, key)
    print(result)

if __name__ == "__main__":
    main()

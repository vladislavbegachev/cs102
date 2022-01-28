def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    ciphertext = ""
    for i in plaintext:
        if i.isalpha():
            if i.islower():
                ciphertext += chr((ord(i) + shift - ord("a")) % 26 + ord("a"))
            else:
                ciphertext += chr((ord(i) + shift - ord("A")) % 26 + ord("A"))
        else:
            ciphertext += i
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    plaintext = ""
    for i in ciphertext:
        if i.isalpha():
            if i.islower():
                plaintext += chr((ord(i) - shift - ord("a")) % 26 + ord("a"))
            else:
                plaintext += chr((ord(i) - shift - ord("A")) % 26 + ord("A"))
        else:
            plaintext += i
    return plaintext

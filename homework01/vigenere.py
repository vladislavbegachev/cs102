def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    ciphertext = ""
    keyword = keyword.upper()
    for i, letter in enumerate(plaintext):
        if letter.isalpha():
            shift = ord(keyword[i % len(keyword)]) - ord("A")
            if letter.islower():
                ciphertext += chr((ord(letter) + shift - ord("a")) % 26 + ord("a"))
            else:
                ciphertext += chr((ord(letter) + shift - ord("A")) % 26 + ord("A"))
        else:
            ciphertext += letter
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    plaintext = ""
    keyword = keyword.upper()
    for i, letter in enumerate(ciphertext):
        if letter.isalpha():
            shift = ord(keyword[i % len(keyword)]) - ord("A")
            if letter.islower():
                plaintext += chr((ord(letter) - shift - ord("a")) % 26 + ord("a"))
            else:
                plaintext += chr((ord(letter) - shift - ord("A")) % 26 + ord("A"))
        else:
            plaintext += letter

    return plaintext

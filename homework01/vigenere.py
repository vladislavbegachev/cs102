def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    ciphertext_list = []
    plain = []
    plain_nums = []
    code = []
    code_nums = []
    capital_indicator = []


    for letter in plaintext:
        plain.append(letter)

    for coding_letter in keyword:
        code.append(coding_letter)

    for letter in plain:
        index = ord(letter) - 97
        if index > -1:
            plain_nums.append(index)
            capital_indicator.append(0)
        else:
            index += 32
            plain_nums.append(index)
            capital_indicator.append(-32)
    for letter in code:
        index = ord(letter) - 97
        if index > -1:
            code_nums.append(index)
        else:
            index += 32
            code_nums.append(index)

    i  =  0
    while i < len(plain_nums):
        for index in plain_nums:
            if plain_nums[i] + code_nums[i] <= 25:
                plain_nums[i] += code_nums[i]
            else:
               plain_nums[i] += code_nums[i] - 1 - 25
            code_nums.append(code_nums[i])
            plain_nums[i] += capital_indicator[i]
            i += 1

    i = 0
    for index in plain_nums:
        ciphertext_list.append(chr(plain_nums[i] + 97))
        i += 1
    
    ciphertext = "".join(map(str, ciphertext_list))

    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    ciphertext_list = []
    plain = []
    plain_nums = []
    code = []
    code_nums = []
    capital_indicator = []


    for letter in ciphertext:
        plain.append(letter)

    for coding_letter in keyword:
        code.append(coding_letter)

    for letter in plain:
        index = ord(letter) - 97
        if index > -1:
            plain_nums.append(index)
            capital_indicator.append(0)
        else:
            index += 32
            plain_nums.append(index)
            capital_indicator.append(-32)

    for letter in code:
        index = ord(letter) - 97
        if index > -1:
            code_nums.append(index)
        else:
            index += 32
            code_nums.append(index)

    i = 0

    while i < len(plain_nums):
        for index in plain_nums:
            if plain_nums[i] - code_nums[i] >= 0:
                plain_nums[i] -= code_nums[i]
            else:
               plain_nums[i] -= code_nums[i] - 1 - 25
            code_nums.append(code_nums[i])
            plain_nums[i] += capital_indicator[i]
            i += 1

    i = 0
    for index in plain_nums:
        ciphertext_list.append(chr(plain_nums[i] + 97))
        i += 1
    
    plaintext = "".join(map(str, ciphertext_list))
    
    return plaintext

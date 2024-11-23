def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    for i in plaintext:
        time = ord(i)
        if 65 <= time <= 90:
            c = ((time - 65) + shift) % 26 + 65
            ciphertext += chr(c)
        elif 97 <= time <= 122:
            c = ((time - 97) + shift) % 26 + 97
            ciphertext += chr(c)
        else:
            ciphertext +=i


    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    for i in ciphertext:
        time = ord(i)
        if 65 <= time <= 90:
            c = ((time - 65) - shift) % 26 + 65
            plaintext += chr(c)
        elif 97 <= time <= 122:
            c = ((time - 97) - shift) % 26 + 97
            plaintext += chr(c)
        else:
            plaintext += i

    return plaintext

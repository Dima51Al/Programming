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
    for i in range(len(plaintext)):

        time = ord(plaintext[i])
        if 65 <= time <= 90:
            shift = ord(keyword[i % len(keyword)]) -65
            c = ((time - 65) + shift) % 26 + 65
            ciphertext += chr(c)
        elif 97 <= time <= 122:
            shift = ord(keyword[i % len(keyword)]) - 97
            c = ((time - 97) + shift) % 26 + 97
            ciphertext += chr(c)
        else:
            ciphertext += i

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
    plaintext = ""
    # PUT YOUR CODE HERE
    return plaintext
import typing as tp


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
    
    import string
    ciphertext = ""

    up = str(string.ascii_uppercase * 2)
    low = str(string.ascii_lowercase * 2)
    for i in plaintext:
        if i in string.ascii_letters:
            if i.isupper():
                ciphertext += up[up.index(i)+shift]
            elif i.islower():
                ciphertext += low[low.index(i)+shift]
        else:
            ciphertext += i
    return ciphertext
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
    import string
    plaintext = ""

    up = str(string.ascii_uppercase * 2)
    low = str(string.ascii_lowercase * 2)
    for i in ciphertext:
        if i in string.ascii_letters:
            if i.isupper():
                plaintext += up[up.index(i)-shift]
            elif i.islower():
                plaintext += low[low.index(i)-shift]
        else:
            plaintext += i
    return plaintext

    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    # PUT YOUR CODE HERE
    return best_shift

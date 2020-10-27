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
    import string
    up = str(string.ascii_uppercase * 2)
    low = str(string.ascii_lowercase * 2)
    key = keyword
    
    if (len(keyword) < len(plaintext)):
        while (len(key) < len(plaintext)):
            key += keyword
    
    for i in range(len(plaintext)):    
        key = key.upper()
        shift = (string.ascii_uppercase).index(key[i])
        
        if plaintext[i].isupper():
            ciphertext += up[up.index(plaintext[i])+shift]
        elif plaintext[i].islower():
            ciphertext += low[low.index(plaintext[i])+shift]
        else:
        	ciphertext += plaintext[i]
    
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
    import string
    up = str(string.ascii_uppercase * 2)
    low = str(string.ascii_lowercase * 2)
    key = keyword
    
    if (len(keyword) < len(ciphertext)):     #нахожу расширенный ключ, если такой нужен
        while (len(key) < len(ciphertext)): 
            key += keyword
    
    for i in range(len(ciphertext)): 
        key = key.upper()
        shift = (string.ascii_uppercase).index(key[i]) #нахожу сдвиг, чтобы использовать
                                                       #код из предыдущего задания
        if ciphertext[i].isupper():
            plaintext += up[up.index(ciphertext[i])-shift]#использую свой код из Цезаря
        elif ciphertext[i].islower():
            plaintext += low[low.index(ciphertext[i])-shift]
        else:
        	plaintext += ciphertext[i]
    
    return plaintext

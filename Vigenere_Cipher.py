def generateKey(string, key):
    key = list(key)
    if len(string) == len(key):
        return(key)
    else:
        for i in range(len(string) -
                       len(key)):
            key.append(key[i % len(key)])
    return("" . join(key))


def vigenere_encrypt(string, key):
    cipher_text = []
    for i in range(len(string)):
        x = (ord(string[i]) +
             ord(key[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x))
    return("" . join(cipher_text))


def vigenere_decrypt(cipher_text, key):
    orig_text = []
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i]) -
             ord(key[i]) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
    return("" . join(orig_text))


if __name__ == "__main__":
    text = str(input('Kindly input the text to encrypt: '))
    keyword = str(input('Kindly input the text encryption keyword: '))

    key = generateKey(text, keyword)
    cipher_text = vigenere_encrypt(text, key)

    print("\nEncrypted text: ", cipher_text)
    print("Original/Decrypted Text :",
          vigenere_decrypt(cipher_text, key))

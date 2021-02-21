def caesar_cipher_encrypt(text, s):
    result = ''
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
        else:
            result += chr((ord(char) + s-97) % 26 + 97)

    return result


def caesar_cipher_decrypt(text, s):
    result = ''

    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((ord(char) - s-65) % 26 + 65)
        else:
            result += chr((ord(char) - s-97) % 26 + 97)

    return result


text = str(input('Kindly input the text: '))
s = int(input('Kindly indicate text shift pattern (positive int): '))

print(
    f'\n\nRESULT\nInitial text: {text}\nText shift pattern: {s}\nCaesar cipher: {caesar_cipher_encrypt(text, s)}')

print(
    f'\nDecrypted text: {caesar_cipher_decrypt(caesar_cipher_encrypt(text, s), s)}')

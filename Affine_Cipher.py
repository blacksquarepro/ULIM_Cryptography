def egcd(a, b):
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b//a, b % a
        m, n = x-u*q, y-v*q
        b, a, x, y, u, v = a, r, u, v, m, n
    gcd = b
    return gcd, x, y


def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None
    else:
        return x % m


def encrypt(text, key):
    return ''.join([chr(((key[0]*(ord(t) - ord('A')) + key[1]) % 26) + ord('A')) for t in text.upper().replace(' ', '')])


def decrypt(cipher, key):
    return ''.join([chr(((modinv(key[0], 26)*(ord(c) - ord('A') - key[1])) % 26) + ord('A')) for c in cipher])


text = str(input('Kindly input the text to encrypt: '))
multiply_key = int(
    input('Kindly define the multiply cipher key A (positive integer): '))
add_key = int(input('Kindly define the add cipher key B (positive integer): '))

key = [multiply_key, add_key]
enc_text = encrypt(text, key)

print(f'Encrypted Text: {enc_text}')
print(f'Decrypted Text: {decrypt(enc_text, key)}')

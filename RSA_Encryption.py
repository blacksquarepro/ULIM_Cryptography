import rsa # pip install rsa

message = bytearray(input('Provide your text for RSA encryption: '), 'utf-8')
public_key, private_key = rsa.newkeys(1024)

encrypted_message = rsa.encrypt(message, public_key)
decrypted_message = rsa.decrypt(encrypted_message, private_key)

print(f'Encrypted message: {encrypted_message}\n Decrypted message: {decrypted_message}')
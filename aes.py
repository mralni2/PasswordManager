from Crypto.Cipher import AES

main_key = b'R&9Ic{_8G3j:bkt2'


def start_encrypt_file(file, key):
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    file_open = open(file, 'rb')
    data = file_open.read()
    ciphertext = cipher.encrypt(data)
    file_open = open(file, 'wb')
    [file_open.write(x) for x in (nonce, ciphertext)]
    file_open.close()
    return 0


def start_decrypt_file(file, key):
    file_open = open(file, 'rb')
    nonce, ciphertext = [file_open.read(x) for x in (16, -1)]
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    file_open = open(file, 'wb')
    file_open.write(plaintext)
    file_open.close()
    return 0

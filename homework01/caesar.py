def encrypt_caesar(plaintext, shift):
    import string
    alf = string.ascii_letters
    ciphertext = ''
    for i in plaintext:
        if i in alf:
            ciphertext += alf[alf.find(i) + shift % 26]
        else:
            ciphertext += i
    return ciphertext


def decrypt_caesar(plaintext, shift):
    import string
    alf = string.ascii_letters
    ciphertext = ''
    for i in plaintext:
        if i in alf:
            ciphertext += alf[alf.rfind(i) - shift % 26]
        else:
            ciphertext += i
    return ciphertext

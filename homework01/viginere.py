def encrypt_vigenere(plaintext, keyword):
    keyword *= (len(plaintext) // len(keyword) + 1)
    keyword = keyword.upper()
    sum = ''
    s = ''
    s2 = ''
    for i in range(len(plaintext)):
        if plaintext[i].islower():
            s += '1'
            s2 += plaintext[i].upper()
        else:
            s += '0'
            s2 += plaintext[i]
    sum = ''
    for i, j in enumerate(s2):
        qwer = (ord(j) + ord(keyword[i]))
        sum += chr(qwer % 26 + 65)
    s1 = ''
    for i in range(len(sum)):
        if s[i] == '1':
            s1 += sum[i].lower()
        else:
            s1 += sum[i]
    return s1


def decrypt_vigenere(plaintext, keyword):
    keyword *= (len(plaintext) // len(keyword) + 1)
    keyword = keyword.upper()
    sum = ''
    s = ''
    s2 = ''
    for i in range(len(plaintext)):
        if plaintext[i].islower():
            s += '1'
            s2 += plaintext[i].upper()
        else:
            s += '0'
            s2 += plaintext[i]
    sum = ''
    for i, j in enumerate(s2):
        qwer = (ord(j) - ord(keyword[i]))
        sum += chr(qwer % 26 + 65)
    s1 = ''
    for i in range(len(sum)):
        if s[i] == '1':
            s1 += sum[i].lower()
        else:
            s1 += sum[i]
    return s1

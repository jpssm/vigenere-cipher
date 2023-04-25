import re

def shift(key_l, msg_l):
    ord_value = (ord(key_l) + ord(msg_l) - 2 * ord('a')) % 26 + ord('a')
    return chr(ord_value)

def unshift(key_l, msg_l):
    ord_value = (ord(msg_l) - ord(key_l)) % 26 + ord('a')
    return chr(ord_value)

def to_lower_case(str):
    pattern = re.compile('[\W_]+')
    str = pattern.sub(' ', str).lower()
    return str

def match_key(key, msg):
    msg_letters = sum(l.isalpha() for l in msg)
    length = msg_letters
    key = (key * (length // len(key) + 1)) [:length]
    return key

def encrypt(key, msg):
    key_l = list(key)
    msg_l = list(msg)
    j = 0
    k = 0
    for i in key_l:
        if msg_l[j].isalpha():
            msg_l[j] = shift(key_l[k], msg_l[j])
            k = k + 1
        j = j + 1
    return "".join(msg_l)

def decrypt(key, msg):
    key_l = list(key)
    msg_l = list(msg)
    j = 0
    k = 0
    for i in key_l:
        if msg_l[j].isalpha():
            msg_l[j] = unshift(key_l[k], msg_l[j])
            k = k + 1
        j = j + 1
    return "".join(msg_l)


if __name__ == "__main__":
    key = (to_lower_case(input('Enter key: ')))
    msg  = (to_lower_case(input('Enter message: ')))

    key = match_key(key, msg)

    encrypted = encrypt(key, msg)

    print(encrypted)
    print(decrypt(key, encrypted))

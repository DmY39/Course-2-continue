
from simplecrypt import decrypt
a = []
with open("C:\\Users\\Дмитрий\\Downloads\\encrypted (1).bin", "rb") as inp:
    encrypted = inp.read()
    print(encrypted)
with open("C:\\Users\\Дмитрий\\Downloads\\passwords.txt", "r") as pas:
    for line in pas:
        line = line.strip()
        try:
            text = decrypt(line, encrypted).decode('utf8')
            print(text)
        except:
            print('Error')


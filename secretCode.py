def make_code(p):
    s = ""
    for k in p:
        s += k.upper()
    lst = ""
    for i in range(len(s)):
        if s[i] == chr(0):
            lst += chr(81)
            continue
        elif ord(s[i]) >= 64 and ord(s[i]) <= 72:
            lst += chr((ord(s[i]))+25)
            continue
        elif ord(s[i]) >= 73 and ord(s[i]) <= 80:
            lst += chr((ord(s[i]))+2)
            continue
        elif ord(s[i]) >= 81 and ord(s[i]) <= 91:
            lst += chr((ord(s[i]))+19)
            continue
        elif ord(s[i]) == 123:
            lst += chr(122)
            continue
        elif ord(s[i]) == 124:
            lst += chr(120)
            continue
        elif ord(s[i]) == 125:
            lst += chr(121)
            continue
    print(lst)

def decode(s):
    sf = ""
    for i in range(len(s)):
        if s[i] == chr(81):
            sf += chr(0)
            continue
        elif ord(s[i]) > 89 and ord(s[i]) <= 97:
            sf += chr((ord(s[i]))-25)
            continue
        elif ord(s[i]) >= 72 and ord(s[i]) <= 82:
            sf += chr((ord(s[i]))-2)
            continue
        elif ord(s[i]) >= 98 and ord(s[i]) <= 110:
            sf += chr((ord(s[i]))-19)
            continue
        elif ord(s[i]) == 122:
            sf += chr(123)
            continue
        elif ord(s[i]) == 120:
            sf += chr(124)
            continue
        elif ord(s[i]) == 121:
            sf += chr(125)
            continue
    print(sf)

make_code("Hey, I am Mishuk Sarker")
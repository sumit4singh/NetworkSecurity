def encrypt(plaintext, key):
    rows = len(key)
    lst = list(plaintext)
    matrix = []
    row = []
    diff = (rows* rows) - len(lst)
    while diff > 0:
        lst.append('%')
        diff  = diff - 1
    for i in range(0, rows*rows):
        if lst[i] == ' ':
            lst[i] = '%'
        if i > 0 and i % rows == 0:
            matrix.append(row)
            row = []
        row.append(lst[i])
    matrix.append(row)
    cypher = []
    i = 0
    for k in key:
        for i in range(0,5):
            cypher.append(matrix[i][k-1])
    return cypher


def decrypt(cypher, key):
    rows = len(key)
    data = [[0 for _ in range(rows)] for _ in range(rows)]
    plain = []
    a = []
    i = 0
    
    for i in range(0, len(cypher)):
        if i > 0 and i % rows == 0:
            plain.append(a)
            a = []
        a.append(cypher[i])
    plain.append(a)
    # print(plain)
    for i in range(0, rows):
        rowdata = plain[i]
        k = key[i]
        for r,i in zip(rowdata, range(0, rows)):
            data[i][k-1] = r
    plaindata = ""
    for row in data:
        for a in row:
            if a == '%':
                plaindata += " "
            else:
                plaindata += a
    # print(plaindata)
    return plaindata


if __name__ == '__main__':
    while True:
        print(''' Welcome to matrix transformation
        Pick one of the operations
        1. encryption
        2. decryption
        3. anything else to exit''')
        value = input()
        if value =='1':
            print('enter plain text')
            plaintext = input()
            print('enter key with space seperation')
            key = input()
            keys = key.split(' ')
            key = []
            for k in keys:
                key.append(int(k))
            cypher = encrypt(plaintext ,key)
            print('Generated cypher is')
            print(cypher)
        elif value == '2':
            print('enter cypher text')
            cypher = input()
            print('enter key with space seperation')
            key = input()
            keys = key.split(' ')
            key = []
            for k in keys:
                key.append(int(k))
            plain = decrypt(cypher ,key)
            print('Generated plain text is')
            print(plain)
        else: 
            exit()
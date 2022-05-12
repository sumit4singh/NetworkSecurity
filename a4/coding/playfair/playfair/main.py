def secret_key(name):
    name = name.upper()
    matrix = [[0 for x in range(5)] for y in range(5)]
    alpha = [0 for x in range(26)]
    key_word = []
    for a in name:
        if alpha[ord(a) - 65] == 0:
            key_word.append(a)
            if ord(a) == 73 or ord(a) == 74:
                alpha[73 - 65] = 1
                alpha[74 - 65] = 1
                key_word.pop()
                key_word.append('I')
            else:
                alpha[ord(a) - 65] = 1
    for x in range(26):
        if alpha[x] == 0:
            key_word.append(chr(x + 65))
            if x == 8 or x == 9:
                alpha[8] = 1
                alpha[9] = 1
            else:
                alpha[ord(a) - 65] = 1
    for i in range(5):
        for j in range(5):
            if len(key_word) != 0:
                matrix[i][j] = key_word.pop(0)
    return matrix


def encrypt(text, key):
    key_matrix = secret_key(key)
    lst = to_list(text.upper())
    position = find_position(lst, key_matrix)
    pairs = pairing(lst)
    transform = encryption(pairs, position, key_matrix)
    return transform


def decrypt(text, key):
    key_matrix = secret_key(key)
    lst = to_list(text.upper())
    position = find_position(lst, key_matrix)
    pairs = pairing(lst)
    transform = decryption(pairs, position, key_matrix)
    return transform


def encryption(pairs, position, keymatrix):
    cypher = []
    transformedlist = []
    for pair in pairs:
        transform_one = []
        transform_two = []
        locate_one = position.get(pair[0])
        locate_two = position.get(pair[1])
        if locate_one[0] == locate_two[0]:
            transform_one.append(locate_one[0])
            if locate_one[1]+1 > 4:
                transform_one.append(0)
            else:
                transform_one.append((locate_one[1] + 1))
            transform_two.append(locate_two[0])
            if locate_two[1]+1 > 4:
                transform_two.append(0)
            else:
                transform_two.append((locate_two[1] + 1))
        elif locate_one[1] == locate_two[1]:
            if locate_one[0]+1 > 4:
                transform_one.append(0)
            else:
                transform_one.append((locate_one[0] + 1))
            transform_one.append(locate_one[1])
            if locate_two[0]+1 > 4:
                transform_two.append(0)
            else:
                transform_two.append((locate_two[0] + 1))
            transform_two.append(locate_two[1])
        else:
            transform_one.append(locate_one[0])
            transform_two.append(locate_two[0])
            transform_one.append(locate_two[1])
            transform_two.append(locate_one[1])
        cypher.append(transform_one)
        cypher.append(transform_two)
    for x in cypher:
        value = keymatrix[x[0]][x[1]]
        transformedlist.append(value)
    return transformedlist


def decryption(pairs, position, keymatrix):
    cypher = []
    transformedlist = []
    for pair in pairs:
        transform_one = []
        transform_two = []
        locate_one = position.get(pair[0])
        locate_two = position.get(pair[1])
        if locate_one[0] == locate_two[0]:
            transform_one.append(locate_one[0])
            if locate_one[1] - 1 > 4:
                transform_one.append(0)
            else:
                transform_one.append((locate_one[1] - 1))
            transform_two.append(locate_two[0])
            if locate_two[1] - 1 > 4:
                transform_one.append(0)
            else:
                transform_two.append((locate_two[1] - 1))
        elif locate_one[1] == locate_two[1]:
            if locate_one[0] - 1 > 4:
                transform_one.append(0)
            else:
                transform_one.append((locate_one[0] - 1))
            transform_one.append(locate_one[1])
            if locate_two[0] - 1 > 4:
                transform_two.append(0)
            else:
                transform_two.append((locate_two[0] - 1))
            transform_two.append(locate_two[1])
        else:
            transform_one.append(locate_one[0])
            transform_two.append(locate_two[0])
            transform_one.append(locate_two[1])
            transform_two.append(locate_one[1])
        cypher.append(transform_one)
        cypher.append(transform_two)
    for x in cypher:
        value = keymatrix[x[0]][x[1]]
        transformedlist.append(value)
    return transformedlist


def find_position(lst, key_matrix):
    position = {}
    for i in range(0, 5):
        for j in range(0, 5):
            loc = []
            loc.append(i)
            loc.append(j)
            position[key_matrix[i][j]] = loc
    return position


def pairing(lst):
    pair = []
    i = 0
    while i <= (len(lst)-1):
        couple = []
        couple.append(lst[i])
        if i == len(lst)-1:
            lst.append('Z')
        if lst[i] == lst[i+1]:
            couple.append('Q')
            i -= 1
        elif lst[i] == 'I' and lst[i+1] == 'J':
            couple.append('Q')
        else:
            couple.append(lst[i+1])
        pair.append(couple)
        i += 2
    return pair


def to_list(text):
    lst = list(text)
    i = 0
    special = []
    # lst.pop(0)
    for a in lst:
        if ord(a) not in range(65, 90):
            special.append(i)
        if a == 'J':
            lst[i] = 'I'
        i += 1
    l = 0
    for x in special:
        lst.pop(x - l)
        l += 1
    # if len(lst) % 2 != 0:
    #     lst.append('Z')
    return lst


if __name__ == '__main__':
    # method 1
    while True:
        print('''Chose you option from list
        1. key matrix
        2. Encryption
        3. Decryption
        4. Anything else to exit''')
        value = input()
        if value == '1':
            print('Enter key')
            key = input()
            key_matrix = secret_key(key)
            print('Generted key matrix is')
            print(key_matrix)
        elif value == '2':
            print("Enter plain text")
            plain = input()
            print('Enter key')
            key = input()
            cypher = encrypt(plain, key)
            print('Generated cypher is')
            print(cypher)
        elif value == '3':
            print("Enter cypher text")
            cypher = input()
            print('Enter key')
            key = input()
            plaintext = decrypt(cypher, key)
            print('Generated plain text is')
            print(plaintext)
        else:
            exit()
    # key_matrix = secret_key('playfire')
    # print(key_matrix)
    # # method 2
    # cypher = encrypt('''
    # come quickly we need help''', 'security')
    # print(cypher)
    # plaintext = decrypt('''
    # unvtxsysdpgccmsvsffuml''', 'security')
    # print(plaintext)

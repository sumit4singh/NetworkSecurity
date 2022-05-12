public_key = []
private_key = []


def rsa_algo(p, q):
    n = p*q
    x = (p-1)*(q-1)
    e = find_relative_prime(n, x)
    d = calculate_d(e, x)
    public_key.append(e)
    public_key.append(n)
    private_key.append(d)
    private_key.append(n)
    print(f'Public RSA key is ({public_key[0]}, {public_key[1]})')
    print(f'Private RSA key is ({private_key[0]}, {private_key[1]})')
    # print(e)


def calculate_d(e, x):
    # print(x, e)
    for i in range(1, 65000):
        d = ((x*i)+1) % e
        # print(((x*i)+1))
        if d == 0:
            return int(((x*i)+1)/e)
    return None


def find_relative_prime(n, x):
    x_factors = find_factor(x)
    for i in range(2, n):
        i_factor = find_factor(i)
        seta = set(x_factors)
        setb = set(i_factor)
        if seta & setb:
            continue
        else:
            return i
    return None


def find_factor(num):
    factorlist = []
    for i in range(2, num+1):
        if num % i == 0:
            factorlist.append(i)
    return factorlist


def encrypt(m):
    prod = pow(m, public_key[0])
    cypher = prod % public_key[1]
    print(f'The ciphertext c is : {cypher}')
    decrypt(cypher)


def decrypt(cypher):
    print('Decrypting c ….')
    val = cal_mod(cypher)
    print(f'The plaintext m is : {val}')


def cal_mod(cypher):
    k = private_key[0]
    n = 1
    for i in range(0, k):
        n = n*cypher
        mod = n % private_key[1]
    return mod


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Enter the prime numbers, p and q:')
    value = input()
    pq = value.split(' ')
    print('Calculating RSA values ….')
    rsa_algo(int(pq[0]), int(pq[1]))
    print('Enter the plaintext message m (an integer):')
    number = input()
    print('Encrypting m…')
    encrypt(int(number))



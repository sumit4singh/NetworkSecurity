import sys

type = 0 # 1 for standard and 2 for advanced


def standard():
    print(f'Hi, sumit singh')
    file = sys.argv[1]
    data = open(file, "r")
    a = data.read()
    lines = a.split('\n')
    forstandard(lines)


def forstandard(lines):
    status = []
    fromip = []
    maskip = []
    for line in lines:
        value = line.__contains__("access-list")
        if value != True:
            break
        split = line.split()
        if split[2] == 'permit':
            status.append(1)
        elif split[2] == 'deny':
            status.append(0)
        fromip.append(split[3])
        maskip.append(split[4])
    standardlogic(fromip, maskip, status)


def standardlogic(fromip, maskip, status):
    ip = open(sys.argv[2], 'r')
    inputip = ip.read()
    processedlist = validate(fromip, maskip, status)
    inputlist = inputip.split('\n')
    for input in inputlist:
        output = verify(processedlist, input.split('.'))
        if output == 'permit':
            print(f'Packet from {input} is permitted')
        elif output == 'deny':
            print(f'Packet from {input} is denied')


def validate(fromip, maskip, status):
    allowediplist = []
    j = 0
    for ip, mask in zip(fromip, maskip):
        allowedip = []
        iparray = ip.split('.')
        maskarray = mask.split('.')
        for i in range(0, 4):
            if maskarray[i] == '0':
                allowedip.append(iparray[i])
            else:
                allowedip.append('any')
            i += 1
        allowedip.append(status[j])
        allowediplist.append(allowedip)
        j += 1
    return (allowediplist)


def verify(processedlist, input):
    for acl in processedlist:
        ok = False
        for each, inp in zip(acl, input):
            if each == 'any':
                ok = True
            elif each == inp:
                ok = True
            else:
                ok = False
                break
        if acl[4] == 1 and ok:
            return "permit"
        elif acl[4] == 0 and ok:
            return "deny"
    return "deny"


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    standard()

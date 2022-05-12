import sys

type = 0 # 1 for standard and 2 for advanced


def acllogic():
    # Use a breakpoint in the code line below to debug your script.
    # read file and process the data first
    print(f'Hi, sumit singh')  # Press Ctrl+F8 to toggle the breakpoint.
    file = open(sys.argv[1], 'r')
    a = file.read()
#     a = """access-list 104 permit tcp 170.16.10.5 0.0.0.0 170.16.70.0 0.0.0.255 range 22
# access-list 104 deny tcp 170.16.0.0 0.0.255.255 170.16.70.0 0.0.0.255 range 22
# access-list 104 permit ip 170.16.0.0 0.0.255.255 0.0.0.0 255.255.255.255
# R3 # interface E1
# Ip access group 104 out"""
    lines = a.split('\n')
    forstandard(lines)


def forstandard(lines):
    status = []
    fromip = []
    maskip = []
    toip = []
    tomask = []
    port = []
    for line in lines:
        value = line.__contains__("access-list")
        if value != True:
            break
        split = line.split()
        if split[2] == 'permit':
            status.append(1)
        elif split[2] == 'deny':
            status.append(0)
        fromip.append(split[4])
        maskip.append(split[5])
        toip.append(split[6])
        tomask.append(split[7])
        if len(split) == 10:
            port.append(split[9])
        else:
            port.append('any')
    advancedlogic(fromip, maskip, status, toip, tomask, port)


def advancedlogic(fromip, maskip, status, toip, tomask, port):
    inputfile = open(sys.argv[2], 'r')
    inputip = inputfile.read()
#     inputip = '''170.16.10.5 170.16.70.111 22
# 170.16.10.5 170.16.70.111 80
# 170.16.5.12 170.16.70.1 22
# 170.16.6.90 192.45.77.2 59'''
    processedlist = validate(fromip, maskip, status)
    toprocessedlist = validate(toip, tomask, port)
    # sumit we formed both list write logic for comparison
    inputlist = inputip.split('\n')
    for inputdata in inputlist:
        individual = inputdata.split()
        fromlist = individual[0].split('.')
        tolist = individual[1].split('.')
        tolist.append(individual[2])
        fromvalidation= verify(processedlist, fromlist, toprocessedlist, tolist)
        if fromvalidation == 'permit':
            print(f'Packet from {individual[0]} to {individual[1]} on port {individual[2]} permitted')
        else:
            print(f'Packet from {individual[0]} to {individual[1]} on port {individual[2]} denied')


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


def verify(processedlist, input, tolist, toip):
    match = False
    for acl, tol in zip(processedlist, tolist):
        ok = False
        match = False
        i = 0
        for each, inp, to, ip in zip(acl, input, tol, toip):
            i += 1
            if each == 'any':
                ok = True
            elif each == inp:
                ok = True
            else:
                ok = False
                break
            if i < 5:
                if to == 'any':
                    ok = True
                elif to == ip:
                    ok = True
                else:
                    ok = False
                    break
        if tol[4] == toip[4] or tol[4] == 'any':
           match = True
        if acl[4] == 1 and ok and match:
            return "permit"
        # if acl[4] == 1 and ok and not match:
        #     return "deny"
        elif acl[4] == 0 and ok and match:
            return "deny"
        # elif acl[4] == 0 and ok and not match:
        #     return "permit"
    return "deny"


def verifyto(toprocessedlist, tolist):
    for acl in toprocessedlist:
        ok = False
        for each, inp in zip(acl, tolist):
            if each == 'any':
                ok = True
            elif each == inp:
                ok = True
            else:
                ok = False
                break
    if ok:
        return "permit"
    else:
        return "deny"
    return "deny"


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    acllogic()

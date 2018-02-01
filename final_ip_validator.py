"""
IP validator. Checks for IPv4 or IPv6
addresses by passing in a list of 
addresses. Return list where each index
of returned list is IPv4, IPv6, or Neither.
"""

# [IPv4, IPv6, Neither, IPv4]
addresses = ['121.18.19.20', '2001:0db8:0000:0000:0000:ff00:0042:8329', 'this is a junk string', '222.181.190.212']


def checkIP(ip):
    validated = []
    for idx, i in enumerate(ip):
        if i.count('.') == 3:
            try:
                # Split possible ipv4 address along '.', ensure all sections are between [0-255] (2^8)
                validated.append('IPv4' if all(0 <= int(x) <= 255 for x in i.split('.')) else 'Neither')
            except ValueError as e:
                print(repr(e))
                validated.append('Neither')
        elif i.count(':') == 7:
            try:
                # Split along ':', convert hex string to int, ensure each section is between [0-65535] (2^16)
                validated.append('IPv6' if all(0 <= int(x, 16) <= 65535 for x in i.split(':')) else 'Neither')
            except ValueError as e:
                print(repr(e))
                validated.append('Neither')
        else:
            validated.append('Neither')
    return validated


answer = checkIP(addresses)
print(answer)
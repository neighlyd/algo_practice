CHAR_FOR_INT = '0123456789abcdef'

def to_string(num, base):
    if num < base:
        return CHAR_FOR_INT[num]

    return to_string(num//base, base) + CHAR_FOR_INT[num % base]


assert to_string(1453, 16) == '5ad'
assert to_string(10, 2) == '1010'
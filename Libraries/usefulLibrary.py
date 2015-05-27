__author__ = 'Aymen'

# Encode to sha512
def stringTosha512(myString):
    import hashlib
    m = hashlib.sha512()
    m.update(myString.encode('ascii'))
    sha512 = m.hexdigest()
    return sha512
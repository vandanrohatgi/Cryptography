import binascii
from itertools import cycle

def encrypt(message,key):
    encryptedMessage=''.join([
        (
            binascii.hexlify(
                chr(ord(x)^ord(y)).encode())
                ).decode() 
                for x,y in zip(message,cycle(key))
        ])
    return(encryptedMessage)

def decrypt(cipher,key):
    cipher=binascii.unhexlify(cipher.encode()).decode()
    decryptedText=''.join([
        chr(ord(y)^ord(x)) 
        for x,y in zip(cipher,cycle(key))
        ])
        
    return(decryptedText)


def crack():
    pass

cipher=encrypt("Helloworldz!","secretKey")

print(cipher)

print(decrypt(cipher,"secretKey"))
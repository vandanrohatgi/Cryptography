def encrypt(message,key):
    encryptedText=''
    for x in range(len(message)):
        temp=ord(message[x])+ord(key)-97
        if temp>122:
            encryptedText+= chr(temp-122+96)
        else:
            encryptedText+=chr(temp)
    return encryptedText

def decrypt(cipher,key):
    decrypted=''
    for x in range(len(cipher)):
        temp=ord(cipher[x])-ord(key)+97
        if temp<97:
            decrypted+=chr(temp+122-96)
        else:
            decrypted+=chr(temp)
    return decrypted

def crack(cipher):
    for x in range(26):
        attempt=''
        for y in range(len(cipher)):
            temp=x+ord(cipher[y])
            if temp>122:
                attempt+=chr(temp-122+96)
            else:
                attempt+=chr(temp)
        print(attempt)

cipher=encrypt("helloworldz","c")

#deciphered=decrypt(cipher,'c')
#print(deciphered)
crack(cipher)
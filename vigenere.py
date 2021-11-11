def encrypt(message,key):
    encryptedText=''
    i=0
    for x in range(len(message)):
        temp=ord(message[x])+ord(key[i])-97
        if temp>122:
            encryptedText+= chr(temp-122+96)
        else:
            encryptedText+=chr(temp)
        if i==(len(key)-1):
            i=0
        else:
            i+=1

    return(encryptedText)

def decrypt(message,key):
    decryptedText=''
    i=0
    for x in range(len(message)):
        temp=ord(message[x])-ord(key[i])+97
        if temp<97:
            decryptedText+= chr(temp+122-96)
        else:
            decryptedText+=chr(temp)
        if i==(len(key)-1):
            i=0
        else:
            i+=1
    return decryptedText


def crack(message):
    pass

Text=encrypt("seeyouatnoon","spy")

print(Text)
print(decrypt(Text,"spy"))


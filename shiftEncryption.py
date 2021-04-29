def encrypt(m,s):
    #m = message
    #s = shift (the key)
    #direction = shift direction

    result = ""
    for i in m:
        
        if (i.isupper()):
            result += chr((ord(i) + s-97) % 26 + 97)

        elif i == " ":
            result += " "
            
        else:
            result += chr((ord(i) + s - 65) % 26 + 65)

    return result

def decrypt(c,k):
    #c = chiper text (encryption text)
    #k = key
   
    for j in range(1,26):
        result = ""
        for i in c:
            
            if (i.isupper()):
                result += chr((ord(i) - j-97) % 26 + 97)
            elif i == " ":
                result += " "
            
            else:
                result += chr((ord(i) - j - 65) % 26 + 65) 
            
        if j == k:
            #print("decryption: ", result)
            break
        
    return result
    

m = "wkwkkw"
s = 5
enc = encrypt(m,s)

dec = decrypt(enc,s)
print("encryption: ", enc)
print("decryption: ", dec)



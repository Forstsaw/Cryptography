import random


rawText = "hello world"
key = "" # The Key for encrypt or decrypt

# convert plaint text to binary
def convertStringToBinary(m): 
    return ' '.join(format(ord(x), 'b') for x in m).split(" ")
m = convertStringToBinary(rawText)


#generate random binary key
for i in range(len(m)):
	key += str(random.randint(0,1))



# add 0 to every binary until 8 bit
def convertTo8bit(binary):
    binary_8bit =""
    for i in binary:
        temp = i
        while len(temp) != 8:
            temp = '0'+temp
        binary_8bit += temp
        
    return binary_8bit
m = convertTo8bit(m)
key = convertTo8bit(key)

#encrypt the message with the key 
def encrypt(m,k):
        result = ""
        for i in range(len(m)):
                result += str(int(m[i])^int(k[i]))
        return result

#decrypt the cipher text with the key 
def decrypt(c,k):
        result = ""
        for i in range(len(c)):
                result += str(int(c[i])^int(k[i]))
        return result


c = encrypt(m,key)
d = decrypt(c,key)
plainDec = ''.join(chr(int(x, 2)) for x in (d[8*i:8*i+8] for i in range(len(d)//8))) #convert binary to ascii
print("\t\tSTREAM CIPHER ALGORITHM BY FORSTSAW\n")
print("Message (Plain Text) : ", rawText)
print("Binary: ", m)
print("Key : ", key)	
print("Encryption : ", c)
print("Decryption : ", d)
print("Plaint text (Decryption): ",plainDec)

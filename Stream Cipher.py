import random


rawText = "Forstsaw"
m = ''.join(format(ord(x), 'b') for x in rawText) # convert plaint text to binary
key = "" # The Key for encrypt or decrypt


#generate random binary key
for i in range(len(m)):
	key += str(random.randint(0,1))


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

print("\t\tSTREAM CIPHER ALGORITHM BY FORSTSAW\n")
print("Message (Plain Text) : ", rawText)
print("Binary: ", m)
print("Key : ", key)	
print("Encryption : ", c)
print("Decryption : ", d)

#author Fortsaw
def checkKey(k):
    #the key must be 8 bit
    if len(k) < 8:
        check = 8-len(k)
        for i in range(check):
            k +=" "
        print("key after process:",k)
    elif len(k) > 8:
        k = k[:8]
        print("key after process:",k)
    return k

#convert string to binary
def convertStringToBinary(m): 
    return ' '.join(format(ord(x), 'b') for x in m).split(" ")


# add 0 to every binary until 8 bit (ex = 10010 to 00010010)
def convertTo8bit(binary):
    binary_8bit =""
    for i in binary:
        temp = i
        while len(temp) != 8:
            temp = '0'+temp
        binary_8bit += temp
        
    return binary_8bit

#the f function Li⊕ 'F(Ri,Ki)'
def xor(r,k):
    #r = right
    #k = the key from the iteration
    result = ""
    for i in range(len(r)):
            result += str(int(r[i])^int(k[i]))
    return result

def encrypt(m,key):

    #check the key if the key is 8 character
    k = checkKey(key)
    print("Check Key :", k )
    
    binary_m = convertStringToBinary(m)
    binary_k = convertStringToBinary(k)
    print("message (CTB):", binary_m)
    print("key (CTB):", binary_k)

    print('\n')
    #convert to 8 bit every binary
    binary_m = convertTo8bit(binary_m)
    binary_k = convertTo8bit(binary_k)
    print("message (CT8b):", binary_m)
    print("key (CT8b):", binary_k)
    
    
    #split into 2 slice left and right
    L = binary_m[:int(len(binary_m)/2)]
    R = binary_m[int(len(binary_m)/2):]
    print("Left Message #0 :", L)
    print("Right Message #0 :", R)
    
    enc = "" #temp and for calculate the result of F function F(Ri,Ki)
    keyList = processKey(binary_k,16)

    #the main of feistel cipher (encryption)
    j = 0
    for i in keyList:
        
        enc = xor(L,xor(R,i)) # the function of f
        R = L
        L = enc

        j+=1
        print("Left #{0} : {1}".format(j,L))
        print("Right #{0} : {1}".format(j,R))
        

    return L + R

#decrypt the cipher text
def decrypt(c,k):
    #c = cipher text(encryption text)
    #k = key
    k = checkKey(key)
    binary_k = convertStringToBinary(k)
    binary_k = convertTo8bit(binary_k)
    L = c[:int(len(c)/2)]
    R = c[int(len(c)/2):]
    j = 0
    keyList = processKey(binary_k,16)
    print(keyList)
    keyList = keyList[::-1] #reverse the keylist
    print(keyList)
    
    for i in keyList:
        a = xor(R,i)
        enc = xor(L,a)

        L = R
        R = enc

    return L + R

#shift first letter to right to the lastest letter in the key
def processKey(k, loop):
    #k =  key
    #loop = number iteration for generate key
    key = []
    for i in range(loop):
        k = k[1:len(k)]+k[0]
        key.append(k)
    return key


m = "forstsaw"
key = "AUDHJSHD#1"

enc = encrypt(m,key)
dec = decrypt(enc,key)
print("\t\tFEISTEL CIPHER ALGORITHM BY FORSTSAW")
print("Message :",m)
print("Key :",key)
print("Encryption : ", hex(int(enc,2)))
print("Binary Decryption:",dec)
print("Decryption :",''.join([chr(int(dec[i:i+8], 2)) for i in range(0, len(dec),8)]))







        

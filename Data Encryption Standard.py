#convert binary to decimal
def binary_to_decimal(num):
	b = list(num)
	n = len(list(num))
	decimal = 0
	hold = 0
	i = 0
	exp = n-1
	while (i < n):
		x = int(b[i])
		quot= 2**exp
		hold = x*quot
		i += 1
		exp -= 1
		decimal = decimal + hold
	return(decimal)

#DECIMAL TO BINARY
def decimal_to_binary(num):
	quot = int(num)
	base = 0
	counter = 0
	binary=[]
	while (quot > 0):
		rem = quot%2
		binary.append(str(rem))
		quot = quot//2
		counter +=1

	binary.reverse()
	return(int(''.join(binary)))

    
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


import random

#random permutation
def randomPermutation():
    p = []
    while len(p) < 64:
        choose = random.randint(1,64)
        
        if choose not in p:
            p.append(choose)
    #print(p)
    print(len(p),max(p))
    return p #return with list type


#use randomPermuation Function first
#to convert original location of key bit to the location of the permutation
#ex = original 010010 to 101000 depend to the permuation 
def convertPermutationLocation(k,p):
    #k = key
    #p = lift of random permutation from randomPermuation Function
    kp = [] #key permuation
    stop = 1
    print(k)
    print(len(k))
    print("a",p)
    for i in p:
        kp.append(int(k[i-1]))
        if stop == 56:
            print(kp)
            break
        stop+=1
    return kp  #return with list type
    

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
    while len(result) < len(self):
            result = '0' + result
    for i in range(len(r)):
            result += str(int(r[i])^int(k[i]))
    return result

#shift first letter to right to the lastest letter in the key
def shiftkey(k, shift,loop):
    #k =  key
    #loop = number iteration for generate key
    key = []
    j = []
    for i in range(loop):
        print(len(shift))
        for j in range(shift[i]):
            k = k[1:len(k)]+k[0]
            print(k)
        key.append(k)
    return key



#shift first letter to right to the lastest letter in the key
def processKey(k, loop):
    #k =  key
    #loop = number iteration for generate key
    key = []
    
    for i in range(loop):
        print(type(k))
        print(k)
        print(type(k[0]),k[0])
        k = k[1:len(k)]+k[0]
        key.append(k)
    return key

def seperateTo6Bit(m):
    a = []
    res = ""
    for i in range(len(m)):
        res += m[i]
        if i % 6 == 0 and i != 0:
            a.append(res)
            res = ""
    return a

def sbox(x,y,i):
    #x = column
    #y = row
    #i tell the location of the box
        
    box = {0:
                [[14,  4, 13,  1,  2, 15, 11,  8,  3, 10,  6, 12,  5,  9,  0,  7],
                 [ 0, 15,  7,  4, 14,  2, 13,  1, 10,  6, 12, 11,  9,  5,  3,  8],
                 [ 4,  1, 14,  8, 13,  6,  2, 11, 15, 12,  9,  7,  3, 10,  5,  0],
                 [15, 12,  8,  2,  4,  9,  1,  7,  5, 11,  3, 14, 10,  0,  6, 13]],
              1:
                [[15,  1,  8, 14,  6, 11,  3,  4,  9,  7,  2, 13, 12,  0,  5, 10],
                 [ 3, 13,  4,  7, 15,  2,  8, 14, 12,  0,  1, 10,  6,  9, 11,  5],
                 [ 0, 14,  7, 11, 10,  4, 13,  1,  5,  8, 12,  6,  9,  3,  2, 15],
                 [13,  8, 10,  1,  3, 15,  4,  2, 11,  6,  7, 12,  0,  5, 14,  9]],
              2:
                [[10,  0,  9, 14,  6,  3, 15,  5,  1, 13, 12,  7, 11,  4,  2,  8],
                 [13,  7,  0,  9,  3,  4,  6, 10,  2,  8,  5, 14, 12, 11, 15,  1],
                 [13,  6,  4,  9,  8, 15,  3,  0, 11,  1,  2, 12,  5, 10, 14,  7],
                 [ 1, 10, 13,  0,  6,  9,  8,  7,  4, 15, 14,  3, 11,  5,  2, 12]],
              3:
                [[ 7, 13, 14,  3,  0,  6,  9, 10,  1,  2,  8,  5, 11, 12,  4, 15],
                 [13,  8, 11,  5,  6, 15,  0,  3,  4,  7,  2, 12,  1, 10, 14,  9],
                 [10,  6,  9,  0, 12, 11,  7, 13, 15,  1,  3, 14,  5,  2,  8,  4],
                 [ 3, 15,  0,  6, 10,  1, 13,  8,  9,  4,  5, 11, 12,  7,  2, 14]],
              4:
                [[ 2, 12,  4,  1,  7, 10, 11,  6,  8,  5,  3, 15, 13,  0, 14,  9],
                 [14, 11,  2, 12,  4,  7, 13,  1,  5,  0, 15, 10,  3,  9,  8,  6],
                 [ 4,  2,  1, 11, 10, 13,  7,  8, 15,  9, 12,  5,  6,  3,  0, 14],
                 [11,  8, 12,  7,  1, 14,  2, 13,  6, 15,  0,  9, 10,  4,  5,  3]],
              5:
                [[12,  1, 10, 15,  9,  2,  6,  8,  0, 13,  3,  4, 14,  7,  5, 11],
                 [10, 15,  4,  2,  7, 12,  9,  5,  6,  1, 13, 14,  0, 11,  3,  8],
                 [ 9, 14, 15,  5,  2,  8, 12,  3,  7,  0,  4, 10,  1, 13, 11,  6],
                 [ 4,  3,  2, 12,  9,  5, 15, 10, 11, 14,  1,  7,  6,  0,  8, 13]],
              6:
                [[ 4, 11,  2, 14, 15,  0,  8, 13,  3, 12,  9,  7,  5, 10,  6,  1],
                 [13,  0, 11,  7,  4,  9,  1, 10, 14,  3,  5, 12,  2, 15,  8,  6],
                 [ 1,  4, 11, 13, 12,  3,  7, 14, 10, 15,  6,  8,  0,  5,  9,  2],
                 [ 6, 11, 13,  8,  1,  4, 10,  7,  9,  5,  0, 15, 14,  2,  3, 12]],
              7:
                [[13,  2,  8,  4,  6, 15, 11,  1, 10,  9,  3, 14,  5,  0, 12,  7],
                 [ 1, 15, 13,  8, 10,  3,  7,  4, 12,  5,  6, 11,  0, 14,  9,  2],
                 [ 7, 11,  4,  1,  9, 12, 14,  2,  0,  6, 10, 13, 15,  3,  5,  8],
                 [ 2,  1, 14,  7,  4, 10,  8, 13, 15, 12,  9,  0,  3,  5,  6, 11]]}
    return decimal_to_binary(box[i][y][x])
    # return to decimal from binary example 0101 to 5

    
def convertToSBlocks(m):
    x = -1
    y = -1
    ite = 0
    result = ""
    for i in m:
        if i[0] == "1" and i[5] == "0":
            y = 2
            z = i[1:5]
            x = binary_to_decimal(z)
            b = sbox(x,y,ite) #binary of the sblocs
        elif i[0] == "0" and i[5] == "0":
            xy= 0
            z = i[1:5]
            x = binary_to_decimal(z)
            b = sbox(x,y,ite) #binary of the sblocs

        elif i[0] == "1" and i[5] == "1":
            y = 3
            z = i[1:5]
            x = binary_to_decimal(z)
            b = sbox(x,y,ite) #binary of the sblocs
        elif i[0] == "0" and i[5] == "1":
            y = 1
            z = i[1:5]
            x = binary_to_decimal(z)
            b = sbox(x,y,ite) #binary of the sblocs
        result += b
        ite+=1
    return result
            
            
#prosess DES
def processEncrypt(m,LM,RM,k,p):
    #LM = Left message
    #RM = Right Message
    #m = Message
    #k = list of key
    #p = permutation
    loc_k = [32,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21
             ,22,23,24,25,26,27,28,29,30,31,32,1]
    #Expand Right from 32 bits to 48 according to permutation (message)
    kp = keyPermutation(R,lock_k)
    for i in range(16):
        res = xor(kp[i],k[i])
        s = seperateTo6Bit(res)
        c = convertToSBlocks(s)
        sblockPermutation = keyPermutation(c,p)
    
    

#subkey creation
def keyProcess(k,p):
        #key
        #permutation
        shift = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
        L = k[:int(len(k)/2)]
        R = k[int(len(k)/2):]
        LK = processKey(L,16)
        RK = processKey(R,16)
        LS = shiftkey(L,shift,16)
        RS = shiftkey(R,shift,16)
        key = []
        for i in range(16):
                
                fusionKey = LS[i] + RS[i]
                k = L + R
                k = keyPermutation(k,p)
                key.append(k)
        return key

        
        

def encrypt(m,k):
    #rp = randomPermutation()
    #print("RP : ",rp)
    permutation = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34,
               26, 18, 10, 2, 59, 51, 43, 35, 27, 19, 11, 3,
               60, 52, 44, 36, 63, 55, 47, 39, 31, 23, 15, 7,
               62, 54, 46, 38, 30, 22, 14, 6, 61, 53, 45, 37,
               29, 21, 13, 5, 28, 20, 12, 4]
    c = keyPermutation(b_k,kp1)
    print(c)
    cp = convertPermutationLocation(b_k,kp1)
    b_m = convertStringToBinary(m)
    b_k = convertStringToBinary(k)

    b_m = convertTo8bit(b_m)
    b_k = convertTo8bit(b_k)
    print(b_k)
    kp = keyPermutation(b_k,rp)
    print("KP",kp)

    L = b_m[:int(len(b_m)/2)]
    R = b_m[int(len(b_m)/2):]
    kp = ''.join(kp)
    #keyList = processKey(kp,16)
    kp = keyProcess(b_k,kp)
    for i in keyList:
        enc = xor(L,xor(R,i)) # the function of f
        R = L
        L = enc

    return L + R,keyList

    


m = "IEOFIT#1"
key = "IEOFIT#1"
encrypt(m,key)

#key = checkKey(key) #return string
#kp1 = randomPermutation() #return list and random number 1-64 for key location

shift = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
L = k[:int(len(k)/2)]
R = k[int(len(k)/2):]
LK = processKey(L,16)
RK = processKey(R,16)
LS = shiftkey(L,shift,16)
RS = shiftkey(R,shift,16)
    
#kp = keyProcess("00000000001111111100000010100100110000101110000101010000",kp1)
#print(kp)

#enc,keyList = encrypt(m,key)
#dec = decrypt(enc,keyList)
#print("Encryption :",  hex(int(enc,2)))
#print("Decryption :",''.join([chr(int(dec[i:i+8], 2)) for i in range(0, len(dec),8)]))

"""
step 1:
User input =  forstsaw
change to binary
key = AUDHJSHD#1 change to binary


step2:
generate key permuation
original
1	2	3	4	5	6	7	8	9	10	
0	1	0	0	1	0	0	1	0	1


key permuation
57	49	41	33	25	17	9	1	58	50
0	0	0	0	0	0	0	0	0	0



"""


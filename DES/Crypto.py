from BinaryConverter import decimal_to_binary, binary_to_decimal, convertStringToBinary
from Permutation import p56bit, p48bit, p64bit, E48, E32, Final
from Sboxes import SBOXES,locationSBoxs
class DES:

    def __init__(self,message,key):
        self.oriKey = ""
        self.oriMes = ""
        self.m = message 
        self.k = key
        self.keys = ""

    #convert string to binary
    def convertToBinary(self):
        self.m = convertStringToBinary(self.m) #return to string in 8 bit binary
        self.k = convertStringToBinary(self.k) #return to string in 8 bit binary
        self.oriKey = self.k
        self.oriMes = self.m
    #shifting the first string to the last string depend on the shift[i]
    def shift(self,k, shift):
        #k =  key
        #shift =  how many time we shift the key
        print("Shift : ",shift)
        #print(k)
        #print(k[1:len(k)])
        for i in range(shift):
            k = k[1:len(k)]+k[0]
        return k
    def PLocation(self,k,permutation):
        
        #k = key
        #bit = the bit ex 48
        #location 
        
        kp = "" #key permuation

        
        #process of converting original location to permutation location
        
        for i in permutation:
            #kp.append(int(k[i-1]))
            kp += k[i-1]
            
            #print(k[i])
            

        return kp  #return with list type
        
        

    
    #divide by 2 and become left and right
    #shift the first binary every round by shift list
    #example : 0001, shift by 1 -> 0010
    #convert to permutation location after shifting
    #example : 0010, the permutation location is 3,4,1,2 -> 1000
    def keyProcess(self):
        #key
        #permutation
        
        
        k = self.PLocation(self.k,p56bit)
        print("key permutation : ",k )
        shift = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
        keys = []
        L = k[:int(len(k)/2)] #left
        R = k[int(len(k)/2):] # right
        print("Left: ",L)
        print("Right : ",R)
        for i in range(16):         
            L = self.shift(L,shift[i])
            R = self.shift(R,shift[i])
            print("Left (after shift): ",L)
            print("Right (after shift): ",R)
            print("length L and R after update : ",len(L),len(R))
            LR = L + R
            print("L+R : ",LR)
            key = self.PLocation(LR,p48bit)
            print("length key : ",len(key))
            keys.append(key)
            print("key {0} : {1}".format(i+1,key))
            print()
            
        return keys

    #the f function Li⊕ 'F(Ri,Ki)'
    def xor(self,r,k):
        #r = right
        #k = the key from the iteration
        result = ""
        for i in range(len(r)):
                result += str(int(r[i])^int(k[i]))
        return result
    
    def shrinkSBoxes(self,x1,x2,binary,ite):
        if x1 == "1" and x2 == "0":
            y = 2
            
            x = binary_to_decimal(binary)
            b = locationSBoxs(x,y,ite) #binary of the sblocs
        elif x1 == "0" and x2 == "0":
            y= 0
            x = binary_to_decimal(binary)
            b = locationSBoxs(x,y,ite) #binary of the sblocs

        elif x1 == "1" and x2 == "1":
            y = 3
            
            x = binary_to_decimal(binary)
            b = locationSBoxs(x,y,ite) #binary of the sblocs
        elif x1 == "0" and x2 == "1":
            y = 1
            
            x = binary_to_decimal(binary)
            b = locationSBoxs(x,y,ite) #binary of the sblocs
       
        return b
    
    def shrink(self,m):
        #m is xored by rupdate and key[i]
        #find the first and last every 6 bit is the position row
        #and the middle of first and last is the position column
        #then find the location in sbox with row and column
        #convert the decimal value to binary
        #then combine it and permutate it
        row = -1
        col = -1
        ite = 0
        encryptedMessage = ""
        for i in range(0,len(m),6):
            x1 = m[i]
            x2 = m[i+5]
            bina = m[i+1]+m[i+2]+m[i+3]+m[i+4]
            print("x1",x1)
            print("x2",x2)
            print("binary",bina)
            
            res = self.shrinkSBoxes(x1,x2,bina,ite)
            encryptedMessage += res
            print("hasil shrink ",res)
            ite+=1
            
        print("Encrypted message before permutation ",encryptedMessage)
        return encryptedMessage
    def expand(self,L,R):
        """
        convert from 32 bit to 48 bit by number location in Permutation E48
        after converted, the converted value xor with the key[i]
        then shrink
        """
        for i in range(1):
            print("Left : ",L)
            print("right: ",R)
            rUpdate = self.PLocation(R,E48)
            print("expand: ",rUpdate)
            xored = self.xor(rUpdate,self.keys[i])
            print("result of xor :",xored)
            shrinked = self.shrink(xored)
            encrypted = self.PLocation(shrinked,E32)
            print("Encrypted Message {0}: {1}".format(i+1,encrypted))
            temp = L
            L = encrypted
            R = temp
        return self.PLocation(R + L,Final)
             
            
            
        

    def encryptProcess(self):
        print("Encrypt")
        self.m = self.PLocation(self.m,p64bit)
        L = self.m[:int(len(self.m)/2)] #left
        R = self.m[int(len(self.m)/2):] # right
        #print("Left : ",L)
        #print("right: ",R)
        
        Encrypted = self.expand(L,R)
        print("Encrypted Message: ",Encrypted)
        return Encrypted
        
    
    def encrypt(self):
        self.convertToBinary()
        self.keys = self.keyProcess()
        print(self.keys)
        enc = self.encryptProcess()
        return hex(int(enc,2))

    def show(self):
        print(self.m)
        print(self.k)
        

    
    
    

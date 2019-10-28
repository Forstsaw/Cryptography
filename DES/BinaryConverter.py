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
	return(decimal) #return int


#CONVERT DECIMAL TO BINARY
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
	print("dec bin ",binary)
	return(int(''.join(binary))) #return int

#convert to any bit 
def convertToxbit(binary,bit):
    binary = str(binary)
    
    binary_xbit =""
    
    temp = ""
    while len(temp)+len(binary) != bit :
        temp += '0'
    binary_xbit += temp+binary
        
    return binary_xbit

def convertTo8bit(binary):
    
    binary_8bit =""
    for i in binary:
        temp = i
        while len(temp) != 8:
            temp = '0'+temp
        binary_8bit += temp
        
    return binary_8bit

#convert string to binary
def convertStringToBinary(m): 
    binary =  ' '.join(format(ord(x), 'b') for x in m).split(" ")# return list
    binary = convertTo8bit(binary)
    print("8 Bit Binary : ",binary)
    return binary

if __name__ == '__main__':
    print(binary_to_decimal("1010"))
    print(decimal_to_binary(10))
    c = convertStringToBinary("IEOFIT#1")
    print(c)
    

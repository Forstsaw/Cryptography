
from Crypto import DES



if __name__ == '__main__':
    m = "IEOFIT#1"
    key = "IEOFIT#1"
    c = DES(m,key)
    d = c.encrypt()
    print("Hex : ",d)
    #c.show()
    
    

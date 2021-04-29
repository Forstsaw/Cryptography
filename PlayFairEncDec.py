import random
import math

message = "hello"

class PlayFair():
    
    
    def __init__(self,message):
        
        
        self.m = message
        self.randomTableWord = []
        self.word = []
        self.temp = ""
        self.words = "abcdefghijklmnopqrstuvwxy"
        self.wordToList(self.words)

    def wordToList(self,word):#change word to array
        for i in word:
            self.word.append(i)
        print(self.word)
        

    def chooseWord(self):
        test = False
        for i in self.words:
            choose = random.choice(self.word)

            self.randomTableWord.append(choose)
            for j in self.word:
                if j == choose:
                    self.word.remove(choose)
                    
        #print(self.randomTableWord)
        
        
    def showRandTable(self):
        num = 0
        table = ""
        for i in self.randomTableWord:
            table += i + ' | '
            num+=1
            if num % 5 == 0:
                table += "\n"

        print(table)
        return self.randomTableWord
                    
            
    def randomWord(self):
       
        self.chooseWord()

    def processEnc(self,position):
        c = ""  #cipher text (encryption text)
        print(position)
        num = 0
        for j in position:
            pass
            #c += self.randomTableWord[j]
            
        limit = math.ceil(len(position)/2)
            
        for i in range(0,limit,2):
            if(position[num]-position[num+1] == 1 and (position[num] < 20 or position[num+1] < 20)):
                
                c += self.randomTableWord[position[num]+1]
                c += self.randomTableWord[position[num]+1]
                num +=1
            elif (position[num]-position[num+1] == 1 and (position[num] > 5 or position[num+1] > 5)):
                c += self.randomTableWord[position[num]-1]
                c += self.randomTableWord[position[num]-1]
                num +=1
            else:
                if self.randomTableWord[position[num] < 20] :
                    print(position[num]+4)
                    print(self.randomTableWord[position[num]+5])
                    c += self.randomTableWord[position[num]+5]
                    if(self.randomTableWord[position[num] < 20])
                    
                elif elf.randomTableWord[position[num] > 4]:
                    c += self.randomTableWord[position[num]-5]
                                        
                
                num +=1
        print(c)

    def encryption(self):
        position = []
        
        c = ""  #cipher text (encryption text)
        for i in self.m:
            num = 0
            for j in self.randomTableWord:
                if j == i:
                    position.append(num)
                    break
               

                num += 1
        self.processEnc(position)
        
                
        


a = PlayFair("hellos")
a.randomWord()
key = a.showRandTable()
a.encryption()
            
            
        

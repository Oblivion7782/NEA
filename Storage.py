import os
file_path = 'Storage.txt'

dataing = [["Username","ConvenientUsername"], ["Password","Fo0tBa1l12£"], ["Score",0]]
dataing2 = [["Username","LovePizza"], ["Password","RuGbY0!23"], ["Score",0]]

class storing:
    def __init__(self):
        self.dataing = dataing
        self.dataing2 = dataing2

    def rData(self):
        with open("Storage.txt", "r+") as f:
            readData = f.read() 
            print(readData)  
            return readData  

    def WorA(dataing): #Write or Append
        if os.stat(file_path).st_size == 0:
            emptyData = True
        readData = storing.rData()
        if emptyData:    
            with open('Storage.txt', 'w+') as f:
                writeData = dataing
                f.write(writeData)
                return writeData
        else:
            with open('Storage.txt', 'a') as f:
                appendData = dataing
                f.write(appendData)
                return appendData

choice = ""
player = storing.WorA(dataing)
#player2 = WorA(dataing2)
print(player)
#print(player2)

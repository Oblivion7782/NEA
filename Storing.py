dataing = """{ 
    "playerdata": [ 
    
        {   
            "id":"01",
            "Username":"ConvinientUsername", 
            "Password":"Fo0tBa1l12£", 
            "Score":0
        }, 
    
        {
            "id":"02",
            "Username":"LovePizza", 
            "Password":"RuGbY0!23", 
            "Score":0
        } 
    ]
}"""

import json

def rData():
    with open("Storing.json", "r+") as file:
        readData = json.load(file)
        print(readData)  
        file.close()  

def wData(dataing): #Write
    with open('Storing.json', 'a+') as file:
        json.dump(dataing, file)
        file.close()


playerData = wData(dataing)
player2Data = rData()
print(playerData)
print(player2Data)



#if os.stat(file_path).st_size == 0:
#        emptyData = True
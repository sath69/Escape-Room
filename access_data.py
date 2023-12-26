import json

def saveData(file,data,mode="w"):
    with open(f"{file}.json", mode) as jsonFile:
        json.dump(data,jsonFile,indent=4)

def loadData(file,mode="r"):
    with open(f"{file}.json", mode) as jsonFile:
        data=json.load(jsonFile)
        return data

def writeData(file,data,mode="w"):
    with open(f"{file}.txt", mode) as f:
        f.write(str(data))

def readData(file, mode="r"):
    with open(f"{file}.txt", mode) as f:
        return f.read()
#yo so r we done

          
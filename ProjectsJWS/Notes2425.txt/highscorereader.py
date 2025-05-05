with open("highscores.csv","r") as file:
    theWholeFile = file.readlines()
    
cleanData=[]
for eachLine in theWholeFile:
    print(eachLine.replace(",","\t"))

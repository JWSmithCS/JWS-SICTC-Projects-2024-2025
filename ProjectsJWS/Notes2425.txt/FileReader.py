'''
Flat file database - txt, csv, xlsx - one file for your entire db
relational Database - multiple tables or files

Delineator-the thing that seperates columns in a file

CRUD - Acronym for basic functions of databases
    c - create
    r - read
    u - update
    d - Delete
'''
with open("Classroom.txt","w") as file:
    id=["01110","00111","10001","00101","00110"]
    students=["john","banks","danks","don","moneys"]
    out=""
    for i in range(len(id)):
        out+=f"{id[i]},{students[i]}\n"
        
    file.write(out)
    file.close()
    
    
with open("Classroom.txt","r") as file:
    theWholeFile = file.readlines()
    print(theWholeFile)
    file.close()
    
    
with open("Classroom.txt","a") as file:
    newStudent = "00000,Bander\n"
    file.write(newStudent)
    file.close
    
colors=["green","Chartreuse","purple","blue","red","silver"]

cleanData=[]
for eachLine in theWholeFile:
    cleanData.append(eachLine.rstrip())


for i in range(len(colors)):
    cleanData[i]+=f",{colors[i]}\n"
print(cleanData)

with open("Classroom.txt","w") as file:
    out=""
    for i in range(len(cleanData)):
        out+=cleanData[i]
        
    file.write(out)
    file.close()
    
with open("Classroom.txt","r") as file:
    theWholeFile = file.readlines()
    print(theWholeFile)
    file.close()
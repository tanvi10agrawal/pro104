import csv 
with open("HW.csv", newline="") as f:
    data=csv.reader(f)
    filedata=list(data)
filedata.pop(0)
newdata=[]
for i in range(len(filedata)):
    number=filedata[i][2]
    newdata.append(float(number))

n=len(newdata)
totalweight=0
for i in newdata:
    totalweight=totalweight+i

mean=totalweight/n
print("This is the average weight of an 18 year old person as per the data: " + str(mean))
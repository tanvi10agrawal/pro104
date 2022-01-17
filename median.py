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
print("This is the length of the data: "+str(n))
newdata.sort()

if n%2 == 0:
    m1=float(newdata[n//2])
    m2=float(newdata[n//2-1])
    median=(m1+m2)/2
else:
    median=newdata[n//2]

print("The median of the data set is: " + str(median))
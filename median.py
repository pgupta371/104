import csv

with open("data104.csv", newline = "") as f:
    reader = csv.reader(f)
    fileData = list(reader)

fileData.pop(0)

#print(file_data)
#sorting data to get the height of people
newData = []

for i in range(len(fileData)):
    num = fileData[i][1]
    newData.append(float(num))


# get the median

n=len(newData)
newData.sort()

#use floor division to ge thte nearest whole number
#floor div is shown by //
if n%2 == 0:
    #1st number
    median1=float(newData[n//2])

    #2nd number
    median2=float(newData[n//2-1])

    median=(median1+median2)/2

else:
    median=newData[n//2]
    print(n)

print("median is -"+ str(median))

print    
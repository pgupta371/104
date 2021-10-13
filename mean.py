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


# get the mean

n=len(newData)
t=0
for x in newData:
    t +=x

mean =t/n

print("mean of heights is :-" +str(mean))
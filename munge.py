# Place code below to do the munging part of this assignment.
import os
platform_agnostic_file_path = os.path.join('data', 'NasaData.txt')


#This opens the file in read mode
f = open(platform_agnostic_file_path, 'r')
allLines = f.readlines()

#Removes the heading in the file
for i in range(0, 7):
    del allLines [0]

    length = len(allLines)
    del allLines[length - 1]


#Removes all the line breaks and the extra headings
j = 1
while j < len(allLines):
    if allLines[j] == "\n":
        allLines.pop(j)
        j -= 1
    elif allLines[j][:4] == "Year":
        allLines.pop(j)
        j -= 1
    j += 1


#This is where I selected to delete all rows of data that have missing data. As long as they are indicated by at least one *, then that whole row is deleted.
k = 1
while k < len(allLines):
    temp = allLines[k]
    if ("*" in temp):
        allLines.pop(k)
        k-= 1
    k+=1


data = []
#This removes the last year index and changes all the values into %change in F
#This is stored in data
for k in range(0, len(allLines)):
    tempData = allLines[k].strip().split()[:19]
    if k >= 1:
        for kp in range (1, len(tempData)):
            tempData[kp] = format(((float(tempData[kp])/100) * 1.8), '.1f')
    data += [tempData]

#Creates and open a new file that will store all of the data in csv format
#The new file is called cleanedData.csv
newFile = os.path.join('data', 'cleaned_data.csv')

newF = open(newFile, "w")

#Stores the rows of values as comma separated values
for pl in range(0, len(data)):
    row = data[pl]
    line = ""
    for val in row:
        line += val + ','
    line = line[:-1]
    if(pl == len(data) - 1):
        newF.write(line)
    else:
        newF.write(line + '\n')

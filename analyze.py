# Place code below to do the analysis part of the assignment.
import csv
import os

#Opens the csv with all the data
platform_agnostic_file_path_analyze = os.path.join('data', 'cleaned_data.csv')
f = open(platform_agnostic_file_path_analyze, "r")
readData = csv.DictReader(f)


keys = ["Jan", "Feb", "Mar", "Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

localSum = 0
yearCounter = 0


#The loop works as follows:
#The localSum and yearCounter varaibles will keep track the temporary sum and number of years summed over. These values will be reset to 0 at the end of every decade.
#We will continue to sum up (by every row) until we get to any year with the last digit 9, where we will output the average.

for line in readData:
    for i in range(0, len(keys)):
        localSum += float(line[keys[i]])
    if int(line["Year"][3]) == 9:
        if int(line["Year"]) - 9 == 1880:
            print(f"The Average temperature change anomalies in Farenheit between 1881 and 1899 is {round(localSum/(yearCounter*12),2)} degrees")
        else:
            print(f"The Average temperature change anomalies in Farenheit between {int(line['Year']) - 9} and {line['Year']} is {round(localSum/(yearCounter*12), 2)} degress")
        localSum = 0
        yearCounter = 0
    
    finalYear = line['Year']
    yearCounter += 1

#This section is for the remaining years (where the last digit is less than 9)
#The average for the remaining years that don't make up a decade
remainingYearCounter = yearCounter - 1
print(f"The Average temperature change anomalies in Farenheit between {int(finalYear) - remainingYearCounter + 1} and {int(finalYear)} is {round(localSum/(remainingYearCounter*12), 2)} degress")



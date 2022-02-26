import re
import json

fileToRead = 'websiteData.txt'
delimiterInFile = [',', ';']

def validateEmail(strEmail):
    # .* Zero or more characters of any type. 
    if re.match("(.*)@(.*).(.*)", strEmail):
        return True
    return False

def CheckHuman(strEmail):
    b = strEmail.partition('@') 
    c = b[0]
    if "." in c or len(c)>8:
        return True
    return False

def getdata(key, listt):
    if key in listt:
        return "Human"
    else:
        return "Non-Human"

#creating an empty list to find all the emails present, which is further counted and tested as human or non human
listEmail = []

file = open(fileToRead, encoding="utf8") 
# Read every line of file
listLine = file.readlines()

for itemLine in listLine:
    item =str(itemLine)
    for delimeter in delimiterInFile:
        item = item.replace(str(delimeter),' ')
    
    wordList = item.split()

    for word in wordList:
        if(validateEmail(word)):
            listEmail.append(word)

# Create an empty dictionary
d = {}
# Loop through each line of the file
for line in listEmail:
    # Split the line into words
    words = line.split(" ")
    # Iterate over each word in line
    for word in words:
        # Check if the word is already in dictionary
        if word in d:
            # Increment count of word by 1
            d[word] = d[word] + 1
        else:
            # Add the word to dictionary with count 1
            d[word] = 1

 # Create a empty list to store human type emails 
listhuman = []

for key in list(d.keys()):
    if(CheckHuman(key)):
            listhuman.append(key)

# Create a empty dictionary
Dict = { }
for key in list(d.keys()):
    Dict[key] = {}
    Dict[key]['Occurance'] = d[key]
    Dict[key]['EmailType'] = getdata(key, listhuman)
    
# Dump to json file
with open("result.json","w") as f:
    json.dump(Dict,f)

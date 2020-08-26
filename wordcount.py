# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from tabulate import tabulate # Used for rendering resulting data in easily readable table
import numpy as np # Used functions: np.round()

def hitung_kata(stringFile):
    wordDict = dict()
    # Read string from file and replace all common symbols with empty string and separate words connected by hyphens
    string = stringFile.read()
    string = string.replace(',', '').replace('.', '').replace(':', '').replace(';', '').replace('-', ' ')

    # Split string into Python list
    stringList = string.split()
    # Word counting algorithm: if matching key already exists, increments value by 1, else initiate a new key with starting value of 1
    for index, item in enumerate(stringList):
        if item.lower() in wordDict.keys():
            wordDict[item.lower()] += 1
        else:
            wordDict[item.lower()] = 1
    
    # First sort alphabetically and convert key-value pair to tuple, then sort based on occurrences
    sortDict = sorted(wordDict.items(), key=lambda x: x[0])
    sortDict = sorted(sortDict, key=lambda x: (-x[1], x[0]))
    sortList = list()

    # Count length of string in words for percentage calculation
    counter = len(stringList)

    # Convert tuples to list and append percentage values for each occurence
    for item in sortDict:
        item = list(item)
        rawPercentage = np.round((item[1] / counter) * 100, decimals=3)
        item.append(str(rawPercentage) + '%')
        sortList.append(item)
    return sortList


# %%
testFile = open("text_file/text.txt")
countString = hitung_kata(testFile)
print(tabulate(countString, headers=['Word', 'Occurence', '% of String']))

#Given a list, write a Python program to swap first and last element of the list.

#Examples:

#Input : [12, 35, 9, 56, 24]
#Output : [24, 35, 9, 56, 12]
def swapList(newList):
    size = len(newList)
    newList[0],newList[-1]=[newList[-1],newList[0]]
    return newList


# Driver code
newList = [12, 35, 9, 56, 24]

print(swapList(newList))
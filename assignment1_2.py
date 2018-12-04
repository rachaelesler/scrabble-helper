"""
Author: 27799964
Accepts a query string as input, then outputs all words in the dictionary that can be made using all letters in the
query string.
Complexity requirement: O(klogN + W) for time, note string comparison takes O(k) time.
"""

from assignment1_1 import generateKeyList
from assignment1_1 import sortWord


def binarySearch(key, dictList):
    """
    Returns an index corresponding to one instance of key in dictList; returns -1 if key not found.
    :param key:
    :param dictList:
    :return:
    """
    # Use binary search to find an instance of key
    lo = 0
    hi = len(dictList) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if dictList[mid][1] == key:
            return mid
        elif dictList[mid][1] < key:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

def getScrabbleWords(query, dictList):
    """
    Finds and prints all anagrams in dictList that can be made using the letters in the query string.
    Args:
        query (str): word that the program will find anagrams for
        dictList (list): list of (word, key) pairs; each word corresponds to a dictionary word, while each key is the
        same letters in the word, sorted in alphabetical order.
    Time complexity:

    Space complexity:

    """
    query = query.lower()
    key = sortWord(query)
    foundIndex = binarySearch(key, dictList)
    scrabbleWords = []

    if foundIndex == -1:
        print('No words found matching the query string.')
        return
    else:
        scrabbleWords.append(dictList[foundIndex][0])
        # Iterate backwards from foundIndex, adding
        temp = foundIndex - 1
        while temp != 0 and dictList[temp][1] == key:
            scrabbleWords.append(dictList[temp][0])
            temp -= 1

    # for i in range(len(dictList)):
    #     if key == dictList[i][1]:
    #         print(dictList[i][0])
    #         if key != dictList[i+1][1]:     # Exit loop early if sequence of matching anagrams is broken
    #             return


if __name__ == "__main__":
    # Get name of text file and read data into list
    print("Enter the name of your text file.")
    textFile = input("(If the file does not exist, the default dictionary will be used.)\n")
    try:
        dictionary = generateKeyList(textFile)
    except FileNotFoundError:
        dictionary = generateKeyList()

    quit = False
    while not quit:
        query = input("\nEnter your query string: ")
        if query == "***":
            quit = True
        else:
            getScrabbleWords(query, dictionary)

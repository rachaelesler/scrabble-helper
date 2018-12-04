"""
Author: 27799964
Prints all words in the dictionary that can be made using all letters in the query string and one wildcard tile which
can be any letter.
"""

from assignment1_1 import generateKeyList
from assignment1_1 import sortWord


def getWildCardWords(query, dictList):
    """
    Prints all words in dictList that can be made using all letters in the query string and one wildcard tile which
    can be any letter.
    Args:
        query (str): word that the program will find anagrams for, including one wildcard character
        dictList (list): list of (word, key) pairs; each word corresponds to a dictionary word, while each key is the
        same letters in the word, sorted in alphabetical order.
    Time complexity:

    """

    query = query.lower()
    output = []

    for i in range(26):
        wildcard = chr(ord('a') + i)
        query += wildcard
        key = sortWord(query)

        # Fix this up so it is binary search and not linear search
        for j in range(len(dictList)):
            if key == dictList[j][1]:
                output.append(dictList[j][0])
        query = query[:-1]

    # Sort words in output, using radix sort


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
            getWildCardWords(query, dictionary)



"""
Author: 27799964
A Python program used to assist players in games of 'Scrabble' by printing anagrams for input query strings.
"""


def sortWord(word):
    """Sorts the letters in a word in alphabetical order using counting sort.
    Args:
        word (str): must consist of only alphabetical characters.
    Returns:
        output (str): letters of input word sorted in alphabetical order.
    """
    m = len(word)
    count = [0]*26
    output = ''
    for i in range(m):
        count[ord(word[i]) - 97] += 1
    for j in range(26):
        for k in range(count[j]):
            output += chr(j + 97)
    return output


def maxWordLength(dictList):
    """Returns the maximum word length from a list of [word, key] pairs.
    """
    # Find max word length
    maxLength = 0
    for i in range(len(dictList)):
        if len(dictList[i][0]) > maxLength:
            maxLength = len(dictList[i][0])
    return maxLength


def generateKeyList(fname="Dictionary.txt"):
    """Reads the words from file fname, formatting them appropriately. Produces a new array called output such that
    output[i] is the ordered pair (i-th word, key) where the key is the letters in the word, sorted alphabetically. The
    ordered pair is formatted as an array. The list is sorted using radix sort alphabetically by key. The sorted list
    is returned.
    Args:
        fname (str): name of text file containing a list of dictionary words.
    Returns:
        output (list): contains a list of ordered pairs where the first item of each ordered pair corresponds to a
        dictionary word; the second item of each ordered pair is the same word with its letters sorted alphabetically.
    """
    # Open file and read items from file into 'output' list.
    f = open(fname, 'r')
    dictList = []
    for word in f:
        w = word.strip('\n')  # Remove \n at end of each dictionary word
        w = w.lower()
        key = sortWord(w)  # As each word is read, sort the letters in the word alphabetically and store in key
        dictList.append([w, key])  # Each item in the list contains the word and its key.

    # Sort words in list by key, using radix sort
    maxLength = maxWordLength(dictList)
    for i in range(maxLength - 1, -1, -1):  # i represents the current column of letters we are looking out
        output = []
        count = []  # Initialise new count for each 'column' of letters we are examining
        for k in range(27):
            count.append([0])
        for j in range(len(dictList)):
            currentKey = dictList[j][1]
            if len(currentKey) <= i:
                index = 0
            else:
                index = ord(currentKey[i]) - 96
            count[index].append(dictList[j])
            count[index][0] += 1

        # Append each item from count to output
        for i in range(27):  # Iterates through each 'row' of count list
            for j in range(1, count[i][0]):
                output.append(count[i][j])
        dictList = output

    return output


def largestAnagram(dictList):
    """
    Takes as input the name (fname) of a dictionary file and prints all members of the largest set of anagrams in the
    dictionary.
    Args:
        fname (str): file name of text file containing dictionary data
    """

    # Find longest anagram
    prev = dictList[0][1]
    currentAnagrams = [dictList[0][0]]
    longestAnagrams = [dictList[0][0]]

    # Iterate through items in sortOutput from index 1 to end
    for i in range(1, len(dictList)):
        current = dictList[i][1]
        if current == prev:     # Check if current key same as previous key
            currentAnagrams.append(dictList[i][0])
        else:
            if len(currentAnagrams) >= len(longestAnagrams):    # Update longestAnagrams if necessary
                longestAnagrams = currentAnagrams.copy()
            currentAnagrams = [current]
        prev = current

    # Print result
    print("The longest group of anagrams: ", end="")
    for i in range(len(longestAnagrams)-1):
        print(str(longestAnagrams[i]) + " ", end="")
    print(longestAnagrams[-1], end="\n")


def binarySearch(target, dictList):
    """
    Returns an index corresponding to the first found instance of target in dictList; returns -1 if key not found.
    Args:
        target (str): a query string with its letters sorted in alphabetical order
        dictList (list): list of [word, key] pairs; each word corresponds to a dictionary word, while each key is the
        same letters in the word, sorted in alphabetical order.
    Returns:
        Index of target if found in dictList; -1 otherwise.
    """
    # Use binary search to find an instance of key
    lo = 0
    hi = len(dictList) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if dictList[mid][1] == target:   # Returns index of first found instance of query
            return mid
        elif target < dictList[mid][1]:
            hi = mid - 1
        else:
            lo = mid + 1
    return -1   # Executes if query not found in dictList


def radixSortAlphabetical(aList):
    """
    Takes as input a list of strings. Returns the same list of strings sorted alphabetically. Uses radix sort.

    """
    if aList == []:
        return aList
    # Sort words in list by key, using radix sort
    n = len(aList[0])   # number of letters in each word
    for i in range(n - 1, -1, -1):  # i represents the current column of letters we are looking at
        output = []
        count = []  # Initialise new count each time we look at a new letter
        for k in range(27):
            count.append([0])
        for j in range(len(aList)):
            index = ord(aList[j][i]) - 96   # Gives a number that represents what letter we are looking at
            count[index].append(aList[j])
            count[index][0] += 1

        # Append each item from count to output
        for x in range(len(count)):  # Iterates through each 'row' of count list
            for y in range(1, len(count[x])):   # Iterate through each entry at current row of count
                output.append(count[x][y])
        aList = output

    return output


def getScrabbleWords(query, dictList):
    """
    Finds and prints all anagrams in dictList that can be made using the letters in the query string.
    Args:
        query (str): word that the program will find anagrams for
        dictList (list): list of (word, key) pairs; each word corresponds to a dictionary word, while each key is the
        same letters in the word, sorted in alphabetical order.
    """
    query = query.lower()
    key = sortWord(query)
    foundIndex = binarySearch(key, dictList)
    scrabbleWords = []

    if foundIndex == -1:
        output = []
    else:
        scrabbleWords.append(dictList[foundIndex][0])
        temp = foundIndex - 1

        # Iterate backwards from foundIndex
        # Stop iterating when end of list is reached; or when current word does not match query
        while temp != 0 and dictList[temp][1] == key:
            scrabbleWords.append(dictList[temp][0])
            temp -= 1
        temp = foundIndex + 1

        # Iterate forwards from foundIndex
        # Stop iterating when end of list is reached; or when current word does not match query
        while temp <= len(dictList) and dictList[temp][1] == key:
            scrabbleWords.append(dictList[temp][0])  # if a word matching the query key is found append to scrabbleWords
            temp += 1

        # Sort scrabbleWords list alphabetically
        output = radixSortAlphabetical(scrabbleWords)

    print('Words without using a wildcard: ', end='')
    for i in range(len(output)):
        print(str(output[i]) + " ", end="")


def getWildCardWords(query, dictList):
    """
    Prints all words in dictList that can be made using all letters in the query string and one wildcard tile which
    can be any letter.
    Args:
        query (str): word that the program will find anagrams for, including one wildcard character
        dictList (list): list of (word, key) pairs; each word corresponds to a dictionary word, while each key is the
        same letters in the word, sorted in alphabetical order.
    """
    query = query.lower()
    original = query
    output = []

    for i in range(26):
        wildcard = chr(ord('a') + i)
        query = original + wildcard
        key = sortWord(query)

        foundIndex = binarySearch(key, dictList)

        if foundIndex == -1:
            pass
        else:
            output.append(dictList[foundIndex][0])
            temp = foundIndex - 1

            # Iterate backwards from foundIndex
            # Stop iterating when end of list is reached; or when current word does not match query
            while temp != 0 and dictList[temp][1] == key:
                output.append(dictList[temp][0])
                temp -= 1
            temp = foundIndex + 1

            # Iterate forwards from foundIndex
            # Stop iterating when end of list is reached; or when current word does not match query
            while temp <= len(dictList) and dictList[temp][1] == key:
                output.append(dictList[temp][0])  # if a word matching the query key is found append to scrabbleWords
                temp += 1

    # Sort words in output alphabetically
    output = radixSortAlphabetical(output)
    print("\nWords using a wildcard: ", end="")
    for i in range(len(output)):
        print(output[i], end=" ")


if __name__ == "__main__":
    dictList = generateKeyList()
    largestAnagram(dictList)
    print("\n")
    quit = False
    while not quit:
        query = input('Enter the query string: ')
        if query == "***":
            quit = True
        else:
            print()
            getScrabbleWords(query, dictList)
            getWildCardWords(query, dictList)
            print("\n")

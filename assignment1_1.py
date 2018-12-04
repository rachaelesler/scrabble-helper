"""
Author: 27799964
A Python program that prints the largest group of anagrams in the file "Dictionary.txt".
"""

def sortWord(word):
    """Sorts the letters in a word in alphabetical order using counting sort.
    Args:
        word (str): must consist of only alphabetical characters.
    Returns:
        output (str): letters of input word sorted in alphabetical order.
    Time complexity:
        Worst case O(k) where k is the length of the input word
    Space complexity:
        Worst case O(k)
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


def generateKeyList(fname="Dictionary.txt"):
    """Reads the words from file fname, formatting them appropriately. Produces a new array called output such that
    output[i] is the ordered pair [i-th word, key] where the key is the letters in the word, sorted alphabetically.
    Args:
        fname (str): name of text file containing a list of dictionary words.
    Returns:
        output (list): contains a list of ordered pairs where the first item of each ordered pair corresponds to a
        dictionary word; the second item of each ordered pair is the same word with its letters sorted alphabetically.
    Time complexity:
        Worst case O(N*k) where N is the number of words in fname, k is length of longest word.
    Space complexity:
        Worst case O(N)
    """
    # Open file and read items from file into 'output' list.
    f = open(fname, 'r')
    output = []
    for word in f:
        w = word.strip('\n')  # Remove \n at end of each dictionary word
        w = w.lower()
        key = sortWord(w)  # As each word is read, sort the letters in the word alphabetically and store in key variable.
        output.append([w, key])  # Each item in the list contains the word and its key.
    return output


def largestAnagram(fname='Dictionary.txt'):
    """
    Takes as input the name (fname) of a dictionary file and prints all members of the largest set of anagrams in the
    dictionary.
    Args:
        fname (str): file name of text file containing dictionary data
    Time complexity:
        O(k*N) where N is the number of words and k is the length of the longest word in the dictionary
    Space complexity:
        O(N+M) where M is the number of words in the largest set of anagrams.
    """
    dictList = generateKeyList(fname)

    # Find max word length
    maxLength = 0
    for i in range(len(dictList)):
        if len(dictList[i][0]) > maxLength:
            maxLength = len(dictList[i][0])

    # Sort words in list by key, using counting sort
    sortInput = dictList

    for i in range(maxLength-1, -1, -1):   # i represents the current column of letters we are looking out
        sortOutput = []
        count = []  # Initialise new count for each 'column' of letters we are examining
        for k in range(27):
            count.append([0])
        for j in range(len(sortInput)):
            currentKey = sortInput[j][1]
            if len(currentKey) <= i:
                index = 0
            else:
                index = ord(currentKey[i]) - 96
            count[index].append(sortInput[j])
            count[index][0] += 1

        # Append each item from count to output
        for i in range(27): # Iterates through each 'row' of count list
            for j in range(1, count[i][0]):
                sortOutput.append(count[i][j])
        sortInput = sortOutput

    # Find longest anagram
    prev = sortOutput[0][1]
    currentAnagrams = [sortOutput[0][0]]
    longestAnagrams = [sortOutput[0][0]]

    # Iterate through items in sortOutput from index 1 to end
    for i in range(1, len(sortOutput)):
        current = sortOutput[i][1]
        if current == prev:     # Check if current key same as previous key
            currentAnagrams.append(sortOutput[i][0])
        else:
            if len(currentAnagrams) >= len(longestAnagrams):    # Update longestAnagrams if necessary
                longestAnagrams = currentAnagrams.copy()
            currentAnagrams = [current]
        prev = current

    # Print result
    print("The longest group of anagrams in " + fname + " consists of " + str(len(longestAnagrams)) + " words.")
    print("The words are: ", end="")
    anagramStr=""
    for i in range(len(longestAnagrams)-1):
        anagramStr += longestAnagrams[i]
        anagramStr += ", "
    anagramStr += longestAnagrams[-1]
    print(anagramStr)


if __name__ == "__main__":
    print("Enter the name of your text file.")
    textFile = input("(If the file does not exist, the default dictionary will be used.)\n")
    print("Please wait...")
    try:
        largestAnagram(textFile)
    except FileNotFoundError:
        largestAnagram()



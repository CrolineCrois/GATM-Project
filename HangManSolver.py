from collections import Counter

def Matching(knownList, word):
    for x in range(len(knownList)):
        if word[knownList[x][1]] == knownList[x][0]:
            continue
        else:
            return False
    return True

def playHangMan():
    dictionary = open("Dictionary.txt", "r")
    listDict = dictionary.read().splitlines()
    listDict = [word.lower() for word in listDict]
    countList = Counter(listDict)

    oldList = []
    newList = []

    wordsGuessed = []

    print("\n----------\nWelcome to HangMan Solver!!\n")
    print("Please input the word length to start:\n----------\n")

    wordLength = int(input())
    
    for word in listDict:
        if len(word) == wordLength:
            oldList.append(word)

    currentWord = "".join("*" for i in range(wordLength))

    for i in range(26):
        newList = []
        
        if "*" not in currentWord:
            break

        letter = GetMostCommon(oldList, wordsGuessed)
        #(Counter("".join(oldList))).most_common(1)[0] #get rid of alr used letters

        print("\n----------\nSuggested Guess Letter: " + letter + "\n")
        print("Please input the known letters and their position in this form: bonjo*r\n")
        wordsGuessed.append(letter)

        currentWord = input()

        knownPos = []

        for char in currentWord:
            if char == "*":
                continue
            knownPos.append([char, currentWord.index(char.lower())])
        
        for word in oldList:
            if Matching(knownPos, word):
                newList.append(word)

        if len(newList) == 1:
            print("the answer is: " + newList[0] + "!")
            return

        oldList = newList

def GetMostCommon(listt, wordsGuessed):
    c = 1
    currentLetter = (Counter("".join(listt))).most_common(c)[c-1][0]
    while currentLetter in wordsGuessed:
        c += 1
        currentLetter = (Counter("".join(listt))).most_common(c)[c-1][0]
        if currentLetter not in wordsGuessed:
            break
    return(currentLetter)

playHangMan()






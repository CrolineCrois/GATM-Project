from collections import Counter

dictionary = open("Dictionary.txt", "r")
listDict = dictionary.read().splitlines()
listDict = [word.lower() for word in listDict]
countList = Counter(listDict)

print("\n----------\nWelcome to Snowman Solver!!\n")
print("Please input the word length to start:\n----------\n")

wordLength = int(input())

currentWord = "".join("*" for i in range(wordLength))

currentList = []

for word in listDict:
    if len(word) == wordLength + 1:
        currentList.append(word)

def Matching(knownList, word):
    for i in range(len(knownList)):
        if word[i] == knownList[i][1]:
            continue
        else:
            return false
    return true

for i in range(26):
    
    if "*" not in currentWord:
        break

    letter, counts = countList.most_common(1)[0]

    print("\n----------\nSuggested Guess Letter: " + letter + "\n")
    print("Please input the known letters and their position in this form: hell*\n")

    currentWord = input()

    knownPos = []

    for char in currentWord:
        if char == "*":
            continue
        knownPos.append((char, currentWord.index(char.lower())))

    print(knownPos)
    break







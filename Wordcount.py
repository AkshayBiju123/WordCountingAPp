def countWordsFromFile():
    fileName = input('what file do you want to open?')
    NumberOfWords = 0
    file = open(fileName, 'r')
 
    for line in file:
        words = line.split()
        NumberOfWords = NumberOfWords + len(words)
    print('Word Count is')
    print(NumberOfWords)

countWordsFromFile()
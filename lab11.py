
def createWordList(filename):
    text_file= open(filename,"r")
    temp = text_file.read().split("\n")
    text_file.close()
    temp.pop() #remove the last new line
    return temp


def canWeMakeIt(myWord, myLetters):
    listLetters=[]
    for letter in myLetters:
        listLetters.append (letter)
    for x in myWord:
        if x not in listLetters:
            return False
    else:
        return True
    
def specificLength(s,l):
    result = []
    if l == 1:
        for c in s:
            result.append(c)
        return result
    
    for c in s:
        words = specificLength(s.replace(c,'',1), l-1)
        for w in words:
            result.append(w+c)
    return result

def makeCandidates(s):
    wordSet=set()
    for a in range(1,len(s)):
        word= specificLength(s,a)
        for x in word:
            wordSet.add(x)
    return wordSet

def wordList(s):
    list1=makeCandidates(s)
    list2=createWordList("wordlist.txt")
    list3=[]
    for a in list1:
        if a in list2:
            list3.append(a)
    return list3
    
    
def getWordPoints(myWord):
    letterPoints = {'a':1, 'b':3, 'c':3, 'd':2, 'e':1, 'f':4,\
                'g':2, 'h':4, 'i':1, 'j':8, 'k':5, 'l':1,\
                'm':3, 'n':1, 'o':1, 'p':3, 'q':10, 'r':1,\
                's':1, 't':1, 'u':1, 'v':4,  'w':4, 'x':8,\
                'y':4, 'z':10}
    result=0
    for letter in myWord:
        result=result+letterPoints[letter]
    return result

def scrabbleWords(myLetters):
    list1=wordList(myLetters)
    lst=list()
    for word in list1:
        point=getWordPoints(word)
        lst.append((point,word))
    lst.sort(reverse=True)
    result=[]
    for point,word in lst:
        result.append([point,word])
    return result



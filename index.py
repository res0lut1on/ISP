from __future__ import barry_as_FLUFL
from cgitb import strong
from collections import Counter
from re import S

def deleteLastSymbolIfHeNotALetter(letter):
    if(97 <= ord(letter[-1]) <= 122 or 65 <= ord(letter[-1]) <=90):
        return letter
    return letter[:-1]

def checkEqual(listik, word):
    for wordInList in listik:
        if(wordInList == word):
            return True
    return False

def amount(str):
    text = str.split()
    for i in range(len(text)):
        text[i] = deleteLastSymbolIfHeNotALetter(text[i])
        print(text[i])
    print()
    listCheck = []
    for wordInText in text:
        counter = 0
        if(checkEqual(listCheck, wordInText) == False):
            for item in text:
                if(item == wordInText):
                    counter+=1
            print(f"{wordInText} — {counter}")
            listCheck.append(wordInText) 

def amountDict(str):
    text = str.split()
    for i in range(len(text)):
        text[i] = deleteLastSymbolIfHeNotALetter(text[i])
    dictText = dict()
    for i in range(len(text)):
        dictText[text[i]] = 0
    for wordInText in text:
        if(dictText[wordInText] == 0):
            for item in text:
                if(item == wordInText):
                    dictText[wordInText]+=1
            print(f"{wordInText} — {dictText[wordInText]}")

def amountDict2(str):
    text = str.split()
    i = 0
    amountSentence = 0
    try:
        while i >= 0:
            if(text[i][-1] == '.' or text[i][-1] == '?' or text[i][-1] == '!' or text[i][-1] == ';'):
                amountSentence+=1
            i+=1
    except:
        print(len(text)/amountSentence)

def amountDict3(str):
    text = str.replace('?', '.').replace('!', '.').replace('...', '.')
    l = text.split(' ')
    c = text.count('.')
    print(len(l)/c)

def checkDict(dictNgram, str):
    for item in dictNgram:
        if(item == str):
            return False
    return True


def amountDict4(str, n, k):
    text = str.split()
    saveString = str.split()
    for i in range(len(text)):
        text[i] = deleteLastSymbolIfHeNotALetter(text[i])
    i = 0
    dictNgram = dict()
    while text != []:
        if(n <= len(text[i])):
            for startingIndex in range(len(text[i]) + 1 - n):
                str = ""
                for j in range(startingIndex, startingIndex + n):
                    str+=text[i][j]
                if(checkDict(dictNgram, str)):
                    dictNgram[str] = 1
                else:
                    dictNgram[str]+=1          
        text.remove(text[i])
    list_d = sorted(dictNgram.values())
    sorted(dictNgram.values())
    print(list_d)


    
amountDict4("abcde abcdecdedr", 3, 10)
text = 'ti pidoras 1, a ti, ne ya? ya.'
text1 = 'В этом примере Python мы прочитаем текстовый файл с несколькими строками и подсчитаете количество слов в нем. Рассмотрим следующий текстовый файл.'

#print(type(words))
#print(len(words))


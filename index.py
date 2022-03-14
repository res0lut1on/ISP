from __future__ import barry_as_FLUFL
from cgitb import strong
from collections import Counter
from statistics import median
from tracemalloc import start

def mainMed():
    with open("input.txt") as f:
        print(median([len(sentence.split()) for sentence in f.read().split(".")]))
 
#if __name__ == "__main__":
def amountNull(stroka):
    def checkLiteral(letter):
        if(97 <= ord(letter) <= 122 or 65 <= ord(letter) <=90):
            return 1
        return 0
    wordsCollection = stroka.split()
    for item in wordsCollection:
        amount = 0
        CheckingWord = ""
        for i in len(stroka):
            if(checkLiteral(stroka[i])):
                CheckingWord+=stroka[i]
            else:
                if(CheckingWord == item):
                    amount+=1


        print(f"{item} — {stroka.count(item)}")
    print()

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

text = 'ti pidoras 1, a ti, ne ya? ya.'
text1 = 'В этом примере Python мы прочитаем текстовый файл с несколькими строками и подсчитаете количество слов в нем. Рассмотрим следующий текстовый файл.'
str = text1.split_text([text[1]])

#print(type(words))
#print(len(words))


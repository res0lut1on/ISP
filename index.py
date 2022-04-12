

def deleteLastSymbolIfHeNotALetter(letter):
    if(97 <= ord(letter[-1]) <= 122 or 
            65 <= ord(letter[-1]) <= 90):
        return letter
    return letter[:-1]

def checkDict(dictNgram, str):
    for item in dictNgram:
        if(item == str):
            return False
    return True

def amountDict(str):
    text = str.split()
    for i in range(len(text)):
        text[i] = deleteLastSymbolIfHeNotALetter(text[i])
    dictText = dict()
    for i in range(len(text)):
        dictText[text[i]] = 0
        
    print(" How many times rpt word:")
    for wordInText in text:
        if(dictText[wordInText] == 0):
            for item in text:
                if(item == wordInText):
                    dictText[wordInText] += 1
            print(f"{wordInText} — {dictText[wordInText]}")

def amountDict2(str, k):
    text = str.split()
    i = 0
    amountSentence = 0
    try:
        while i >= 0:
            if(text[i][-1] == '.' or 
                    text[i][-1] == '?' or 
                    text[i][-1] == '!' or 
                    text[i][-1] == ';'):
                amountSentence+=1
            i+=1
    except:
        if( k == 1):
            print(f"Average number of words in a sentence — {len(text)/(amountSentence+1)}")
        else:
            answer = len(text)/(amountSentence)
            return answer #+1 

def amountDict3(str):
    text = str.split()
    i = 0
    sentenceDict = dict()
    newSentence = ""
    amountSentence = 0
    try:
        while i >= 0:
            newSentence+= text[i]
            if(text[i][-1] == '.' or 
                    text[i][-1] == '?' or
                    text[i][-1] == '!' or 
                    text[i][-1] == ';'):
                amountSentence += 1
                sentenceDict[amountSentence] = newSentence
                newSentence =""
            i+=1
            newSentence+=" "
    except:
        print(f"Total sentence  — {amountSentence + 1}")

    try:
        if(amountSentence % 2 == 0):
            answer = (amountDict2(sentenceDict[amountSentence / 2], 0) + amountDict2(sentenceDict[amountSentence/2 + 1], 0))/2
            print(f"{answer}")
        else:
            answer = (amountDict2(sentenceDict[(amountSentence + 1)/2], 0))
            print(f"{answer}")
    except:
        print("0")

def amountDict4(str, n, k):
    text = str.split()
    saveString = str.split()
    for i in range(len(text)):
        text[i] = deleteLastSymbolIfHeNotALetter(text[i])
        
    dictNgram = dict()
    i = 0
    while text != []:
        if(n <= len(text[i])):
            for startingIndex in range(len(text[i]) + 1 - n):
                str = ""
                for j in range(startingIndex, startingIndex + n):
                    str+=text[i][j]
                if(checkDict(dictNgram, str)):
                    dictNgram[str] = 1
                else:
                    dictNgram[str] += 1          
        text.remove(text[i])
    for item in dictNgram:
        text.append(item)

    list_d = sorted(dictNgram.values())
    sortDictNgram = dict()
    for i in range(-1, -len(list_d), -1):
        beginNewIteration = 0
        while beginNewIteration != dictNgram[text[-1]]:
            beginNewIteration = 0
            for item  in range(beginNewIteration, len(text), 1):
                if(list_d[i] == dictNgram[text[item]]):
                    sortDictNgram[text[item]] = list_d[i]
                    beginNewIteration = dictNgram[text[item]]
                    del dictNgram[text[item]]
                    text.remove(text[item])
                    break
                beginNewIteration = dictNgram[text[item]]

    init = 0
    print(f"Top {k} most poplura Ngrm... ")
    for i in sortDictNgram:
        if(init >= k):
            break
        print(f"{sortDictNgram[i]} — {i}")
        init+=1
    
def main_():
    text = '''Сan also be used for sequences of words or almost any type of data. 
              For example, they have been used for extracting features. 
              for clustering large sets of satellite earth images? 
              and for determining what part of the Earth. 
              a particular image came from.'''
    text1 = "Fuck fuck. Fuck fuck fuck fuck fuck. Fuck."
    text2 = '''Taxi dispatcher to the client: Get out in 5 minutes. 
                    Mazda is waiting for you, metallic blue. 
                    Further, according to the driver: 
                    A woman comes out of the entrance. 
                    She walked around the car 2 times, 
                    approached the ajar window and asked 
                    Are you blue Vitalik?'''
    command = input("Empty?, Text, Spam, Small text ")
    
    n = int(input("n for Ngram, n = ")) 
    k = int(input("k for Top, k = "))
    finalChoice = ""
    match command.split():
        case["1"]:
            finalChoice = ""
        case["2"]:
            finalChoice = text2
        case["3"]:
            finalChoice = text1
        case["4"]:
            finalChoice = text
    amountDict(finalChoice)
    print()
    amountDict2(finalChoice, 1)
    print()
    amountDict3(finalChoice)
    print()
    amountDict4(finalChoice, n, k)

main_()

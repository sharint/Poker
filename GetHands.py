def sortingHand(hand):
    hand = list(hand)
    newHand = []
    for i in range(0,len(hand),2):
        if hand[i] == 'A':
            hand[i] = '14'
        if hand[i] == 'K':
            hand[i] = '13'
        if hand[i] == 'Q':
            hand[i] = '12'
        if hand[i] == 'J':
            hand[i] = '11'
        if hand[i] == 'T':
            hand[i] = '10'
    for i in range(1,len(hand),2):
        if hand[i] == 'c':
            hand[i] = '0'
        if hand[i] == 'd':
            hand[i] = '1'
        if hand[i] == 'h':
            hand[i] = '2'
        if hand[i] == 's':
            hand[i] = '3'
            
    for i in range(0,len(hand),2):
        newHand.append(int(hand[i]+hand[i+1]))
        
    newHand.sort(reverse = True)
    strNewHand = []
    
    for i in range(len(newHand)):
        second = str(newHand[i])[-1]
        first = str(newHand[i])[0:len(str(newHand[i]))-1]
        strNewHand.append(first)
        strNewHand.append(second)

    for i in range(0,len(strNewHand),2):
        if strNewHand[i] == '14':
            strNewHand[i] = 'A'
        if strNewHand[i] == '13':
            strNewHand[i] = 'K'
        if strNewHand[i] == '12':
            strNewHand[i] = 'Q'
        if strNewHand[i] == '11':
            strNewHand[i] = 'J'
        if strNewHand[i] == '10':
            strNewHand[i] = 'T'
    for i in range(1,len(strNewHand),2):
        if strNewHand[i] == '0':
            strNewHand[i] = 'c'
        if strNewHand[i] == '1':
            strNewHand[i] = 'd'
        if strNewHand[i] == '2':
            strNewHand[i] = 'h'
        if strNewHand[i] == '3':
            strNewHand[i] = 's'
            
    res = ''
    for elem in strNewHand:
        res+=elem
    return res

def readTxt(num):
    f = open('_per/'+str(num)+'%.txt','r')
    mas = []
    while True:
        # считываем строку
        line = f.readline()
        # прерываем цикл, если строка пустая
        line = line.split()
        for i in range(len(line)):
            mas.append(line[i])
        if not line:
            return mas

def isHandIn(mas,hand):
    for i in range(len(mas)):
        if hand == mas[i]:
            return True
    return False

def calcRank(hand):
    for i in range(1,101,1):
        mas = readTxt(i)
        if isHandIn(mas,hand):
            return i

def getRank(hand):
    hand = sortingHand(hand)
    rank = calcRank(hand)
    return rank

#hand = '7d8sAdAsKh'
#print(getRank(hand))
# c = 0 s = 1 h = 2 d = 3
# s h d c
# s > h | s > d | s > c | h > d | h > c | d > c |
# s > c | d > c | s > h | h > c | s > d | h > d |

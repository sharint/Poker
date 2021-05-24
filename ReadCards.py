from PIL import Image, ImageChops
import pyautogui
import os
import time
import keyboard
import WindowController as wc
import threading
import GetHands

class KeyboardChecking (threading.Thread):
    def __init__(self, name, counter):
        threading.Thread.__init__(self)
        self.threadID =  ''
        self.name = name
        self.counter = counter
    def run(self):
        while True:  # making a loop
            try:  # used try so that if user pressed other than the given key error will not be shown
                if keyboard.is_pressed('f10'):  # if key 'F10' is pressed 
                    print('You Pressed A Key!')
                    windowCount = wc.mainSet()
                    autoFindCards(3)
                    time.sleep(0.1)
                    continue  # finishing the loop
                else:
                    pass
            except:
                pass  # if user

class ScanCards(threading.Thread):
    def __init__(self, name, counter):
        threading.Thread.__init__(self)
        self.threadID =  ''
        self.name = name
        self.counter = counter
    def run(self):
        i = self.counter
        writeOutputData('Готов к работе' ,i)
        while True:
            if i > 1:
                cardsRegion = ((580*(i-2))+2244,830,130,50)
                checkRegion = ((580*(i-2))+2350,875,25,30)
                #checkRegion = ((580*(i-2))+2364,840,20,10)
            else:
                cardsRegion = ((580*(i+1))+320,830,130,50)
                checkRegion = ((580*(i+1))+425,875,45,25)
                #checkRegion = ((580*(i+1))+440,840,20,10)
            if checkOnChange(image[i],checkRegion):
                print("Жду следующей раздачи ",i)
                time.sleep(1)
                continue
            writeOutputData('Вычисление' ,i)
            hand = findCards(cardsRegion,i)
            hand = printOutput(hand,i)
            image[i] = pyautogui.screenshot('check'+str(i)+'.png',region=checkRegion)
            if isNormalHand(hand):                
                rank = str(GetHands.getRank(hand))
                writeOutputData(hand+'\n'+ rank ,i)
                print(hand, rank ,i,'ranking')
            else:
                print('Карты не найдены',i)
                writeOutputData('Карты\nне найдены' ,i)
                
                
def writeOutputData(data,i):
    f = open('TKoutput'+str(i)+'.txt', 'w')
    f.write(data)
    f.close()

def getAllFilesFromDir(root, files_of_type):
    rv = []
    for cwd, folders, files in os.walk(root):
        for fname in files:
            if os.path.splitext(fname)[1] in files_of_type:
                # key = filename, value = directory of file
                rv.append(root+'/'+fname)
    return rv

def printOutput(handCards,i):
    if len(handCards) < 5:
        #print("Карты не найдены", i)
        return "Карты не найдены"
    else:
        result = ''
        for card in handCards:
            result += card
        print(result,i)
        return result
    
def difference_images(img1, img2):
    result=ImageChops.difference(img1, img2).getbbox()
    if result==None:
        #print(img1,img2,'matches')
        return True
    return False

def isNormalHand(hand):
    if hand == 'Карты не найдены':
        return False
    else:
        return True
    
def autoFindCards(count):
    
    for i in range(count):
        if i > 1:
            checkRegion = ((580*(i-2))-10,840,20,10)
        else:
            checkRegion = ((580*(i+1))-10,840,20,10)
        #checkRegion = ((580*(i-2))+2194,840,15,25)
        image.append(pyautogui.screenshot('check'+str(i)+'.png',region=checkRegion))
  
    readCardsThread = []
    for i in range(count):
        readCardsThread.append(ScanCards("readCards"+str(i), i))
        readCardsThread[i].start()
              
    for i in range(count):
        readCardsThread[i].join()

def findCards(cardsRegion,i):
    currentHand = []
    counterCards = 0
    counter = 0
    for card in allCards:
        if counterCards >= 5:
            break
        if counter >= 48:
            break
        if pyautogui.locateOnScreen(card, confidence=0.90,region = cardsRegion) != None:
            currentHand.append(convertFromPathToName(card))
            counterCards+=1
        counter+=1
    return currentHand

def checkOnChange(image1,checkRegion):
    image2 = pyautogui.screenshot('check.png',region=checkRegion)
    if difference_images(image1,image2):
        return True
    else:
        return False

def convertFromPathToName(card):
    # card = 'AllCards/card.png'
    return card.split('/')[1].split('.')[0]

def start():
    keyboardThread = KeyboardChecking("keyboard", 5)
    keyboardThread.start()
    keyboardThread.join()
    
cardsDirectory = 'AllCards'
imageExtension = '.png'
allCards = getAllFilesFromDir(cardsDirectory,imageExtension)
image = []
            


    

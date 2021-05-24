import win32gui
import pyautogui
import pywinauto
import win32con

def openTables(countTable):
    counter = 0
    mainWindow = True
    while counter < countTable:
        totalWindow = counter
        counter = 0
        winds = []
        windows = pywinauto.findwindows.find_elements()
        for window in windows:
            if 'PPPoker' in window.name:
                winds.append(window.name)
                counter+=1
                if counter > totalWindow:
                    if mainWindow:
                        mainWindow = False
                    else:
                        if counter > 4:
                            region = ((counter-5)*575+1920,0,589,1050)
                        else:
                            region = ((counter-2)*575,0,589,1050)
                        setWindowPosition(window.name,region)
                        print(winds[counter-1],"Передвинул")

def resetWindows():
    counter = 0
    windows = pywinauto.findwindows.find_elements()
        for window in windows:
            if 'PPPoker' in window.name:
                counter+=1
    

def setWindowsAgain():
    windows = pywinauto.findwindows.find_elements()
    boardsWindow = []
    hwnds = []
    for window in windows:
            if 'PPPoker' in window.name:
                boardsWindow.append(window.name)
                hwnd = win32gui.FindWindow(None,window.name)
                hwnds.append(hwnd)
    print(len(boardsWindow))
    if len(boardsWindow) < 3:
        return True
    else:
        counter = 0
        for window in boardsWindow:
            region = (counter*575,0,589,1050)
            setWindowPosition(window,region)
            win32gui.ShowWindow(hwnds[counter], win32con.SW_NORMAL)
            counter+=1
        return False

def getCurrentCountWindow():
    windows = pywinauto.findwindows.find_elements()
    counter = 0
    for window in windows:
            if 'PPPoker' in window.name:
                counter+=1
    return counter


def printWindowPosition(window):
    ''' Window  - PPPoker(38.0):
	Location: (1, 0)
	    Size: (589, 1050)'''
    hwnd = win32gui.FindWindow(None, window)
    rect = win32gui.GetWindowRect(hwnd)
    x = rect[0]
    y = rect[1]
    w = rect[2] - x
    h = rect[3] - y
    print("Window %s:" % win32gui.GetWindowText(hwnd))
    print("\tLocation: (%d, %d)" % (x, y))
    print("\t    Size: (%d, %d)" % (w, h))


def setWindowPosition(window,region):
    x,y,cx,cy = region[0],region[1],region[2],region[3]
    hwnd = win32gui.FindWindow(None, window)
    #print(hwnd)
    if hwnd == 0:
        return False
    else:
        win32gui.SetWindowPos(hwnd,1,x,y,cx,cy,0)
        return True

def setWindowCalc():
    if not setWindowPosition('ProPokerTools Odds Oracle',(1725, 0, 200 ,400)):
        print("Окно не найдено")
        return False
    pyautogui.click(1800, 40)
    pyautogui.click(1800, 70)
    setWindowPosition('Range Explorer',(1725, 0, 200 ,400))
    pyautogui.click(1800, 10)
    pyautogui.click(1900, 220)
    return True

#import time
#while setWindowsAgain():
#    print('Откройте 3 стола')
#    time.sleep(1)

#openTables(6)

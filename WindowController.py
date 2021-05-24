import win32gui

def enumHandler(hwnd, lParam):
    if win32gui.IsWindowVisible(hwnd):
        if 'PPPoker' in win32gui.GetWindowText(hwnd):
            mas.append(hwnd)

def setWindows():
    windowCount = len(mas)
    for i in range(windowCount):
        if i > 2:
            win32gui.MoveWindow(mas[i], 579*(i-3)+1920, 0, 589, 1050, True)
        else:
            win32gui.MoveWindow(mas[i], 579*i, 0, 589, 1050, True)

def mainSet():
    global mas
    mas = []
    win32gui.EnumWindows(enumHandler,None)
    setWindows()
    return len(mas)-1

def checkingCountWindows():
    global mas
    mas = []
    win32gui.EnumWindows(enumHandler,None)
    return len(mas)-1

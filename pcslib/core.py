import pyautogui
import time
import pygetwindow


def focus_pcs():
    pcs_window = pygetwindow.getWindowsWithTitle('PCS Maintenance')
    pcs_window[0].activate()
    pcs_window[0].maximize()

def refresh():
    pyautogui.press('f5')
    time.sleep(1)

def copy():
    pyautogui.press('alt')
    pyautogui.press('p')
    pyautogui.press('y')
    time.sleep(1)

def add():
    pyautogui.press('alt')
    pyautogui.press('p')
    pyautogui.press('a')
    time.sleep(1)

def delete():
    pyautogui.press('alt')
    pyautogui.press('p')
    pyautogui.press('d')
    pyautogui.press('enter')
    time.sleep(1)

def ok():
    pyautogui.press('alt')
    pyautogui.press('p')
    pyautogui.press('o')
    time.sleep(1)

def back(i = 1):
    for _ in range(i):
        pyautogui.press('alt')
        pyautogui.press('f')
        pyautogui.press('c')
        time.sleep(1)

def tab(i = 1):
    for _ in range(i):
        pyautogui.press('tab')

def close():
    pyautogui.press('alt')
    pyautogui.press('c')
    time.sleep(1)

def options():
    pyautogui.press('alt')
    pyautogui.press('s')
    #might need to add wait here
    pyautogui.press('o')
    time.sleep(1)

#Usable inside of Options screen
def price():
    pyautogui.press('alt')
    pyautogui.press('s')
    pyautogui.press('i')
    time.sleep(1)

def xcomp():
    pyautogui.press('alt')
    pyautogui.press('s')
    pyautogui.press('c')
    time.sleep(1)

def long_desc():
    pyautogui.press('alt')
    pyautogui.press('s')
    pyautogui.press('l')
    time.sleep(1)

def paint_group():
    pyautogui.press('alt')
    pyautogui.press('s')
    pyautogui.press('g')
    time.sleep(1)
#End of Options Screen


def select_model(model_code, year, down = 1):
    pyautogui.write(model_code)
    tab(2)
    pyautogui.write(year)
    refresh()
    tab(4)
    for _ in range(down):
        pyautogui.press('down')
    options()

def select_option(option):
    pyautogui.write(option)
    refresh()

def add_price(invoice, msrp, differential = False):
    price()
    add()
    tab()
    pyautogui.write(invoice)
    tab()
    pyautogui.write(msrp)
    if differential:
        tab()
        pyautogui.press('down')
        pyautogui.press('down')
    pyautogui.press('enter')
    time.sleep(1)
    back()


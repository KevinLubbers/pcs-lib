import pyautogui
import time
import pygetwindow
import pyperclip


def focus_pcs():
    pcs_window = pygetwindow.getWindowsWithTitle('PCS Maintenance')
    pcs_window[0].activate()
    pcs_window[0].maximize()

#Start Basic Building Block Functions
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

def back_reset():
    for _ in range(6):
        pyautogui.hotkey('shift' , 'tab')
    time.sleep(1)
def option_back_reset():
    for _ in range(7):
        pyautogui.hotkey('shift' , 'tab')
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
    time.sleep(1)
    pyautogui.press('o')
    time.sleep(1)
#end Basic Building Blocks


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

#Start ACTION Functions
def select_model(model_code, year, down = 1):
    pyautogui.write(model_code)
    tab(2)
    pyautogui.write(year)
    refresh()
    tab(4)
    for _ in range(down):
        pyautogui.press('down')
    #check = check_model(model_code)
    options()
    

def check_model(model_code):
    for _ in range(4):
        pyautogui.press('right')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(2)
    copy_model = pyperclip.paste().strip()
    if model_code != copy_model:
        return False
    else:
        return True



def select_option(option, name, category, invoice, msrp):
    pyautogui.write(option)
    refresh()
    check_option(option, name, category, invoice, msrp)

def check_option(option, name, category, invoice, msrp):
    tab(7)
    for _ in range(1):
        pyautogui.press('right')
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(2)
    copy_option = pyperclip.paste().strip()
    if option != copy_option:
        add_option(option, name, category, invoice, msrp)
    else:
        check_price(invoice, msrp)

def add_option(option, name, category, invoice, msrp):
    
    add()
    pyautogui.write(option)
    tab()
    pyautogui.write(name)
    tab()
    pyautogui.write(category)
    tab()
    pyautogui.write('MFG')
    pyautogui.press('enter')
    time.sleep(2)
    close()
    price()
    tab()
    pyautogui.write(str(invoice))
    tab()
    pyautogui.write(str(msrp))
    pyautogui.press('enter')

    time.sleep(1)



def check_price(invoice, msrp, down = 1):
    price()
    tab(3)
    for _ in range(down):
        pyautogui.press('down')
    for _ in range(4):
        pyautogui.press('right')
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(2)
    copy_invoice = float(pyperclip.paste().strip())
    pyautogui.press('right')
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(2)
    copy_msrp = float(pyperclip.paste().strip())
    if invoice != copy_invoice or msrp != copy_msrp:
        delete()
        add_price(invoice, msrp, True)
    else:
        back()

def add_price(invoice, msrp, correct_screen = False, differential = False):
    #checking if you're already inside price screen or need to go there
    #default acts as if you are on the options screen
    #must
    if not correct_screen:
        price()
    add()
    tab()
    pyautogui.write(str(invoice))
    tab()
    pyautogui.write(str(msrp))
    if differential:
        tab()
        pyautogui.press('down')
        pyautogui.press('down')
    pyautogui.press('enter')
    time.sleep(1)
    back()

def add_price_compare(invoice, msrp, down = 1, differential = False):
    check = check_price(invoice, msrp, down)
    if not check:
        delete()
        add_price(invoice, msrp, True)
    #else do nothing, price is already correct
    back()
    
#End ACTION Functions
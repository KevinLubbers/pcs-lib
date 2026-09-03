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
    pyautogui.hotkey('alt', 'c')
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

def get_all_options():
    tab(7)
    time.sleep(1)
    #highlighting all option codes and names and copying to clipboard
    pyautogui.press('right')
    pyautogui.keyDown('shift')
    pyautogui.press('right')
    pyautogui.press('pagedown')
    pyautogui.press('pagedown')
    pyautogui.press('pagedown')
    pyautogui.press('pagedown')
    pyautogui.keyUp('shift')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(2)
    copy_options = pyperclip.paste().strip()
    lookup = []
    #separate the code and name from the clipboard data
    for line in copy_options.splitlines():
        code, name = line.split(maxsplit=1)
        lookup.append((code, name))
    #reset cursor to option input field
    option_back_reset()
    return lookup
    

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
    
    time.sleep(.5)
    
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

#Same Functions repeated but WITHOUT category and name
#Used for Stellantis PDF Extractor

def stellantis_select_option(option, invoice, msrp, differential = False):
    pyautogui.write(option)
    refresh()
    return stellantis_check_option(option, invoice, msrp, differential)

def stellantis_check_option(option, invoice, msrp, differential = False):
    tab(7)
    for _ in range(1):
        pyautogui.press('right')
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(2)
    copy_option = pyperclip.paste().strip()
    if option != copy_option:
        return False
    else:
        if not differential:
            check_price(invoice, msrp, 0, differential)
        else:
            check_price(invoice, msrp, 1, differential)
#end Stellantis repeated functions

def check_price(invoice, msrp, down = 0, differential = False):
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
        if down == 0:
            delete()
        add_price(invoice, msrp, True, differential)
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
        add_price(invoice, msrp, True, differential)
    #else do nothing, price is already correct
    back()
    


def add_paints(paints):
    pyautogui.write("EXT1")
    refresh()
    paint_group()
    add()
    for paint in paints:
        pyautogui.write(paint)
        pyautogui.press('enter')
        pyautogui.press('enter')
    close()
    back()

def add_interiors(interiors):
    pyautogui.write("INT1")
    refresh()
    paint_group()
    add()
    for interior in interiors:
        pyautogui.write(interior)
        pyautogui.press('enter')
        pyautogui.press('enter')
        time.sleep(1)
    close()
    back()
#End ACTION Functions
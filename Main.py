# coding: utf-8
import win32clipboard
import win32com.client as comclt

def entoar(char):
    if(char == 'Q' or char == 'q'):
        char = 'ض'
        return char
    elif(char == 'W' or char == 'w'):
        char = 'ص'
        return char
    elif (char == 'E' or char == 'e'):
        char = 'ث'
        return char
    elif (char == 'R' or char == 'r'):
        char = 'ق'
        return char
    elif (char == 'T' or char == 't'):
        char = 'ف'
        return char
    elif (char == 'y'):
        char = 'غ'
        return char
    elif (char == 'Y'):
        char == 'إ'
        return char
    elif (char == 'U' or char == 'u'):
        char = 'ع'
        return char
    elif (char == 'I' or char == 'i'):
        char = 'ه'
        return char
    elif (char == 'O' or char == 'o'):
        char = 'خ'
        return char
    elif (char == 'P' or char == 'p'):
        char = 'ح'
        return char
    elif (char == '['):
        char = 'ج'
        return char
    elif (char == ']'):
        char = 'د'
        return char
    elif (char == 'A' or char == 'a'):
        char = 'ش'
        return char
    elif (char == 'S' or char == 's'):
        char = 'س'
        return char
    elif (char == 'D' or char == 'd'):
        char = 'ي'
        return char
    elif (char == 'F' or char == 'f'):
        char = 'ب'
        return char
    elif (char == 'G' or char == 'g'):
        char = 'ل'
        return char
    elif (char == 'H' or char == 'h'):
        char = 'ا'
        return char
    elif (char == 'J' or char == 'j'):
        char = 'ت'
        return char
    elif (char == 'K' or char == 'k'):
        char = 'ن'
        return char
    elif (char == 'L' or char == 'l'):
        char = 'م'
        return char
    elif (char == ':' or char == ';'):
        char = 'ك'
        return char
    elif (char == '"' or char == "'"):
        char = 'ط'
        return char
    elif (char == '`' or char == '~'):
        char = 'ذ'
        return char
    elif (char == 'Z' or char == 'z'):
        char = 'ئ'
        return char
    elif (char == 'X' or char == 'x'):
        char = 'ء'
        return char
    elif (char == 'C' or char == 'c'):
        char = 'ؤ'
        return char
    elif (char == 'V' or char == 'v'):
        char = 'ر'
        return char
    elif (char == 'B' or char == 'b'):
        char = 'لا'
        return char
    elif (char == 'n'):
        char = 'ى'
        return char
    elif(char == 'N'):
        char = 'آ'
        return char
    elif (char == 'M' or char == 'm'):
        char = 'ة'
        return char
    elif (char == '<' or char == ','):
        char = 'و'
        return char
    elif (char == '>' or char == '.'):
        char = 'ز'
        return char
    elif (char == '/'):
        char = 'ظ'
        return char
    elif (char == '?'):
        char = '؟'
        return char
    else:
        return char


def entxtar(text):
    ftxt=""
    for i in text:
        ftxt += entoar(i)
    return ftxt

def getcb():
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData(win32clipboard.CF_UNICODETEXT)
    win32clipboard.CloseClipboard()
    return data


def addcb(text):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardText(text, win32clipboard.CF_UNICODETEXT)
    win32clipboard.CloseClipboard()

# wsh = comclt.Dispatch("WScript.Shell")
# wsh.SendKeys("^c") # ^: Control, +: Shift, %: Alt

print(getcb())

transdata = entxtar(getcb())

addcb(transdata)
# wsh.SendKeys("^v")
print(getcb())

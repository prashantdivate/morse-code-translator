'''
Created By: Prashant Divate
Version 1.0

Supports Text to morse with support of playsound

'''

from playsound import playsound
import time
import pyttsx3 as pyttsx

MORSE_CODE_DICT = { ' ':'/',
                    'A':'.-',
                    'B':'-...',
                    'C':'-.-.',
                    'D':'-..',
                    'E':'.',
                    'F':'..-.',
                    'G':'--.',
                    'H':'....',
                    'I':'..',
                    'J':'.---',
                    'K':'-.-',
                    'L':'.-..',
                    'M':'--',
                    'N':'-.',
                    'O':'---',
                    'P':'.--.',
                    'Q':'--.-',
                    'R':'.-.',
                    'S':'...',
                    'T':'-',
                    'U':'..-',
                    'V':'...-',
                    'W':'.--',
                    'X':'-..-',
                    'Y':'-.--',
                    'Z':'--..',
                    '1':'.----',
                    '2':'..---',
                    '3':'...--',
                    '4':'....-',
                    '5':'.....',
                    '6':'-....',
                    '7':'--...',
                    '8':'---..',
                    '9':'----.',
                    '0':'-----', 
                    ', ':'--..--',
                    '.':'.-.-.-',
                    '?':'..--..',
                    '/':'-..-.',
                    '-':'-....-',
                    '(':'-.--.',
                    ')':'-.--.-'}


def Txt_to_Morse():
    txt = input('Enter Text to Convert to Morse: ')
    code = [MORSE_CODE_DICT[i.upper()] + ' ' for i in txt if i.upper() in MORSE_CODE_DICT.keys()]
    morse=''.join(code)
    print(morse)
    for m in morse:
        if m=='.':
            playsound('resources/dit.wav')
        elif m=='-':
            playsound('resources/dah.wav')
        else:
            time.sleep(0.5)

def Morse_to_Txt():
    txt = input('Enter Morse to Convert to Text: ')
    code = [k for i in txt.split() for k,v in MORSE_CODE_DICT.items() if i==v]
    newtxt = ''.join(code)
    print(newtxt)
    engine = pyttsx.init()
    engine.say(newtxt)
    engine.runAndWait()


print ("   _____                                                .___             ")
print ("  /     \   ___________  ______ ____     ____  ____   __| _/___________  ")
print (" /  \ /  \ /  _ \_  __ \/  ___// __ \  _/ ___\/  _ \ / __ |/ __ \_  __ \ ")
print ("/    Y    (  <_> )  | \/\___ \\  ___/  \  \__(  <_> ) /_/ \  ___/|  | \/ ")
print ("\____|__  /\____/|__|  /____  >\___  >  \___  >____/\____ |\___  >__|    ")
print ("        \/                  \/     \/       \/           \/    \/        ")

print('''\n1 - Convert Text to Morse \n2 - Convert Morse to Text\n3 - Quit\n ''')

while True:
    try:
        selection = int(input('Select Your Choice: '))
        if selection == 1:
            print(Txt_to_Morse())
            break
        elif selection == 2:
            print(Morse_to_Txt())
            break
        elif selection == 3:
            print('Exiting')
            break
        else:
            print('Wrong Selection, enter again')
    except:
        print('Wrong Selection, enter again')

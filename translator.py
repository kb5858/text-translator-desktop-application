from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
from textblob import TextBlob

root = Tk()
root.geometry('600x450')
root.title('Language Translator')
root.resizable(False, False)
root.configure(bg='gold2')

## LANGUAGE DICTIONARY

dict = {'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar', 'armenian': 'hy',
        'azerbaijani': 'az', 'basque': 'eu', 'belarusian': 'be', 'bengali': 'bn', 'bosnian': 'bs',
        'bulgarian': 'bg', 'catalan': 'ca', 'cebuano': 'ceb', 'chichewa': 'ny',
        'chinese (simplified)': 'zh-cn', 'chinese (traditional)': 'zh-tw', 'corsican': 'co', 'croatian': 'hr',
        'czech': 'cs', 'danish': 'da', 'dutch': 'nl', 'english': 'en', 'esperanto': 'eo', 'estonian': 'et',
        'filipino': 'tl', 'finnish': 'fi', 'french': 'fr', 'frisian': 'fy', 'galician': 'gl', 'georgian': 'ka',
        'german': 'de', 'greek': 'el', 'gujarati': 'gu', 'haitian creole': 'ht', 'hausa': 'ha',
        'hawaiian': 'haw', 'hebrew': 'he', 'hindi': 'hi', 'hmong': 'hmn', 'hungarian': 'hu',
        'icelandic': 'is', 'igbo': 'ig', 'indonesian': 'id', 'irish': 'ga', 'italian': 'it', 'japanese': 'ja',
        'javanese': 'jw', 'kannada': 'kn', 'kazakh': 'kk', 'khmer': 'km', 'korean': 'ko',
        'kurdish (kurmanji)': 'ku', 'kyrgyz': 'ky', 'lao': 'lo', 'latin': 'la', 'latvian': 'lv',
        'lithuanian': 'lt', 'luxembourgish': 'lb', 'macedonian': 'mk', 'malagasy': 'mg', 'malay': 'ms',
        'malayalam': 'ml', 'maltese': 'mt', 'maori': 'mi', 'marathi': 'mr', 'mongolian': 'mn',
        'myanmar (burmese)': 'my', 'nepali': 'ne', 'norwegian': 'no', 'odia': 'or', 'pashto': 'ps',
        'persian': 'fa', 'polish': 'pl', 'portuguese': 'pt', 'punjabi': 'pa', 'romanian': 'ro', 'russian':
            'ru', 'samoan': 'sm', 'scots gaelic': 'gd', 'serbian': 'sr', 'sesotho': 'st', 'shona': 'sn',
        'sindhi': 'sd', 'sinhala': 'si', 'slovak': 'sk', 'slovenian': 'sl', 'somali': 'so', 'spanish': 'es',
        'sundanese': 'su', 'swahili': 'sw', 'swedish': 'sv', 'tajik': 'tg', 'tamil': 'ta', 'telugu': 'te',
        'thai': 'th', 'turkish': 'tr', 'ukrainian': 'uk', 'urdu': 'ur', 'uyghur': 'ug', 'uzbek': 'uz',
        'vietnamese': 'vi', 'welsh': 'cy', 'xhosa': 'xh', 'yiddish': 'yi', 'yoruba': 'yo', 'zulu': 'zu'}

## COMBO-BOX  - SCROLL-DOWN-FOR-LANGUAGES

languages = StringVar()
fontbox = Combobox(root, width=30, textvariable=languages, state='readonly')
fontbox['values'] = [e for e in dict.keys()]
fontbox.current(37)
fontbox.place(x=380, y=20)


def display(event=None):
    try:
        text = TextBlob(var1.get())
        lang = text.detect_language()
        lang_dict = languages.get()
        lang_to = dict[lang_dict]
        text = text.translate(from_lang=lang, to=lang_to)
        var2.set(text)
    except:
        var2.set("Try another keyword")


def exit():
    message = messagebox.askyesnocancel('Alert', 'Do u want to exit', parent=root)
    if (message == True):
        root.destroy()


###binding functions####
def enterentry1(e):
    entry1['bg'] = "brown1"


def leaveentry1(e):
    entry1['bg'] = "white"


def enterentry2(e):
    entry2['bg'] = "brown1"


def leaveentry2(e):
    entry2['bg'] = "white"


def enterbtn1(e):
    btn1['bg'] = "coral1"


def leavebtn1(e):
    btn1['bg'] = "khaki4"


def enterbtn2(e):
    btn2['bg'] = "red"


def leavebtn2(e):
    btn2['bg'] = "khaki4"


## ENTRY-BOX

var1 = StringVar()
entry1 = Entry(root, width=30, textvariable=var1, font=('times', 15, 'italic bold'))
entry1.place(x=180, y=80)

var2 = StringVar()
entry2 = Entry(root, width=30, textvariable=var2, font=('times', 15, 'italic bold'))
entry2.place(x=180, y=180)

## LABELS

label1 = Label(root, text='Enter to convert:', font=('times', 15, 'italic bold'), bg='gold2')
label1.place(x=5, y=80)

label2 = Label(root, text='Converted text: ', font=('times', 15, 'italic bold'), bg='gold2')
label2.place(x=5, y=180)

## BUTTONS

btn1 = Button(root, text='Click', bd=5, bg='cyan', activebackground='red', width=10, font=('times', 15,
                                                                                            'italic bold'),
              command=display)
btn1.place(x=100, y=300)

btn2 = Button(root, text='Exit', bd=5, bg='cyan', activebackground='red', width=10, font=('times', 15,
                                                                                           'italic bold'), command=exit)
btn2.place(x=300, y=300)

####binding######

entry1.bind('<Enter>', enterentry1)
entry1.bind('<Leave>', leaveentry1)

entry2.bind('<Enter>', enterentry2)
entry2.bind('<Leave>', leaveentry2)

btn1.bind('<Enter>', enterbtn1)
btn1.bind('<Leave>', leavebtn1)

btn2.bind('<Enter>', enterbtn2)
btn2.bind('<Leave>', leavebtn2)

root.bind('<Return>', display)

root.mainloop()

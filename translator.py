
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
from textblob import TextBlob

root = Tk()
root.geometry('500x400')
root.title('Translator')
root.resizable(True, True)
root.configure(bg='turquoise1')

## LANGUAGE DICTIONARY

lang_dict = {'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar', 'armenian': 'hy',
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
font_box = Combobox(root,width=30,textvariable=languages,state='readonly')
font_box['values'] = [e for e in lang_dict.keys()]
font_box.current(37)
font_box.place(x=300,y=0)

def tt(event=None):
    try:
        word3=TextBlob(varname1.get())
        lan=word3.detect_language()
        lan_todict=languages.get()
        lan_to=lang_dict[lan_todict]
        word3=word3.translate(from_lang=lan,to=lan_to)
        label3.configure(text=word3)
        varname2.set(word3)
    except:
        varname2.set("try another keyword")
    

def main_exit():
    rr=messagebox.askyesnocancel('notification','do u want to exit',parent=root)
    if(rr==True):
        root.destroy()

###binding functions####
def on_enterentry1(e):
    entry1['bg']="spring green"
def on_leaveentry1(e):
    entry1['bg']="white"
def on_enterentry2(e):
    entry2['bg']="spring green"
def on_leaveentry2(e):
    entry2['bg']="white"
def on_enterbtn1(e):
    btn1['bg']="yellow"
def on_leavebtn1(e):
    btn1['bg']="pink"
def on_enterbtn2(e):
    btn2['bg']="yellow"
def on_leavebtn2(e):
    btn2['bg']="pink"


## ENTRY-BOX

varname1 = StringVar()
entry1 = Entry(root,width=30,textvariable=varname1,font=('times', 15, 'italic bold'))
entry1.place(x=150,y=40)

varname2 = StringVar()
entry2 = Entry(root,width=30,textvariable=varname2,font=('times', 15, 'italic bold'))
entry2.place(x=150,y=100)

## LABELS

label1 = Label(root,text='Enter to convert:',font=('times', 15, 'italic bold'),bg='turquoise1')
label1.place(x=5,y=40)

label2 = Label(root,text='Converted : ',font=('times', 15, 'italic bold'),bg='turquoise1')
label2.place(x=5,y=100)

label3 = Label(root,text='',font=('times', 15, 'italic bold'),bg='turquoise1')
label3.place(x=5,y=250)

## BUTTONS

btn1 = Button(root,text='Click',bd=5,bg='white',activebackground='red',width=10,font=('times', 15,
 'italic bold'),command=tt)
btn1.place(x=70,y=170)

btn2 = Button(root,text='Exit',bd=5,bg='white',activebackground='red',width=10,font=('times', 15,
 'italic bold'),command=main_exit)
btn2.place(x=280,y=170)

####binding######
entry1.bind('<Enter>',on_enterentry1)
entry1.bind('<Leave>',on_leaveentry1)

entry2.bind('<Enter>',on_enterentry2)
entry2.bind('<Leave>',on_leaveentry2)

btn1.bind('<Enter>',on_enterbtn1)
btn2.bind('<Leave>',on_leavebtn1)

btn2.bind('<Enter>',on_enterbtn2)
btn2.bind('<Leave>',on_leavebtn2)




root.bind('<Return>',tt)

root.mainloop()
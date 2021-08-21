import wolframalpha
client = wolframalpha.Client("Y4RUJW-62XHEURVAV")

import wikipedia

import PySimpleGUI as sg 
sg.theme('DarkPurple6')
layout =[[sg.Text('Enter a command'), sg.InputText()], [sg.Button('Tell me'), sg.Button('Nothing')]  ]
# Create the Window
window = sg.Window('AI-ex', layout)

import pyttsx3
engine = pyttsx3.init()

while True:
    event, values = window.read()
    if event in (None, 'Nothing'): 
        break
    try:
        wiki_res = wikipedia.summary(values[0], sentences=2)
        wolfram_res = next(client.query(values[0]).results).text
        engine.say(wolfram_res)
        sg.PopupNonBlocking("Wolfram Resul: "+wolfram_res,"Wikipedia Result: "+wiki_res)
    except wikipedia.exceptions.DisambiguationError:
        wolfram_res = next(client.query(values[0]).results).text
        engine.say(wolfram_res)
        sg.PopupNonBlocking(wolfram_res)
    except wikipedia.exceptions.PageError:
        wolfram_res = next(client.query(values[0]).results).text
        engine.say(wolfram_res)
        sg.PopupNonBlocking(wolfram_res)
    except:
        wiki_res = wikipedia.summary(values[0], sentences=2)
        engine.say(wiki_res)
        sg.PopupNonBlocking(wiki_res)

    engine.runAndWait()

    print (values[0])

window.close()
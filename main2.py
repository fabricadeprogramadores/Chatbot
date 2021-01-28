from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import pyttsx3 as pp
from tkinter import *
import os
import speech_recognition as s
import threading

engine = pp.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(word):
    engine.say(word)
    engine.runAndWait()


def take_query():
    sr = s.Recognizer()
    sr.pause_threshold = 1
    print("Seu robo esta esperando você falar")
    with s.Microphone()as m:
        try:
            audio = sr.listen(m)
            query = sr.recognize_google(audio, language='pt-BR')
            print(query)
            questionField.delete(0, END)
            questionField.insert(0, query)
            ask_from_bot()
        except Exception as e:
            print(e)
            # tkinter.messagebox.showerror("Error","Voice not recognized")


def ask_from_bot():
    query = questionField.get()
    answer = bot.get_response(query)
    msglist.insert(END, 'Você: ' + query+'\n\n')
    msglist.insert(END, 'Meu robo: ' + str(answer)+'\n\n')
    speak(answer)

    questionField.delete(0, END)
    msglist.yview(END)


bot=ChatBot('Meu robo')
trainer = ListTrainer(bot)




root = Tk()
root.geometry('500x570+100+30')
root.config(bg='rosybrown2')
root.title("ChatBot criado pela Fábrica de Programadores")

pic = PhotoImage(file='pic.png')
picture_Label = Label(root, image=pic, bg='rosybrown2')
picture_Label.pack(pady=5)
center_Frame = Frame(root)
center_Frame.pack()
scrollbar = Scrollbar(center_Frame)
scrollbar.pack(side=RIGHT, fill=Y)
msglist = Text(center_Frame, width=80,font=('times new roman',20,'bold'), height=10, yscrollcommand=scrollbar.set, bg='grey95', fg='grey2',wrap='word')
msglist.pack(side=LEFT, fill=BOTH)

questionField = Entry(root, font=('verdana',20,'bold'), bg='grey95', fg='grey2',bd=4,relief=GROOVE)
questionField.pack(fill=X, pady=15)
askphoto = PhotoImage(file='ask.png')
btn = Button(root, image=askphoto, font='verdana,25', command=ask_from_bot)
btn.pack()


def enter_function(event):
    btn.invoke()


root.bind('<Return>', enter_function)
close = TRUE


def repeat():
    while True:
        take_query()


t = threading.Thread(target=repeat)
t.setDaemon(True)
t.start()
root.mainloop()
from tkinter import *
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import pyttsx3 as pp
import speech_recognition as s
import tkinter.messagebox
import threading

engine = pp.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(word):
    engine.say(word)
    engine.runAndWait()


bot = ChatBot('Meu robo')

convo = [
    'Ola',
    'tudo bem !',
    'como é seu nome ?',
    'Meu nome é Geraldo e fui criado pela Fábrica de Programadores',
    'Como você está ?',
    'Eu estou bem',
    'Obrigado',
    'Qual a capital do Brasil?',
    'Brasilia é a capital do Brasil',
    'não fale comigo ',
    'eu vou falar com você',
    'Você é inteligente?',
    'Sim, eu sou inteligente',
    'Onde você mora ?',
    'Eu vivo na sua memória ram agora',
     'o que você faz?',
     'Eu faço chat',
     'Você é solteiro ou casado?',
     'Ainda não achei minha memória gemea',

     'Diga algo',
     'Não, você diz algo',

     'Em que idioma você fala?',

     'Eu falo principalmente em Inglês',
     'o que você faz no tempo livre?',
     'Eu memorizo coisas no meu tempo livre',
     'ok tchau, se cuide, vejo você de novo',
     'tchau'

]

trainer = ListTrainer(bot)

trainer.train(convo)


def take_query():
    sr = s.Recognizer()
    sr.pause_threshold = 1
    print("O robo esta aguardando você falar")
    with s.Microphone()as m:
        try:
            print("Escutando")
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
    msglist.insert(END, 'Você: ' + query)
    msglist.insert(END, 'Geraldo: ' + str(answer))
    speak(answer)

    questionField.delete(0, END)
    msglist.yview(END)


root = Tk()
root.geometry('500x570+100+30')
root.config(bg='rosybrown2')
root.title("ChatBot criado pela Fábrica de Programadores")

picture_Label = Label(root, bg='rosybrown2')
picture_Label.pack(pady=5)
center_Frame = Frame(root)
center_Frame.pack()
scrollbar = Scrollbar(center_Frame)
scrollbar.pack(side=RIGHT, fill=Y)
msglist = Listbox(center_Frame, width=80,font=('times new roman',20,'bold'), height=10, yscrollcommand=scrollbar.set, bg='grey95', fg='grey2')
msglist.pack(side=LEFT, fill=BOTH)

questionField = Entry(root, font='verdana,25,bold', bg='grey95', fg='grey2')
questionField.pack(fill=X, pady=15)
btn = Button(root, font='verdana,25', command=ask_from_bot)
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

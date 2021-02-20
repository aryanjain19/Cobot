# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 19:55:18 2021
"""
from tkinter import *
from tkinter.ttk import *
import tkinter.scrolledtext as st
import aiml
import os
import gtts
from gtts import *
import pyttsx3 
import webbrowser
from playsound import playsound
def start_GUI():
   
    
    def send_msg():
        chat_area.config(state = NORMAL)
        sent_message = bot_input.get()
        bot_input.set("")
        #print(sent_message)
        chat_area.insert(INSERT,"You: "+ sent_message)
        res = str(kernal.respond(sent_message))
        #print(res)
        output = ""
        if res == "?!!" or res == "?!":
            
            import requests
            from bs4 import BeautifulSoup
            if res == "?!!":
                URL = "https://www.worldometers.info/coronavirus/country/india/"
            elif res == "?!":
                URL = "https://www.worldometers.info/coronavirus/"
            r = requests.get(URL)
            soup = BeautifulSoup(r.content,'html5lib')
            n1 = soup.find('div',attrs = {'class':'container'})
            n2 = n1.find_all_next('div',attrs = {'class' : 'row'})
            n3 = n2[0].find_all_next('div',attrs = {'class':'col-md-8'})
            n4 = n3[0].find_all_next('div',attrs = {'class':'content-inner'})
            num5 = n4[0].find_all_next('div',attrs = {'id':'maincounter-wrap'})
            
            conf = (num5[0].find_all_next('div',attrs = {'class':'maincounter-number'}))
            
            confirm = ""
            for i in conf[0].span.text:
                if i == ',':
                    continue
                else:
                    confirm = confirm + i
            #chat_area.insert(INSERT,"\nBOT: Active Cases: " + cases[0].span.text + "\n")
            conf_cases = int(confirm)        
            de = num5[1].find_all_next('div',attrs = {'class':'maincounter-number'})
            deaths = de[0].span.text
            #chat_area.insert(INSERT,"Deaths: "+ deaths[0].span.text+"\n")
            recov = (num5[2].find_all_next('div',attrs = {'class':'maincounter-number'}))
            recover = ""
            for i in recov[0].span.text:
                if i == ',':
                    continue
                else:
                    recover += i
            recoveries = int(recover)
            active_cases = conf_cases - recoveries
            active = str(active_cases)
            
            output = "Confirmed Cases: " + conf[0].span.text +"\nActive Cases: " + active + "   \nDeaths: " + deaths + "   \nRecoveries: " + recover
            chat_area.insert(INSERT,"\nBOT: "+ output + "\n\n")
            #chat_area.insert(INSERT,"Recoveries: " + rec[0].span.text + "\n")
            #print(soup.prettify())
            #print(numbers)
        elif res[0] == 's' and res[1] == 's':
            search = ""
            output = "Redirecting to your default browser"
            chat_area.insert(INSERT,"\nBOT: Redirecting to your default browser\n\n")
            for i in range(2,len(res)):
                search += res[i]
            webbrowser.open_new_tab(search)    
        else:
            output = res
            #webbrowser.open_new_tab('http://www.python.org')
            chat_area.insert(INSERT,"\nBOT: " + res +"\n\n")
            
        #chat_area.focus()
        
        sound = gtts.gTTS(text = output,lang = 'en',slow = False)
        #mp3_fp = BytesIO()
        #sound.write_to_fp(mp3_fp)
        
        sound.save("speak.mp3")
        #os.system("start speak.mp3")
        #os.system("taskkill /im speak.mp3 /f")
        """engine = pyttsx3.init()
        engine.connect('started')
        engine.say(output)
        engine.runAndWait()"""
        playsound("speak.mp3")
        os.remove("speak.mp3")
        
        chat_area.config(state = DISABLED)
        
        
    
    """  
    base = Tk()
    base.title("CoBot 1.0")
         bot_input = StringVar()
    base.geometry('500x500')
    
    heading = Label(base,text = "Welcome to CoBot",font = "25",foreground = "red").pack()
    
    msg = Message(base,text = "ChatBot to answer Covid related queries",justify = "center",foreground = "blue").pack()
    inp_entry = Entry(base,textvariable = bot_input).place(x = 220, y = 400)
    send  = Button(base,text = "Send",command = lambda : send_msg()).place(x = 350,y = 400 )
    send_lab = Label(base,text = "Enter your query here:",font =("Italics",12)).place(x = 50,y = 400)
    chat_area = st.ScrolledText(base,width  = 30,height = 12,font = ("Times New Roman",15))
    chat_area.config(state = DISABLED)
    
    
    chat_area.place(x = 100,y = 100)
    
        
    base.mainloop()"""
    base = Tk()
    base.title("COBOT 2.0")
    bot_input = StringVar()
    base.resizable(width = False,height = False)
    base.configure(width = 470,height = 550,bg = "#17202A")
    head = Label(base,text = "Welcome to CoBot !",font = ("helvetica",15),foreground = "orange",background ="#17202A" )
    head.place(x =230,y = 30, anchor= CENTER)
    footer = LabelFrame(base,borderwidth= 5,width= 450,height = 70).place(x = 10,y = 458)

    send = Button(footer,text="Send",command = lambda: send_msg(),width = 10)
    #send.config(font= ("helvetica" ,10, "bold"))
    send.place(relheight = 0.09,x = 370,y = 468)
    entrymsg = Entry(base,textvariable = bot_input ,font = ("Helvetica",15))
    entrymsg.focus()
    entrymsg.place(in_= footer,relwidth = 0.74,  relheight = 0.09, y = 468, x = 20 )

    chat_area = Text(base,width = 20,height = 2,bg = "indigo",fg = "#EAECEE",font = "Helvetica 14",padx = 5,pady = 5)
    chat_area.place(relheight = 0.745,relwidth = 1,rely = 0.08)
    chat_area.config(cursor= "arrow")
    scroll  = Scrollbar(chat_area)
    scroll.config(command= chat_area.yview)
    scroll.place(relheight=1,relx = 0.98)
    #chat_area.insert(INSERT,"BOT: HELLO TESTING")
    #chat_area.insert(INSERT,"\nTesting again")
    chat_area.config(state = DISABLED)
    copyr = Label(base,text = "By Team PRO_fessors",font = ("Times New Roman",10),foreground= "red",background="#17202A")
    copyr.place(x = 150,y = 530)
    base.mainloop()


kernal = aiml.Kernel()
#kernal.learn("startup.xml")
#kernal.learn("*.aiml.xml")
if os.path.isfile("bot_brain2.brn"):
    kernal.bootstrap(brainFile = "bot_brain2.brn")
else:
    kernal.bootstrap(learnFiles = "startup.xml",commands =["load aiml a","load aiml b"] )
    kernal.saveBrain("bot_brain2.brn")

start_GUI()    

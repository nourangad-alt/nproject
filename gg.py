from gtts import gTTS
from playsound import playsound
from tkinter import *

root=Tk()
root.title('text to speech ')
mylabel1=Label(root ,text='text to speech')
mylabel1.pack()
mylabel2=Label(root ,text='enter your text')
mylabel2.pack()

mytext=Entry(root , width=50)
mytext.pack()
def texttospeech():
    text=mytext.get()
    if text:
        t=gTTS(text)
        t.save('out.mp3')
        playsound('out.mp3')
    else:
        print('error')    
button1=Button(root , text='play' , command=texttospeech )

button1.pack( side=LEFT , padx=40, pady=10 )
def deletetext():
    mytext.delete( 0 ,END)
button2=Button(root , text='set' , command=deletetext , bg='blue' )

button2.pack( side=LEFT , padx=40 , pady=10)    
def closewindow():
    root.quit()
button3=Button(root , text='exit' , command=closewindow ,bg='red'  )

button3.pack( side=RIGHT , padx= 40 , pady=10)



root.mainloop()
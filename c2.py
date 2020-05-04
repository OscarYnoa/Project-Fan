from tkinter import *
import os

def click():
    os.system("start C:/Users/oscar/Desktop/Listo/Slow_Fan.mp4")
def click_2():
    os.system("start C:/Users/oscar/Desktop/Listo/Med_Fan.mp4")
def click_3():
    os.system("start C:/Users/oscar/Desktop/Listo/High_Fan.mp4")



window = Tk()
window.title('My Display')
window.configure(background="black")

photo = PhotoImage (file="C:/Users/oscar/Desktop/Listo/Off_Fan.gif")
Label( window, image=photo,bg='black').grid(row=0,column=0,sticky=W)

Button(window,text='1',width= 6, command =click) .grid(row=3,column = 0,sticky=W)
Button(window,text='2',width= 6, command =click_2) .grid(row=3,column = 0,sticky=N)
Button(window,text='3',width= 6, command =click_3) .grid(row=3,column = 0,sticky=E)




window.mainloop()

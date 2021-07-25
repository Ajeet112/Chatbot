from tkinter import *
root=Tk()
def send():
    send="you-"+e.get()
    txt.insert(END, "\n" + send)
    if (e.get() == "hello"):
        txt.insert(END, "\n" + "bot-> Hi,how are you?")
    elif (e.get() == "I am good"):
        txt.insert(END, "\n" + "bot-> nice to hear")
    else:
        txt.insert(END, "\n" + "bot-> sorry,I din't get it")

txt=Text(root)
txt.grid(row=0,column=0,columnspan=2)
e=Entry(root,width=100)
send=Button(root,text="Send",command=send).grid(row=1,column=1)
e.grid(row=1,column=0)
root.title("Chatbot")
root.mainloop()


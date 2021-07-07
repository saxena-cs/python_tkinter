import webbrowser
import tkinter as tk
root = tk.Tk()
root.geometry('500x200')
root.title("WEB Browser")


def fb():
    webbrowser.open_new("www.facebook.com")


def insta():
    webbrowser.open_new("www.instagram.com")


def twi():
    webbrowser.open_new("www.twitter.com")


def lin():
    webbrowser.open_new("www.linkedin.com")


def search():
    word = x.get()
    key = 'https://www.google.com/search?q=' + word
    webbrowser.open_new(key)


def yt():
    webbrowser.open_new("www.youtube.com")


x = tk.StringVar()
b1 = tk.Button(root,text="Facebook",fg="white",bg="#3b5998",command=fb)
b1.place(x=20,y=60,width=90,height=30)
b2 = tk.Button(root,text="Instagram",fg="white",bg="#a31782",command=insta)
b2.place(x=160,y=60,width=90,height=30)
b3 = tk.Button(root,text="Twitter",fg="white",bg="#277ee3",command=twi)
b3.place(x=20,y=100,width=90,height=30)
b4 = tk.Button(root,text="LinkedIn",fg="white",bg="#0840a1",command=lin)
b4.place(x=160,y=100,width=90,height=30)
b5 = tk.Button(root,text="Search",fg="white",bg="#1c1a1a",command=search)
b5.place(x=5,y=10,width=90,height=30)
b6 = tk.Button(root,text="Youtube",fg="white",bg="#b80606",command=yt)
b6.place(x=20,y=140,width=90,height=30)
e1 = tk.Entry(root,textvariable=x)
e1.place(x=100,y=10,width=380,height=30)
root.mainloop()
from tkinter import *

def my_window():
    window = Tk()

    window.geometry("300x300")
    window.maxsize(800,800)
    window.minsize(200,200)

    window.title("My application")

    # create label
    label = Label(window, text="Salam be class python khosh amadid 😊")
    label.pack()
    # label.place(x=30,y=50)

    # create input
    input1 = Entry(window)
    input1.pack()

    input2 = Entry(window)
    input2.pack()


    def say_hello():
        # print("salam donya")
        label.config(text="Django")
        btn.config(text="clicked")
        name = input1.get()
        l_name = input2.get()    

    # create button
    btn = Button(window, text="Click here", fg="Yellow", bg="Blue",command=say_hello)
    btn.pack()


    window.mainloop()



my_window()
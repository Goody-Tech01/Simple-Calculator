from tkinter import *

def button_press(num):
    global equation_text
    equation_text=equation_text + str(num)
    equation_label.set(equation_text)


def equals():
    global equation_text
    try:
        total=str(eval(equation_text))
        equation_label.set(total)
        equation_text=total
    except ZeroDivisionError:
        equation_label.set("Arithmetic Error")
        equation_text=""
    except SyntaxError:
        equation_label.set("Syntax Error")
        equation_text = ""

def clear():
    global equation_text
    equation_label.set("")
    equation_text=""


window=Tk()
window.title("simple calculator program"),
window.geometry("800x700"),
window.resizable(True,True)

equation_text=" "
equation_label=StringVar()

display_frame=Frame(window,
                    bg="grey",
                    bd=7,
                    relief="ridge",
                    )
display_frame.pack(pady=10)

label=Label(display_frame,
            textvariable=equation_label,
            font=("consolas",20),
            bg="light grey",
            anchor="e",
            width=27,
            height=1,
            padx=5,
            pady=5)

label.pack()


frame=Frame(window,bd=5,relief="groove",bg="#e6f2ff")
frame.pack(pady=20)   #the frame is for the numbers

button1=Button(frame,
               text=1,height=3,width=7,font=35,bg="red",relief="flat",
               command=lambda:button_press(1))
button1.grid(row=0,column=0,padx=2,pady=2)

button2=Button(frame,
               text=2,height=3,width=7,font=35,bg="green",relief="flat",
               command=lambda:button_press(2))
button2.grid(row=0,column=1,padx=2,pady=2)

button3=Button(frame,
               text=3,height=3,width=7,font=35,bg="blue",relief="flat",
               command=lambda:button_press(3))
button3.grid(row=0,column=2,padx=2,pady=2)

button4=Button(frame,
               text=4,height=3,width=7,font=35,bg="green",relief="flat",
               command=lambda:button_press(4))
button4.grid(row=1,column=0,padx=2,pady=2)

button5=Button(frame,
               text=5,height=3,width=7,font=35,bg="blue",relief="flat",
               command=lambda:button_press(5))
button5.grid(row=1,column=1,padx=2,pady=2)

button6=Button(frame,
               text=6,height=3,width=7,font=35,bg="red",relief="flat",
               command=lambda:button_press(6))
button6.grid(row=1,column=2,padx=2,pady=2)

button7=Button(frame,
               text=7,height=3,width=7,font=35,bg="blue",relief="flat",
               command=lambda:button_press(7))
button7.grid(row=2,column=0,padx=2,pady=2)

button8=Button(frame,
               text=8,height=3,width=7,font=35,bg="green",relief="flat",
               command=lambda:button_press(8))
button8.grid(row=2,column=1,padx=2,pady=2)

button9=Button(frame,
               text=9,height=3,width=7,font=35,bg="red",relief="flat",
               command=lambda:button_press(9))
button9.grid(row=2,column=2,padx=2,pady=2)

button0=Button(frame,
               text=0,height=3,width=7,font=35,bg="red",relief="flat",
               command=lambda:button_press("0"))
button0.grid(row=3,column=0,padx=2,pady=2)

plus=Button(frame,
               text="+",height=3,width=7,font=35,bg="#4A90E2",relief="flat",
               command=lambda:button_press("+"))
plus.grid(row=0,column=3,padx=2,pady=2)

minus=Button(frame,
               text="-",height=3,width=7,font=35,bg="#4A90E2",relief="flat",
               command=lambda:button_press("-"))
minus.grid(row=1,column=3,padx=2,pady=2)

multiply=Button(frame,
               text="*",height=3,width=7,font=35,bg="#4A90E2",relief="flat",
               command=lambda:button_press("*"))
multiply.grid(row=2,column=3,padx=2,pady=2)

divide=Button(frame,
               text="/",height=3,width=7,font=35,bg="#4A90E2",relief="flat",
               command=lambda:button_press("/"))
divide.grid(row=3,column=3,padx=2,pady=2)

equals=Button(frame,
               text="=",height=3,width=7,font="35",bg="#4A90E2",relief="flat",
               command=(equals))
equals.grid(row=3,column=2,padx=2,pady=2)

decimal=Button(frame,
               text=".",height=3,width=7,font="35",bg="#4A90E2",relief="flat",
               command=lambda:button_press("."))
decimal.grid(row=3,column=1,padx=2,pady=2)

clear=Button(frame,
               text="CLEAR",height=2,width=17,font="35",bg="#4A90E2",relief="flat",
               command=(clear))
clear.grid(row=4,column=0,columnspan=4,pady=(5,10))

window.mainloop()



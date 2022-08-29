from tkinter import*

import random


root = Tk()  #gui interface create

root.geometry("350x250+250+250")  # weidth, height

root.title("Lottery")   # interface name"Lottery"

root.configure(bg="#437EAB")


def rm():
    
    
    a = int(take_in_value.get())
    cal = random.randint(1,10)

    if (cal == a):
    

        p = "Yeaaa ! you won!"
        
        
        y.delete('1.0',END)
        y.insert(END,p)

        t.delete('1.0',END)
        t.insert(END,cal)

    else:
        
        d = "you lose"
        y.delete('1.0',END)
        y.insert(END,d)
        

        t.delete('1.0',END)
        t.insert(END,cal)
        
def reset():
    rm = " "
    y.delete('1.0',END)
    y.insert(END,rm)
    
    t.delete('1.0',END)
    t.insert(END,rm)


take_num = Label(root, text ="Enter any number [1 to 10] :",bg="#D2E7F6",fg="#515354")
take_num.grid(row=0,sticky=E)


take_in_value  = StringVar()
take_in = Entry(root, textvar = take_in_value)   # Entry diye user theke value nae
take_in.grid(row=0,column=1)
t = Text(root, height = 1, width = 20)
t.grid(row=2,columnspan=2,pady=5)

lot = Button(root,text = "Lottery",command=rm, bg="#E8EAEB",fg="orange")
lot.grid(row=1,columnspan=2,pady=15)

mass= Label(root, text="Complement",bg="#D2E7F6",fg="#515354")
mass.grid(row=3,sticky=W,pady=10)


y = Text(root, height = 1, width = 20)
y.grid(row=3,column=1,pady=10)

rese = Button(root, text="Reset", command=reset,bg="black",fg="orange")
rese.grid(row=5,columnspan=2,pady=10)





root.mainloop()
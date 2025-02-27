def nazat ():
    global combobox
    print(combobox.get())

def klass1():
    global combobox
    zube()
    print("вы очистили окно")
    languages=["воин","лучник","маг"]
    combobox = ttk.Combobox(values=languages)
    combobox.grid(column=0,row=0)
    btn3=Button(window,text="начать",command=nazat)
    btn3.grid(column=0,row=1)

def crahenie():
    global lbl1
    global lbl2
    global fi
    global btn1
    global btn2

    zube()
    
    lbl1=Label(window,text="0")
    lbl1.grid(column=0,row=0,columnspan=20)

    fi=Label(window,text="ты ударил на ")
    fi.grid(column=0,row=1,columnspan=20)

    lbl2=Label(window,text="ю левель ")
    lbl2.grid(column=0,row=2,columnspan=20)

    btn1=Button(window,text="кликай",width=10,height=10,command=plastinavzube)
    btn1.grid(column=0,row=3,columnspan=15)

    btn2=Button(window,text="улучшение",width=10,height=10,command=plastinavzube)
    btn2.grid(column=21,row=3,columnspan=15)

def be():
    global lov
    global exp
    if exp==0:
        messagebox.showinfo("ошибка","недостаточно опыта!")
    else: 
        lov=lov+1
        exp=exp-1
        lbl4["text"]=f"ловкость {lov}"
        lbl6["text"]=f"опыт {exp}"
    

def e():
    global ym
    global exp
    if exp==0:
        messagebox.showinfo("ошибка","недостаточно опыта!")
    else: 
        ym=ym+1
        exp=exp-1
        lbl5["text"]=f"интелект {ym}"
        lbl6["text"]=f"опыт {exp}"
    
def a():
    global CNLA
    global exp
    if exp==0:
        messagebox.showinfo("ошибка","недостаточно опыта!")
    else: 
        CNLA=CNLA+1
        exp=exp-1
        lbl3["text"]=f"сила {CNLA}"
        lbl6["text"]=f"опыт {exp}"

def zube():
  for widget in window.winfo_children():
        if not isinstance(widget,tk.Menu):
            widget.destroy()


def vzube():
    global lbl3
    global lbl4
    global lbl5
    global lbl6
    global exp
    print("вы нажали навыки")
    zube()
    lbl3=Label(window,text=f"сила {CNLA}")
    lbl3.grid(column=0,row=1)
    
    lbl4=Label(window,text=f"ловкость {lov}")
    lbl4.grid(column=0,row=2)
    
    lbl5=Label(window,text=f"интелект {ym}")
    lbl5.grid(column=0,row=3)

    lbl6=Label(window,text=f"опыт {exp}")
    lbl6.grid(column=0,row=0)


    btn3=Button(window,text="+",command=a)
    btn3.grid(column=1,row=1)

    btn4=Button(window,text="+",command=be)
    btn4.grid(column=1,row=2)

    btn5=Button(window,text="+",command=e)
    btn5.grid(column=1,row=3)

    
    
#кнопка
def plastinavzube():
    global i
    global level
    global level1
    global f
    global exp
    ataka = rd.randint(level1,level1*2)
    i = i - ataka
    lbl1["text"]=i
    fi["text"]=f"вы ударили на {ataka}"
    if i<=0:
        lbl1["text"]="ю виктори"
        level = level + 1
        i=level*100
        level1=level1+level
        lbl2["text"]=f"ю левель {level1}"
        exp=exp+1
        
import tkinter as tk  
from tkinter import *
from tkinter import messagebox
from random import *
import random as rd
from tkinter import ttk

#хп монстра
i=5

#ур монстра
level=1

#твой ур 
level1=1

#атака
f = rd.randint(level1,level1*2)

#опыт
exp=0

#интелект
ym=0

#сила
CNLA=0

#класс
klass=0

#ловкость
lov=0

window=Tk()
window.title("кликер")
window.geometry('200x200')

main_menu = Menu()

game_menu =Menu(main_menu,tearoff=0)
game_menu.add_command(label="сохранить")
game_menu.add_command(label="загрузить")
game_menu.add_command(label="сражение",command=crahenie)

people_menu =Menu(main_menu,tearoff=0)
people_menu.add_command(label="навыки",command=vzube)
people_menu.add_command(label="броня")
people_menu.add_command(label="класс",command=klass1)

main_menu.add_cascade(label="игра",menu=game_menu)

main_menu.add_cascade(label="игрок",menu=people_menu)

main_menu.add_cascade(label="выход",command=lambda: window.destroy())

lbl1=Label(window,text="0")
lbl1.grid(column=0,row=0,columnspan=20)

fi=Label(window,text="ты ударил на ")
fi.grid(column=0,row=1,columnspan=20)

lbl2=Label(window,text="ю левель ")
lbl2.grid(column=0,row=2,columnspan=20)

btn1=Button(window,text="кликай",width=10,height=10,command=plastinavzube)
btn1.grid(column=0,row=3,columnspan=15)

btn2=Button(window,text="улучшение",width=10,height=10,command=plastinavzube)
btn2.grid(column=21,row=3,columnspan=15)

window.config(menu=main_menu)


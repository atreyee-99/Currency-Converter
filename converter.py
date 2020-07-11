from forex_python.converter import CurrencyRates, CurrencyCodes
from tkinter import *
import tkinter


root=tkinter.Tk()
root.title("Currency Converter")

root.geometry("500x500")

l1=Label(root,text='Currency Converter',font='times 20',fg='red')
l1.pack(ipadx=10,ipady=10,pady=30)

OPTIONS = ['Bulgaria Lev',
           'Euro',
           'India Rupee',
           'Indonesia Rupiah',
           'Israel Shekel',
           'Japan Yen',
           'Thailand Baht',
           'United Kingdom Pound',
           'United States Dollar']

SYMBOLS = ['BGN','EUR','INR','IDR','ILS','JPY','THB','GBP','USD']

def action():
    p1=variable1.get() #converts from(currency)
    n1=v1.get() #amount to be converted
    p2=variable2.get() #converts to(currency)
    m1=SYMBOLS[OPTIONS.index(p1)] 
    m2 = SYMBOLS[OPTIONS.index(p2)]
    n2=c.convert(m1,m2,n1) #converted amount(imported from library)
    E2.config(text=cur.get_symbol(m2)+' '+str(n2)) #displays the result


variable1 = StringVar(root)
variable1.set(OPTIONS[0])

variable2 = StringVar(root)
variable2.set(OPTIONS[0])

l2=Label(root,text='Choose Original Currency:',font='times 20')
l2.pack()

w1 = OptionMenu(root, variable1, *OPTIONS)
w1.config(font=('Helvetica', 15))
w1.pack()

v1=IntVar(root)
v2=IntVar(root)

E1 = Entry(root,textvariable=v1,bg='#d6d4d4',font='times 15')
E1.pack(pady=2)

l4=Label(root)
l4.pack(pady=5)

l3=Label(root,text='Choose Converted Currency:',font='times 20')
l3.pack()

w2 = OptionMenu(root, variable2, *OPTIONS)
w2.config(font=('Helvetica', 15))
w2.pack()

E2 = Label(root,text="",font='times 15')
E2.pack(pady=2)

b1=Button(root,text='Convert',font=('Helvetica', 15),bg='#84d5fa',command=action)
b1.pack(pady=20)

c=CurrencyRates()   
cur=CurrencyCodes() #current value 

root.mainloop()
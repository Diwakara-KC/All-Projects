from tkinter import *
from tkinter import filedialog, messagebox
import time
import psycopg2

conn = psycopg2.connect(database="SaviRuchiHotel", user = "postgres", password = "root", host = "127.0.0.1", port = "5432")

cur = conn.cursor()
# cur.execute('''CREATE TABLE HOTEL_DB
#       (ID INT     NOT NULL,
#       Today_Date     DATE  NOT NULL,
#       Name      TEXT NOT NULL,
#       Phone_Number VARCHAR(15)  NOT NULL,
#       Price       INT     NOT NULL
#       );''')

def reset():
    textReceipt.delete(1.0, END)
    textname.delete(0,END)
    textphone.delete(0,END)

    e_idli.set('0')
    e_vada.set('0')
    e_dosa.set('0')
    e_puri.set('0')
    e_chapathi.set('0')
    e_parotta.set('0')
    e_rice.set('0')
    e_minimeals.set('0')
    e_meals.set('0')
    e_bajjibonda.set('0')

    e_milk.set('0')
    e_badammilk.set('0')
    e_coffee.set('0')
    e_tea.set('0')
    e_cooldrinks.set('0')
    e_waterbottle.set('0')

    e_chocolate.set('0')
    e_parsal.set('0')
    e_others.set('0')

    textname.config()
    textphone.config()
    textidli.config(state=DISABLED)
    textvada.config(state=DISABLED)
    textdosa.config(state=DISABLED)
    textpuri.config(state=DISABLED)
    textchapathi.config(state=DISABLED)
    textparotta.config(state=DISABLED)
    textrice.config(state=DISABLED)
    textminimeals.config(state=DISABLED)
    textmeals.config(state=DISABLED)
    textbajjibonda.config(state=DISABLED)

    textmilk.config(state=DISABLED)
    textbadammilk.config(state=DISABLED)
    textcoffee.config(state=DISABLED)
    texttea.config(state=DISABLED)
    textcooldrinks.config(state=DISABLED)
    textwaterbottle.config(state=DISABLED)

    textchocolate.config(state=DISABLED)
    textparsal.config(state=DISABLED)
    textothers.config(state=DISABLED)

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)
    var19.set(0)

    costofdrinksvar.set('')
    costoffoodvar.set('')
    costofothersvar.set('')
    subtotalvar.set('')
    servicetaxvar.set('')
    totalcostvar.set('')

def save():
    if textReceipt.get(1.0, END) == '\n':
        pass
    else:
        url = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
        if url == None:
            pass
        else:

            bill_data = textReceipt.get(1.0, END)
            url.write(bill_data)
            url.close()
            messagebox.showinfo('Information', 'Your Bill Is Succesfully Saved')
a=1
x = range(a, 100000)
y = iter(x)
def receipt():
    global billnumber, date,BN

    if costoffoodvar.get() != '' or costofothersvar.get() != '' or costofdrinksvar.get() != '':

        textReceipt.delete(1.0, END)

        billnumber=next(y)
        BN=billnumber
        date = time.strftime('%d-%m-%Y')

        textReceipt.insert(END, 'Receipt No :\t' + str(billnumber) + '\t\t' +'Date : '+ date + '\n')
        textReceipt.insert(END, '---------------------------------------------------------------\n')
        textReceipt.insert(END, 'Name : ' + str(textname.get()) + '\t\t' + 'Phone : ' + str(textphone.get()) + '\n')
        textReceipt.insert(END, '***********************************************************\n')
        textReceipt.insert(END, 'Items:\t\t\tCost Of Items(Rs)\n')
        textReceipt.insert(END, '***********************************************************\n')

        if e_idli.get() != '0':
            textReceipt.insert(END, f'Idli         :\t\t\t\t        {int(e_idli.get()) *     30} \n\n')

        if e_vada.get() != '0':
            textReceipt.insert(END, f'Vada         :\t\t\t\t        {int(e_vada.get()) *     10} \n\n')

        if e_dosa.get() != '0':
            textReceipt.insert(END, f'Dosa         :\t\t\t\t        {int(e_dosa.get()) *     30} \n\n')

        if e_puri.get() != '0':
            textReceipt.insert(END, f'Puri         :\t\t\t\t        {int(e_puri.get()) *     30} \n\n')

        if e_chapathi.get() != '0':
            textReceipt.insert(END, f'Chapathi     :\t\t\t\t        {int(e_chapathi.get()) * 30} \n\n')

        if e_parotta.get() != '0':
            textReceipt.insert(END, f'Parotta      :\t\t\t\t        {int(e_parotta.get()) *  30} \n\n')

        if e_rice.get() != '0':
            textReceipt.insert(END, f'Rice         :\t\t\t\t        {int(e_rice.get()) *     30} \n\n')

        if e_minimeals.get() != '0':
            textReceipt.insert(END, f'Mini Meals   :\t\t\t\t        {int(e_minimeals.get())* 40} \n\n')

        if e_meals.get() != '0':
            textReceipt.insert(END, f'Meals        :\t\t\t\t        {int(e_meals.get()) *    50} \n\n')

        if e_bajjibonda.get() != '0':
            textReceipt.insert(END,f'Bajji/Bonda   :\t\t\t\t        {int(e_bajjibonda.get())*20} \n\n')


        if e_milk.get() != '0':
            textReceipt.insert(END, f'Milk         :\t\t\t\t        {int(e_milk.get()) *     10} \n\n')

        if e_badammilk.get() != '0':
            textReceipt.insert(END, f'Badam Milk   :\t\t\t\t        {int(e_badammilk.get()) *10} \n\n')

        if e_coffee.get() != '0':
            textReceipt.insert(END, f'Coffee       :\t\t\t\t        {int(e_coffee.get()) *   10} \n\n')

        if e_tea.get() != '0':
            textReceipt.insert(END, f'Tea          :\t\t\t\t        {int(e_tea.get()) *      10} \n\n')

        if e_cooldrinks.get() != '0':
            textReceipt.insert(END, f'Cold Drinks  :\t\t\t\t        {int(e_cooldrinks.get())   } \n\n')

        if e_waterbottle.get() != '0':
            textReceipt.insert(END, f'Water Bottle :\t\t\t\t        {int(e_waterbottle.get())  } \n\n')


        if e_chocolate.get() != '0':
            textReceipt.insert(END, f'Chocolate    :\t\t\t\t        {int(e_chocolate.get())   } \n\n')

        if e_parsal.get() != '0':
            textReceipt.insert(END, f'Parsal       :\t\t\t\t        {int(e_parsal.get()) * 5     } \n\n')

        if e_others.get() != '0':
            textReceipt.insert(END, f'Other        :\t\t\t\t        {int(e_others.get())         }  \n\n')



        textReceipt.insert(END, '***********************************************************\n')

        textReceipt.insert(END, f'Sub Total    :\t\t\t\t        {subtotalofItems             } \n\n')
        textReceipt.insert(END, f'Service Tax  :\t\t\t\t        {0                           } \n\n')
        textReceipt.insert(END, '***********************************************************\n')
        textReceipt.insert(END, f'Total Cost   :\t\t\t\t        {subtotalofItems             } Rs\n')
        textReceipt.insert(END, '***********************************************************\n')
        textReceipt.insert(END, f'\t\tThank You\n')

        date1 = time.strftime('%Y-%m-%d')
        cur.execute("INSERT INTO HOTEL_DB (ID,Today_Date,Name,Phone_Number,Price) \
                  VALUES ({},'{}','{}',{},{})".format(billnumber,str(date1),str(textname.get()),str(textphone.get()),subtotalofItems));



    else:
        messagebox.showerror('Error', 'No Item Is selected')




def totalcost():
    global priceofFood, priceofDrinks, priceofOthers, subtotalofItems
    if var1.get() != 0 or var2.get() != 0 or var3.get() != 0 or var4.get() != 0 or var5.get() != 0 or \
            var6.get() != 0 or var7.get() != 0 or var8.get() != 0 or var9.get() != 0 or var10.get() != 0 or \
            var11.get() != 0 or var12.get() != 0 or var13.get() != 0 or var14.get() != 0 or var15.get() != 0 or \
            var16.get() != 0 or var17.get() != 0 or var18.get() != 0 or var19.get() != 0 :

        item1 = int(e_idli.get())
        item2 = int(e_vada.get())
        item3 = int(e_dosa.get())
        item4 = int(e_puri.get())
        item5 = int(e_chapathi.get())
        item6 = int(e_parotta.get())
        item7 = int(e_rice.get())
        item8 = int(e_minimeals.get())
        item9 = int(e_meals.get())
        item10 = int(e_bajjibonda.get())

        item11 = int(e_milk.get())
        item12 = int(e_badammilk.get())
        item13 = int(e_coffee.get())
        item14 = int(e_tea.get())
        item15 = int(e_cooldrinks.get())
        item16 = int(e_waterbottle.get())


        item17 = int(e_chocolate.get())
        item18 = int(e_parsal.get())
        item19 = int(e_others.get())




        priceofFood = (item1 * 30) + (item2 * 10) + (item3 * 30) + (item4 * 30) + (item5 * 30) + (item6 * 30) + (
                    item7 * 30) \
                      + (item8 * 40) + (item9 * 50)+(item10 *20)

        priceofDrinks = (item11 * 10) + (item12 * 10) + (item13 * 10) + (item14 * 10) + item15 + item16

        priceofOthers = item17  + item18 + item19

        costoffoodvar.set(str(priceofFood) + ' Rs')
        costofdrinksvar.set(str(priceofDrinks) + ' Rs')
        costofothersvar.set(str(priceofOthers) + ' Rs')

        subtotalofItems = priceofFood + priceofDrinks + priceofOthers
        subtotalvar.set(str(subtotalofItems) + ' Rs')

        servicetaxvar.set('0 Rs')

        tottalcost = subtotalofItems
        totalcostvar.set(str(tottalcost) + ' Rs')

    else:
        messagebox.showerror('Error', 'No Item Is selected')


def idli():
    if var1.get() == 1:
        textidli.config(state=NORMAL)
        textidli.delete(0, END)
        textidli.focus()
    else:
        textidli.config(state=DISABLED)
        e_idli.set('0')


def vada():
    if var2.get() == 1:
        textvada.config(state=NORMAL)
        textvada.delete(0, END)
        textvada.focus()

    else:
        textvada.config(state=DISABLED)
        e_vada.set('0')


def dosa():
    if var3.get() == 1:
        textdosa.config(state=NORMAL)
        textdosa.delete(0, END)
        textdosa.focus()

    else:
        textdosa.config(state=DISABLED)
        e_dosa.set('0')


def puri():
    if var4.get() == 1:
        textpuri.config(state=NORMAL)
        textpuri.focus()
        textpuri.delete(0, END)
    elif var4.get() == 0:
        textpuri.config(state=DISABLED)
        e_puri.set('0')


def chapathi():
    if var5.get() == 1:
        textchapathi.config(state=NORMAL)
        textchapathi.focus()
        textchapathi.delete(0, END)
    elif var5.get() == 0:
        textchapathi.config(state=DISABLED)
        e_chapathi.set('0')


def parotta():
    if var6.get() == 1:
        textparotta.config(state=NORMAL)
        textparotta.focus()
        textparotta.delete(0, END)
    elif var6.get() == 0:
        textparotta.config(state=DISABLED)
        e_parotta.set('0')


def rice():
    if var7.get() == 1:
        textrice.config(state=NORMAL)
        textrice.focus()
        textrice.delete(0, END)
    elif var7.get() == 0:
        textrice.config(state=DISABLED)
        e_rice.set('0')


def minimeals():
    if var8.get() == 1:
        textminimeals.config(state=NORMAL)
        textminimeals.focus()
        textminimeals.delete(0, END)
    elif var8.get() == 0:
        textminimeals.config(state=DISABLED)
        e_minimeals.set('0')


def meals():
    if var9.get() == 1:
        textmeals.config(state=NORMAL)
        textmeals.focus()
        textmeals.delete(0, END)
    elif var9.get() == 0:
        textmeals.config(state=DISABLED)
        e_meals.set('0')


def bajjibonda():
    if var10.get() == 1:
        textbajjibonda.config(state=NORMAL)
        textbajjibonda.focus()
        textbajjibonda.delete(0, END)
    elif var10.get() == 0:
        textbajjibonda.config(state=DISABLED)
        e_bajjibonda.set('0')


def milk():
    if var11.get() == 1:
        textmilk.config(state=NORMAL)
        textmilk.focus()
        textcoffee.delete(0, END)
    elif var11.get() == 0:
        textmilk.config(state=DISABLED)
        e_milk.set('0')


def badammilk():
    if var12.get() == 1:
        textbadammilk.config(state=NORMAL)
        textbadammilk.focus()
        textbadammilk.delete(0, END)
    elif var12.get() == 0:
        textbadammilk.config(state=DISABLED)
        e_badammilk.set('0')


def coffee():
    if var13.get() == 1:
        textcoffee.config(state=NORMAL)
        textcoffee.focus()
        textcoffee.delete(0, END)
    elif var13.get() == 0:
        textcoffee.config(state=DISABLED)
        e_coffee.set('0')


def tea():
    if var14.get() == 1:
        texttea.config(state=NORMAL)
        texttea.focus()
        texttea.delete(0, END)
    elif var14.get() == 0:
        texttea.config(state=DISABLED)
        e_tea.set('0')


def cooldrinks():
    if var15.get() == 1:
        textcooldrinks.config(state=NORMAL)
        textcooldrinks.focus()
        textcooldrinks.delete(0, END)
    elif var15.get() == 0:
        textcooldrinks.config(state=DISABLED)
        e_cooldrinks.set('0')


def waterbottle():
    if var16.get() == 1:
        textwaterbottle.config(state=NORMAL)
        textwaterbottle.focus()
        textwaterbottle.delete(0, END)
    elif var16.get() == 0:
        textwaterbottle.config(state=DISABLED)
        e_waterbottle.set('0')


def chocolate():
    if var17.get() == 1:
        textchocolate.config(state=NORMAL)
        textchocolate.focus()
        textchocolate.delete(0, END)
    elif var17.get() == 0:
        textchocolate.config(state=DISABLED)
        e_chocolate.set('0')


def parsal():
    if var18.get() == 1:
        textparsal.config(state=NORMAL)
        textparsal.focus()
        textparsal.delete(0, END)
    elif var18.get() == 0:
        textparsal.config(state=DISABLED)
        e_parsal.set('0')


def others():
    if var19.get() == 1:
        textothers.config(state=NORMAL)
        textothers.delete(0, END)
        textothers.focus()
    else:
        textothers.config(state=DISABLED)
        e_others.set('0')

root = Tk()

root.geometry('1270x690+0+0')

root.resizable(0, 0)

root.title('Savi Ruchi Restaurant Management System created by Diwakara KC')

root.config(bg='firebrick4')

topFrame = Frame(root, bd=10, relief=RIDGE, bg='lightgreen')
topFrame.pack(side=TOP)

labelTitle = Label(topFrame, text='Savi Ruchi Hotel', font=('arial', 30, 'bold'), fg='yellow', bd=4,
                   bg='lightBlue', width=20)
labelTitle.grid(row=5, column=5)
name = Label(topFrame, text='NAME : ' , font=('arial', 10, 'bold'), fg='Black', bd=9,
                   bg='lightBlue', width=45)
name.grid(row=2, column=1)
textname = Entry(topFrame, font=('arial', 18, 'bold'), bd=9, width=15,textvariable=name)
textname.grid(row=5, column=1)
textname.focus_set()


phone= Label(topFrame, text='Phone Number : ' , font=('arial', 10, 'bold'), fg='Black', bd=9,
                   bg='lightBlue', width=45)
phone.grid(row=2, column=20)
textphone = Entry(topFrame, font=('arial', 18, 'bold'), bd=9, width=15,textvariable=phone)
textphone.grid(row=5, column=20)
textphone.focus_set()


menuFrame = Frame(root, bd=1, relief=RIDGE, bg='lightblue')
menuFrame.pack(side=LEFT)

costFrame = Frame(menuFrame, bd=6, relief=RIDGE, bg='green', pady=3)
costFrame.pack(side=BOTTOM)

foodFrame = LabelFrame(menuFrame, text='Food', font=('arial', 19, 'bold'), bd=11, relief=RIDGE, fg='red4', )
foodFrame.pack(side=LEFT)

drinksFrame = LabelFrame(menuFrame, text='Drinks', font=('arial', 19, 'bold'), bd=10, relief=RIDGE, fg='red4')
drinksFrame.pack(side=LEFT)

othersFrame = LabelFrame(menuFrame, text='Others', font=('arial', 19, 'bold'), bd=10, relief=RIDGE, fg='red4')
othersFrame.pack(side=LEFT)



rightFrame = Frame(root, bd=10, relief=RIDGE, bg='red4')
rightFrame.pack(side=RIGHT)

calculatorFrame = Frame(rightFrame, bd=1, relief=RIDGE, bg='red4')
calculatorFrame.pack()

recieptFrame = Frame(rightFrame, bd=3, relief=RIDGE, bg='red4')
recieptFrame.pack()

buttonFrame = Frame(rightFrame, bd=2, relief=RIDGE, bg='red4')
buttonFrame.pack()

# Variables

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()
var17 = IntVar()
var18 = IntVar()
var19 = IntVar()

e_idli = StringVar()
e_vada= StringVar()
e_dosa = StringVar()
e_puri = StringVar()
e_chapathi = StringVar()
e_parotta = StringVar()
e_rice= StringVar()
e_minimeals = StringVar()
e_meals = StringVar()
e_bajjibonda = StringVar()

e_milk = StringVar()
e_badammilk = StringVar()
e_coffee = StringVar()
e_tea = StringVar()
e_cooldrinks = StringVar()
e_waterbottle = StringVar()


e_chocolate = StringVar()
e_parsal = StringVar()
e_others = StringVar()

costoffoodvar = StringVar()
costofdrinksvar = StringVar()
costofothersvar = StringVar()
subtotalvar = StringVar()
servicetaxvar = StringVar()
totalcostvar = StringVar()

e_idli.set('0')
e_vada.set('0')
e_dosa.set('0')
e_puri.set('0')
e_chapathi.set('0')
e_parotta.set('0')
e_rice.set('0')
e_minimeals.set('0')
e_meals.set('0')
e_bajjibonda.set('0')

e_milk.set('0')
e_badammilk.set('0')
e_coffee.set('0')
e_tea.set('0')
e_cooldrinks.set('0')
e_waterbottle.set('0')

e_chocolate.set('0')
e_parsal.set('0')
e_others.set('0')
##FOOD

idli = Checkbutton(foodFrame, text='Idli', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var1
                   , command=idli)
idli.grid(row=0, column=0, sticky=W)

vada = Checkbutton(foodFrame, text='Vada', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var2
                   , command=vada)
vada.grid(row=1, column=0, sticky=W)

dosa = Checkbutton(foodFrame, text='Dosa', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var3
                   , command=dosa)
dosa.grid(row=2, column=0, sticky=W)



puri = Checkbutton(foodFrame, text='Puri', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var4
                    , command=puri)
puri.grid(row=3, column=0, sticky=W)

chapathi = Checkbutton(foodFrame, text='Chapathi', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var5
                    , command=chapathi)
chapathi.grid(row=4, column=0, sticky=W)

parotta = Checkbutton(foodFrame, text='Parotta', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var6
                     , command=parotta)
parotta.grid(row=5, column=0, sticky=W)

rice = Checkbutton(foodFrame, text='Rice', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var7,
                     command=rice)
rice.grid(row=6, column=0, sticky=W)

minimeals = Checkbutton(foodFrame, text='Mini Meals', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var8
                     , command=minimeals)
minimeals.grid(row=7, column=0, sticky=W)

meals = Checkbutton(foodFrame, text='Meals', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var9
                      , command=meals)
meals.grid(row=8, column=0, sticky=W)


bajjibonda = Checkbutton(foodFrame, text='Bajji/Bonda', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var10
                      , command=bajjibonda)
bajjibonda.grid(row=9, column=0, sticky=W)

# Entry Fields for Food Items

textidli = Entry(foodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_idli)
textidli.grid(row=0, column=1)

textvada = Entry(foodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_vada)
textvada.grid(row=1, column=1)

textdosa = Entry(foodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_dosa)
textdosa.grid(row=2, column=1)

textpuri = Entry(foodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_puri)
textpuri.grid(row=3, column=1)

textchapathi = Entry(foodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_chapathi)
textchapathi.grid(row=4, column=1)

textparotta = Entry(foodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_parotta)
textparotta.grid(row=5, column=1)

textrice = Entry(foodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_rice)
textrice.grid(row=6, column=1)

textminimeals = Entry(foodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_minimeals)
textminimeals.grid(row=7, column=1)

textmeals = Entry(foodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_meals)
textmeals.grid(row=8, column=1)

textbajjibonda = Entry(foodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_bajjibonda)
textbajjibonda.grid(row=9, column=1)


# Drmilk
milk = Checkbutton(drinksFrame, text='Milk', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var11
                    , command=milk)
milk.grid(row=0, column=0, sticky=W)

badammilk = Checkbutton(drinksFrame, text='Badam Milk', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var12
                     , command=badammilk)
badammilk.grid(row=1, column=0, sticky=W)

coffee = Checkbutton(drinksFrame, text='Coffee', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var13
                     , command=coffee)
coffee.grid(row=2, column=0, sticky=W)

tea = Checkbutton(drinksFrame, text='Tea', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var14
                       , command=tea)
tea.grid(row=3, column=0, sticky=W)

cooldrinks = Checkbutton(drinksFrame, text='Cool Drinks', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var15
                       , command=cooldrinks)
cooldrinks.grid(row=4, column=0, sticky=W)

waterbottle = Checkbutton(drinksFrame, text='Water Bottle', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var16
                       , command=waterbottle)
waterbottle.grid(row=5, column=0, sticky=W)


# entry fields for drink items

textmilk = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_milk)
textmilk.grid(row=0, column=1)

textbadammilk = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_badammilk)
textbadammilk.grid(row=1, column=1)

textcoffee = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_coffee)
textcoffee.grid(row=2, column=1)

texttea = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_tea)
texttea.grid(row=3, column=1)

textcooldrinks = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_cooldrinks)
textcooldrinks.grid(row=4, column=1)

textwaterbottle = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_waterbottle)
textwaterbottle.grid(row=5, column=1)


# Others

chocolate = Checkbutton(othersFrame, text='Chocolate', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var17
                       , command=chocolate)
chocolate.grid(row=0, column=0, sticky=W)

parsal = Checkbutton(othersFrame, text='Parsal', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var18
                        , command=parsal)
parsal.grid(row=1, column=0, sticky=W)

others = Checkbutton(othersFrame, text='Other', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var19
                         , command=others)
others.grid(row=2, column=0, sticky=W)


# entry fields for others

textchocolate = Entry(othersFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_chocolate)
textchocolate.grid(row=0, column=1)

textparsal = Entry(othersFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_parsal)
textparsal.grid(row=1, column=1)

textothers = Entry(othersFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_others)
textothers.grid(row=2, column=1)


# costlabels & entry fields

labelCostofFood = Label(costFrame, text='Cost of Food', font=('arial', 16, 'bold'), bg='firebrick4', fg='white')
labelCostofFood.grid(row=0, column=0)

textCostofFood = Entry(costFrame, font=('arial', 16, 'bold'), bd=6, width=14, state='readonly',
                       textvariable=costoffoodvar)
textCostofFood.grid(row=0, column=1, padx=41)

labelCostofDrinks = Label(costFrame, text='Cost of Drinks', font=('arial', 16, 'bold'), bg='firebrick4', fg='white')
labelCostofDrinks.grid(row=1, column=0)

textCostofDrinks = Entry(costFrame, font=('arial', 16, 'bold'), bd=6, width=14, state='readonly',
                         textvariable=costofdrinksvar)
textCostofDrinks.grid(row=1, column=1, padx=41)

labelCostofOthers = Label(costFrame, text='Cost of Others', font=('arial', 16, 'bold'), bg='firebrick4', fg='white')
labelCostofOthers.grid(row=2, column=0)

textCostofOthers = Entry(costFrame, font=('arial', 16, 'bold'), bd=6, width=14, state='readonly',
                        textvariable=costofothersvar)
textCostofOthers.grid(row=2, column=1, padx=41)

labelSubTotal = Label(costFrame, text='Sub Total', font=('arial', 16, 'bold'), bg='firebrick4', fg='white')
labelSubTotal.grid(row=0, column=2)

textSubTotal = Entry(costFrame, font=('arial', 16, 'bold'), bd=6, width=14, state='readonly', textvariable=subtotalvar)
textSubTotal.grid(row=0, column=3, padx=41)

labelServiceTax = Label(costFrame, text='Service Tax', font=('arial', 16, 'bold'), bg='firebrick4', fg='white')
labelServiceTax.grid(row=1, column=2)

textServiceTax = Entry(costFrame, font=('arial', 16, 'bold'), bd=6, width=14, state='readonly',
                       textvariable=servicetaxvar)
textServiceTax.grid(row=1, column=3, padx=41)

labelTotalCost = Label(costFrame, text='Total Cost', font=('arial', 16, 'bold'), bg='firebrick4', fg='white')
labelTotalCost.grid(row=2, column=2)

textTotalCost = Entry(costFrame, font=('arial', 16, 'bold'), bd=6, width=14, state='readonly',
                      textvariable=totalcostvar)
textTotalCost.grid(row=2, column=3, padx=41)

# Buttons

buttonTotal = Button(buttonFrame, text='Total', font=('arial', 14, 'bold'), fg='white', bg='red4', bd=3, padx=13,
                     command=totalcost)
buttonTotal.grid(row=0, column=0)

buttonReceipt = Button(buttonFrame, text='Receipt', font=('arial', 14, 'bold'), fg='white', bg='red4', bd=1, padx=13
                       , command=receipt)
buttonReceipt.grid(row=0, column=1)

buttonSave = Button(buttonFrame, text='Save', font=('arial', 14, 'bold'), fg='white', bg='red4', bd=3, padx=13
                    , command=save)
buttonSave.grid(row=0, column=2)

buttonReset = Button(buttonFrame, text='Reset', font=('arial', 14, 'bold'), fg='white', bg='red4', bd=3, padx=13,
                     command=reset)
buttonReset.grid(row=0, column=4)

# textarea for receipt

textReceipt = Text(recieptFrame, font=('arial', 12, 'bold'), bd=3, width=42, height=14)
textReceipt.grid(row=0, column=0)

# Calculator
operator = ''  # 7+9


def buttonClick(numbers):  # 9
    global operator
    operator = operator + numbers
    calculatorField.delete(0, END)
    calculatorField.insert(END, operator)


def clear():
    global operator
    operator = ''
    calculatorField.delete(0, END)


def answer():
    global operator
    result = str(eval(operator))
    calculatorField.delete(0, END)
    calculatorField.insert(0, result)
    operator = ''


calculatorField = Entry(calculatorFrame, font=('arial', 16, 'bold'), width=32, bd=4)
calculatorField.grid(row=0, column=0, columnspan=4)

button7 = Button(calculatorFrame, text='7', font=('arial', 16, 'bold'), fg='yellow', bg='red4', bd=6, width=6,
                 command=lambda: buttonClick('7'))
button7.grid(row=1, column=0)

button8 = Button(calculatorFrame, text='8', font=('arial', 16, 'bold'), fg='yellow', bg='red4', bd=6, width=6,
                 command=lambda: buttonClick('8'))
button8.grid(row=1, column=1)

button9 = Button(calculatorFrame, text='9', font=('arial', 16, 'bold'), fg='yellow', bg='red4', bd=6, width=6
                 , command=lambda: buttonClick('9'))
button9.grid(row=1, column=2)

buttonPlus = Button(calculatorFrame, text='+', font=('arial', 16, 'bold'), fg='yellow', bg='red4', bd=6, width=6
                    , command=lambda: buttonClick('+'))
buttonPlus.grid(row=1, column=3)

button4 = Button(calculatorFrame, text='4', font=('arial', 16, 'bold'), fg='yellow', bg='red4', bd=6, width=6
                 , command=lambda: buttonClick('4'))
button4.grid(row=2, column=0)

button5 = Button(calculatorFrame, text='5', font=('arial', 16, 'bold'), fg='red4', bg='white', bd=6, width=6
                 , command=lambda: buttonClick('5'))
button5.grid(row=2, column=1)

button6 = Button(calculatorFrame, text='6', font=('arial', 16, 'bold'), fg='red4', bg='white', bd=6, width=6
                 , command=lambda: buttonClick('6'))
button6.grid(row=2, column=2)

buttonMinus = Button(calculatorFrame, text='-', font=('arial', 16, 'bold'), fg='yellow', bg='red4', bd=6, width=6
                     , command=lambda: buttonClick('-'))
buttonMinus.grid(row=2, column=3)

button1 = Button(calculatorFrame, text='1', font=('arial', 16, 'bold'), fg='yellow', bg='red4', bd=6, width=6
                 , command=lambda: buttonClick('1'))
button1.grid(row=3, column=0)

button2 = Button(calculatorFrame, text='2', font=('arial', 16, 'bold'), fg='red4', bg='white', bd=6, width=6
                 , command=lambda: buttonClick('2'))
button2.grid(row=3, column=1)

button3 = Button(calculatorFrame, text='3', font=('arial', 16, 'bold'), fg='red4', bg='white', bd=6, width=6
                 , command=lambda: buttonClick('3'))
button3.grid(row=3, column=2)

buttonMult = Button(calculatorFrame, text='*', font=('arial', 16, 'bold'), fg='yellow', bg='red4', bd=6, width=6
                    , command=lambda: buttonClick('*'))
buttonMult.grid(row=3, column=3)

buttonAns = Button(calculatorFrame, text='Ans', font=('arial', 16, 'bold'), fg='yellow', bg='red4', bd=6, width=6,
                   command=answer)
buttonAns.grid(row=4, column=0)

buttonClear = Button(calculatorFrame, text='Clear', font=('arial', 16, 'bold'), fg='yellow', bg='red4', bd=6, width=6
                     , command=clear)
buttonClear.grid(row=4, column=1)

button0 = Button(calculatorFrame, text='0', font=('arial', 16, 'bold'), fg='yellow', bg='red4', bd=6, width=6
                 , command=lambda: buttonClick('0'))
button0.grid(row=4, column=2)

buttonDiv = Button(calculatorFrame, text='/', font=('arial', 16, 'bold'), fg='yellow', bg='red4', bd=6, width=6,
                   command=lambda: buttonClick('/'))
buttonDiv.grid(row=4, column=3)


root.mainloop()

conn.commit()
print("Records created successfully");
conn.close()


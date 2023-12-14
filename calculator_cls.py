from tkinter import Tk,Frame,Button,Label,StringVar

root = Tk()

# root.mainloop()


# step2 : adding the resolution to the screen..

# root.geometry('500x500+450+100')

# root.title("Calculator")

# root.resizable(0,0)
# root.mainloop()

# step3: Dividing the screen into 4 different frames..

# root.geometry('500x500+450+100')

# root.title("Calculator")

# root.resizable(0,0)


# frame1 = Frame(root,bg='red')
# frame1.pack(fill='both',expand=True)

# frame2 = Frame(root,bg='green')
# frame2.pack(fill='both',expand=True)

# frame3 = Frame(root,bg='blue')
# frame3.pack(fill='both',expand=True)

# frame4 = Frame(root,bg='black')
# frame4.pack(fill='both',expand=True)


# btn1 = Button(frame1,text='1',font=('Verdana',20),border=0)
# btn1.pack(fill='both',expand=True,side='left')

# btn2 = Button(frame1,text='2',font=('Verdana',20),border=0)
# btn2.pack(fill='both',expand=True,side='left')

# btn3 = Button(frame1,text='3',font=('Verdana',20),border=0)
# btn3.pack(fill='both',expand=True,side='left')

# btnplus = Button(frame1,text='+',font=('Verdana',20),border=0)
# btnplus.pack(fill='both',expand=True,side='left')


# btn4 = Button(frame2,text='4',font=('Verdana',20),border=0)
# btn4.pack(fill='both',expand=True,side='left')

# btn5 = Button(frame2,text='5',font=('Verdana',20),border=0)
# btn5.pack(fill='both',expand=True,side='left')

# btn6 = Button(frame2,text='6',font=('Verdana',20),border=0)
# btn6.pack(fill='both',expand=True,side='left')

# btnminus = Button(frame2,text='-',font=('Verdana',20),border=0)
# btnminus.pack(fill='both',expand=True,side='left')


# btn7 = Button(frame3,text='7',font=('Verdana',20),border=0)
# btn7.pack(fill='both',expand=True,side='left')

# btn8 = Button(frame3,text='8',font=('Verdana',20),border=0)
# btn8.pack(fill='both',expand=True,side='left')

# btn9 = Button(frame3,text='9',font=('Verdana',20),border=0)
# btn9.pack(fill='both',expand=True,side='left')

# btnmul = Button(frame3,text='*',font=('Verdana',20),border=0)
# btnmul.pack(fill='both',expand=True,side='left')


# btnC = Button(frame4,text='C',font=('Verdana',20),border=0)
# btnC.pack(fill='both',expand=True,side='left')

# btn0 = Button(frame4,text='0',font=('Verdana',20),border=0)
# btn0.pack(fill='both',expand=True,side='left')

# btnequal = Button(frame4,text='=',font=('Verdana',20),border=0)
# btnequal.pack(fill='both',expand=True,side='left')

# btndiv = Button(frame4,text='/',font=('Verdana',20),border=0)
# btndiv.pack(fill='both',expand=True,side='left')


# root.mainloop()


# Step4 : Defining the label

# root.geometry('500x500+450+100')

# root.title("Calculator")

# root.resizable(0,0)

# root_lbl = Label(root,text="This is Label",anchor='se')
# root_lbl.pack(fill='both',expand=True)

# frame1 = Frame(root,bg='red')
# frame1.pack(fill='both',expand=True)

# frame2 = Frame(root,bg='green')
# frame2.pack(fill='both',expand=True)

# frame3 = Frame(root,bg='blue')
# frame3.pack(fill='both',expand=True)

# frame4 = Frame(root,bg='black')
# frame4.pack(fill='both',expand=True)


# btn1 = Button(frame1,text='1',font=('Verdana',20),border=0)
# btn1.pack(fill='both',expand=True,side='left')

# btn2 = Button(frame1,text='2',font=('Verdana',20),border=0)
# btn2.pack(fill='both',expand=True,side='left')

# btn3 = Button(frame1,text='3',font=('Verdana',20),border=0)
# btn3.pack(fill='both',expand=True,side='left')

# btnplus = Button(frame1,text='+',font=('Verdana',20),border=0)
# btnplus.pack(fill='both',expand=True,side='left')


# btn4 = Button(frame2,text='4',font=('Verdana',20),border=0)
# btn4.pack(fill='both',expand=True,side='left')

# btn5 = Button(frame2,text='5',font=('Verdana',20),border=0)
# btn5.pack(fill='both',expand=True,side='left')

# btn6 = Button(frame2,text='6',font=('Verdana',20),border=0)
# btn6.pack(fill='both',expand=True,side='left')

# btnminus = Button(frame2,text='-',font=('Verdana',20),border=0)
# btnminus.pack(fill='both',expand=True,side='left')


# btn7 = Button(frame3,text='7',font=('Verdana',20),border=0)
# btn7.pack(fill='both',expand=True,side='left')

# btn8 = Button(frame3,text='8',font=('Verdana',20),border=0)
# btn8.pack(fill='both',expand=True,side='left')

# btn9 = Button(frame3,text='9',font=('Verdana',20),border=0)
# btn9.pack(fill='both',expand=True,side='left')

# btnmul = Button(frame3,text='*',font=('Verdana',20),border=0)
# btnmul.pack(fill='both',expand=True,side='left')


# btnC = Button(frame4,text='C',font=('Verdana',20),border=0)
# btnC.pack(fill='both',expand=True,side='left')

# btn0 = Button(frame4,text='0',font=('Verdana',20),border=0)
# btn0.pack(fill='both',expand=True,side='left')

# btnequal = Button(frame4,text='=',font=('Verdana',20),border=0)
# btnequal.pack(fill='both',expand=True,side='left')

# btndiv = Button(frame4,text='/',font=('Verdana',20),border=0)
# btndiv.pack(fill='both',expand=True,side='left')


# # root.mainloop()

# Step5: Writing the functionalities of each button..

root.geometry('500x500+450+100')

root.title("Calculator")

root.resizable(0,0)

str_val = StringVar()
val = ''

root_lbl = Label(root,text="This is Label",anchor='se',textvariable=str_val,font=('Verdana',20))
root_lbl.pack(fill='both',expand=True)


def btn1_isclicked():
    global val
    val  = val+'1'
    str_val.set(val)

def btn2_isclicked():
    global val
    val  = val+'2'
    str_val.set(val)

def btn3_isclicked():
    global val
    val  = val+'3'
    str_val.set(val)

def btn4_isclicked():
    global val
    val  = val+'4'
    str_val.set(val)

def btn5_isclicked():
    global val
    val  = val+'5'
    str_val.set(val)

def btn6_isclicked():
    global val
    val  = val+'6'
    str_val.set(val)

def btn7_isclicked():
    global val
    val  = val+'7'
    str_val.set(val)

def btn8_isclicked():
    global val
    val  = val+'8'
    str_val.set(val)

def btn9_isclicked():
    global val
    val  = val+'9'
    str_val.set(val)

def btn0_isclicked():
    global val
    val  = val+'0'
    str_val.set(val)

def btnplus_isclicked():
    global val
    val  = val+'+'
    str_val.set(val)

def btnminus_isclicked():
    global val
    val  = val+'-'
    str_val.set(val)

def btnmul_isclicked():
    global val
    val  = val+'*'
    str_val.set(val)

def btndiv_isclicked():
    global val
    val  = val+'/'
    str_val.set(val)

def btnC_isclicked():
    global val
    val  = ''
    str_val.set(val)

def btnequal_isclicked():
    global val
    print(val)
    print(type(val))
    val  = str(eval(val))
    str_val.set(val)



frame1 = Frame(root,bg='red')
frame1.pack(fill='both',expand=True)

frame2 = Frame(root,bg='green')
frame2.pack(fill='both',expand=True)

frame3 = Frame(root,bg='blue')
frame3.pack(fill='both',expand=True)

frame4 = Frame(root,bg='black')
frame4.pack(fill='both',expand=True)


btn1 = Button(frame1,text='1',font=('Verdana',20),border=0,command=btn1_isclicked)
btn1.pack(fill='both',expand=True,side='left')

btn2 = Button(frame1,text='2',font=('Verdana',20),border=0,command=btn2_isclicked)
btn2.pack(fill='both',expand=True,side='left')

btn3 = Button(frame1,text='3',font=('Verdana',20),border=0,command=btn3_isclicked)
btn3.pack(fill='both',expand=True,side='left')

btnplus = Button(frame1,text='+',font=('Verdana',20),border=0,command=btnplus_isclicked)
btnplus.pack(fill='both',expand=True,side='left')


btn4 = Button(frame2,text='4',font=('Verdana',20),border=0,command=btn4_isclicked)
btn4.pack(fill='both',expand=True,side='left')

btn5 = Button(frame2,text='5',font=('Verdana',20),border=0,command=btn5_isclicked)
btn5.pack(fill='both',expand=True,side='left')

btn6 = Button(frame2,text='6',font=('Verdana',20),border=0,command=btn6_isclicked)
btn6.pack(fill='both',expand=True,side='left')

btnminus = Button(frame2,text='-',font=('Verdana',20),border=0,command=btnminus_isclicked)
btnminus.pack(fill='both',expand=True,side='left')


btn7 = Button(frame3,text='7',font=('Verdana',20),border=0,command=btn7_isclicked)
btn7.pack(fill='both',expand=True,side='left')

btn8 = Button(frame3,text='8',font=('Verdana',20),border=0,command=btn8_isclicked)
btn8.pack(fill='both',expand=True,side='left')

btn9 = Button(frame3,text='9',font=('Verdana',20),border=0,command=btn9_isclicked)
btn9.pack(fill='both',expand=True,side='left')

btnmul = Button(frame3,text='*',font=('Verdana',20),border=0,command=btnmul_isclicked)
btnmul.pack(fill='both',expand=True,side='left')


btnC = Button(frame4,text='C',font=('Verdana',20),border=0,command=btnC_isclicked)
btnC.pack(fill='both',expand=True,side='left')

btn0 = Button(frame4,text='0',font=('Verdana',20),border=0,command=btn0_isclicked)
btn0.pack(fill='both',expand=True,side='left')

btnequal = Button(frame4,text='=',font=('Verdana',20),border=0,command=btnequal_isclicked)
btnequal.pack(fill='both',expand=True,side='left')

btndiv = Button(frame4,text='/',font=('Verdana',20),border=0,command=btndiv_isclicked)
btndiv.pack(fill='both',expand=True,side='left')

root.mainloop()


# '1+2-3'

# ['1', '2-3']

# ['1','2','3']

# eval() -- It will convert the string expression in mathematical expression
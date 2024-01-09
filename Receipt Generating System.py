from ast import Break
from telnetlib import IP
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.ttk import Progressbar
import tempfile
import os


#=====================Main Program===================

def main_window():
    root=Tk()
    root.title('TECH GROUP STORE')
    root.geometry('890x825+0+0')
    bg_color='#0F1425'
    root.resizable(False, False)

#=====================variables===================

    # PHONE
    IPHONE=IntVar()
    OPPO=IntVar()
    SAMSUNG=IntVar()
    HUAWEI=IntVar()
    XIAOMI=IntVar()
    Total=IntVar()

    cIp=StringVar()
    cOp=StringVar()
    cSa=StringVar()
    cHu=StringVar()
    cXi=StringVar()
    total_cost=StringVar()

    # ===========Function===============


    def total():
        if IPHONE.get()==0 and OPPO.get()==0 and SAMSUNG.get()==0 and HUAWEI.get()==0 and XIAOMI.get()==0:
            messagebox.showerror('Error','Please select number of quantity')
            
        else:
            Ip=IPHONE.get()
            Op=OPPO.get()
            Sa=SAMSUNG.get()
            Hu=HUAWEI.get()
            Xi=XIAOMI.get()

            t = float(Ip*70990+Op* 65000+Sa*81000+Hu*52999+Xi*50000)
            Total.set(Ip + Op + Sa + Hu + Xi)
            total_cost.set('PHP ' + str(round(t, 2)))

            cIp.set('PHP '+str(round(Ip * 70990, 2)))
            cOp.set('PHP '+str(round(Op*65000,2)))
            cSa.set('PHP '+str(round(Sa*81000,2)))
            cHu.set('PHP '+str(round(Hu*52999,2)))
            cXi.set('PHP '+str(round(Xi*50000,2)))

    def reset():
        IPHONE.set(0)
        OPPO.set(0)
        SAMSUNG.set(0)
        HUAWEI.set(0)
        XIAOMI.set(0)
        Total.set(0)

        cIp.set('')
        cOp.set('')
        cSa.set('')
        cHu.set('')
        cXi.set('')
        total_cost.set('')

    def exit():
        if messagebox.askyesno('Exit','Do you really want to exit'):
            root.destroy()


    title=Label(root,pady=5,text="TECH GROUP STORE",bd=12,bg=bg_color,fg='White',font=('Century Gothic', 35 ,'bold'),relief=FLAT,justify=CENTER)
    title.pack(fill=X)

    #===============Product Details=================

    F1 = LabelFrame(root, bg=bg_color,bd=15,relief=FLAT)
    F1.place(x=5, y=95,width=880,height=600)

    #=====================Heading==========================

    itm=Label(F1, text='Items', font=('Helvetic',25, 'bold',), fg='White',bg=bg_color)
    itm.grid(row=0,column=0,padx=20,pady=15)

    n=Label(F1, text='Quantity', font=('Helvetic',25, 'bold',), fg='white',bg=bg_color)
    n.grid(row=0,column=1,padx=30,pady=15)

    cost=Label(F1, text='Cost', font=('Helvetic',25, 'bold',), fg='white',bg=bg_color)
    cost.grid(row=0,column=2,padx=30,pady=15)

    #===============Product============

    iphone=Label(F1, text='IPHONE 13 PRO MAX  ', font=('Century Gothic',16,), fg='white',bg=bg_color)
    iphone.grid(row=1,column=0,padx=10,pady=15)
    i_txt=Entry(F1,font='arial 15 bold',relief=FLAT,bd=7,textvariable=IPHONE,justify=CENTER,bg='#f27348')
    i_txt.grid(row=1,column=1,padx=20,pady=15)
    ci_txt=Entry(F1,font='arial 15 bold',relief=FLAT,bd=7,textvariable=cIp,justify=CENTER,bg='#f27348')
    ci_txt.grid(row=1,column=2,padx=5,pady=15)

    oppo=Label(F1, text='OPPO FIND X5 PRO ', font=('Century Gothic',16,), fg='white',bg=bg_color)
    oppo.grid(row=2,column=0,padx=10,pady=15)
    o_txt=Entry(F1,font='arial 15 bold',relief=FLAT,bd=7,textvariable=OPPO,justify=CENTER,bg='#f9968b')
    o_txt.grid(row=2,column=1,padx=20,pady=15)
    co_txt=Entry(F1,font='arial 15 bold',relief=FLAT,bd=7,textvariable=cOp,justify=CENTER,bg='#f9968b')
    co_txt.grid(row=2,column=2,padx=5,pady=15)

    samsung=Label(F1, text='SAMSUNG GALAXY \n S22 ULTRA', font=('Century Gothic',16,), fg='white',bg=bg_color)
    samsung.grid(row=3,column=0,padx=10,pady=15)
    s_txt=Entry(F1,font='arial 15 bold',relief=FLAT,bd=7,textvariable=SAMSUNG,justify=CENTER, bg="#f2eccb")
    s_txt.grid(row=3,column=1,padx=20,pady=15)
    cs_txt=Entry(F1,font='arial 15 bold',relief=FLAT,bd=7,textvariable=cSa,justify=CENTER, bg="#f2eccb")
    cs_txt.grid(row=3,column=2,padx=5,pady=15)

    huawei=Label(F1, text='HUAWEI P50 PRO', font=('Century Gothic',16,), fg='white',bg=bg_color)
    huawei.grid(row=4,column=0,padx=10,pady=15,)
    h_txt=Entry(F1,font='arial 15 bold',relief=FLAT,bd=7,textvariable=HUAWEI,justify=CENTER, bg="#76cdcd")
    h_txt.grid(row=4,column=1,padx=20,pady=15)
    ch_txt=Entry(F1,font='arial 15 bold',relief=FLAT,bd=7,textvariable=cHu,justify=CENTER, bg="#76cdcd")
    ch_txt.grid(row=4,column=2,padx=5,pady=15)

    xiaomi=Label(F1, text='XIAOMI 12 PRO', font=('Century Gothic',16,), fg='white',bg=bg_color)
    xiaomi.grid(row=5,column=0,padx=10,pady=15)
    x_txt=Entry(F1,font='arial 15 bold',relief=FLAT,bd=7,textvariable=XIAOMI,justify=CENTER, bg='#2cced2')
    x_txt.grid(row=5,column=1,padx=20,pady=15)
    cx_txt=Entry(F1,font='arial 15 bold',relief=FLAT,bd=7,textvariable=cXi,justify=CENTER, bg='#2cced2')
    cx_txt.grid(row=5,column=2,padx=5,pady=15)

    t=Label(F1, text='TOTAL', font=('Century Gothic',16,), fg='white',bg=bg_color)
    t.grid(row=6,column=0,padx=5,pady=15)
    t_txt=Entry(F1,font='arial 15 bold',relief=FLAT,bd=7,textvariable=Total,justify=CENTER,bg='#6d6875')
    t_txt.grid(row=6,column=1,padx=20,pady=15)
    totalcost_txt=Entry(F1,font='arial 15 bold',relief=FLAT,bd=7,textvariable=total_cost,justify=CENTER,bg='#6d6875')
    totalcost_txt.grid(row=6,column=2,padx=5,pady=15)

    #=====================Receipt Window====================

    def proceed_bill():
        if IPHONE.get()==0 and OPPO.get()==0 and SAMSUNG.get()==0 and HUAWEI.get()==0 and XIAOMI.get()==0:
            messagebox.showerror('Error','Please select number of quantity')
            main_window
        else:
            total()
            receipt_window()

    def receipt_window():
        root=Tk()
        root.title('Receipt')
        root.geometry('390x600+0+0')

        def print():
            q=textarea.get('1.0','end-1c')
            filename=tempfile.mktemp('.txt')
            open(filename,'w').write(q)
            os.startfile(filename,'Print')

        def exit():
            if messagebox.askyesno('Exit','Do you really want to exit'):
                try:
                    root.destroy()
                    main_window
                except:
                    pass
                

        F2=Frame(root,relief=FLAT,bd=10)
        F2.place(width=390,height=600)
        bill_title=Label(F2,text='Receipt',font='arial 15 bold',bd=7,relief=GROOVE,bg='#0F1425',fg='white')
        bill_title.pack(fill=BOTH)
        scroll_y=Scrollbar(F2,orient=VERTICAL)
        scroll_y.pack(side=RIGHT,fill=BOTH)
        textarea=Text(F2,font='arial 13',yscrollcommand=scroll_y.set,bg="#f2eccb")
        textarea.pack(fill=BOTH)
        scroll_y.config(command=textarea.yview)

        textarea.insert(END,' \tItems \t  Quantity \tCost of Items\n')
        textarea.insert(END,f'\nIPHONE 13 PRO MAX\t{IPHONE.get()}\t{cIp.get()}')
        textarea.insert(END,f'\n\nOPPO FIND X5 PRO\t{OPPO.get()}\t{cOp.get()}')
        textarea.insert(END,f'\n\nSAMSUNG GALAXY \n S22 ULTRA \t\t{SAMSUNG.get()}\t{cSa.get()}')
        textarea.insert(END,f'\n\nHUAWEI P50 PRO\t\t{HUAWEI.get()}\t{cHu.get()}')
        textarea.insert(END,f'\n\nXIAOMI 12 PRO\t\t{XIAOMI.get()}\t{cXi.get()}')
        textarea.insert(END, f"\n\n========================================")
        textarea.insert(END,f'\nTotal Price\t\t{Total.get()}\t{total_cost.get()}')
        textarea.insert(END, f"\n=========================================")

        button=Frame(F2,bg='#0F1425',bd=20,relief=FLAT)
        button.place(x=0, y=500)
        b2=Button(button,width=20,text='Print',command=print,border=0,bg='#374255',fg='#ECECEC')
        b2.grid(row=10,column=2,padx=5,pady=5)
        b2=Button(button,width=20,text='Close Window',command=exit,border=0,bg='#374255',fg='#ECECEC')
        b2.grid(row=10,column=3,padx=5,pady=5)

    F3 =Frame(root,bg=bg_color,bd=15,relief=FLAT)
    F3.place(x=5, y=700,width=880,height=120)

    btn1 = Button(F3, text='Total', font='arial 25 bold', padx=5, pady=5, bg='#374255',fg='#ECECEC',width=8,command=total)
    btn1.grid(row=0,column=0,padx=20,pady=10)

    btn2 = Button(F3, text='Receipt', font='arial 25 bold', padx=5, pady=5, bg='#374255',fg='#ECECEC',width=8,command=proceed_bill)
    btn2.grid(row=0,column=1,padx=15,pady=10)

    btn4 = Button(F3, text='Reset', font='arial 25 bold', padx=5, pady=5, bg='#374255',fg='#ECECEC',width=8,command=reset)
    btn4.grid(row=0,column=3,padx=15,pady=10)

    btn5 = Button(F3, text='Exit', font='arial 25 bold', padx=5, pady=5, bg='#374255',fg='#ECECEC',width=8,command=exit)
    btn5.grid(row=0,column=4,padx=15,pady=10)

    w.mainloop()


# =========================Initializing frame=================

w=Tk()
w.geometry('427x250+0+0')


width_of_window = 427
height_of_window = 250
screen_width = w.winfo_screenwidth()
screen_height = w.winfo_screenheight()
x_coordinate = (screen_width/2)-(width_of_window/2)
y_coordinate = (screen_height/2)-(height_of_window/2)
w.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))
w.overrideredirect(1)

s=ttk.Style()
s.theme_use('clam')
s.configure("red.horizontal.TProgressbar",foreground='red',backgrounds='#4f4f4f')
progress=Progressbar(w,style="red.Horizontal.TProgressbar",orient=HORIZONTAL,length=500,mode='determinate')


def bar():
    l4=Label(w,text='Loading...',fg='white',bg='#0F1425')
    lst4=('Calibri (Body)',10)
    l4.config(font=lst4)
    l4.place(x=18,y=210)
    
    import time
    r=0
    for i in range(95):
        progress['value']=r
        w.update_idletasks()
        time.sleep(0.0001)
        r=r+1
    w.destroy()
    main_window()

def exit():
    if messagebox.askyesno('Exit','Do you really want to exit'):
        w.destroy()
          
progress.place(x=-10,y=235)


splash=Frame(w,width=427,height=241,bg='#0F1425').place(x=0,y=0)

# ======================splash buttons===================
button=Frame(w,bg="#0F1425",bd=15,relief=FLAT)
button.place(x=80, y=150)
b1=Button(button,width=12,height=1,text='Get Started',command=bar,border=0,fg='#374255',activebackground="#0F1425")
b1.grid(row=4,column=2,padx=10,pady=15)
b2=Button(button,width=12,height=1,text='Close Window',command=exit,border=0,fg='#374255',activebackground="#0F1425")
b2.grid(row=4,column=3,padx=10,pady=15)


l1=Label(w,text='LINTECH',fg='#f27348',bg='#0F1425')
lst1=('Century Gothic',40,'bold')
l1.config(font=lst1)
l1.place(x=107,y=68)


l3=Label(w,text='RECEIPT GENERATING SYSTEM',fg='white',bg='#0F1425')
lst3=('Calibri (Body)',12,'bold')
l3.config(font=lst3)
l3.place(x=82,y=130)




w.mainloop()


"""
formula 

Cutter Teeth / Work Teeth = (D / C) x (B / A)

"""

from tkinter import *
from tkinter import ttk,messagebox

GUI = Tk()
GUI.title('Lorenz Gear Shaper Design')
GUI.geometry('500x700')

L = ttk.Label(GUI,text='Index Gear Change Design',font=(None,20,'bold')).pack(pady=10)



L = ttk.Label(GUI,text='Gear Teeth (work)').pack()
v_work = StringVar()
E2 = ttk.Entry(GUI,textvariable=v_work,font=('tahoma',20))
E2.pack(pady=10)

L = ttk.Label(GUI,text='--------------').pack()

L = ttk.Label(GUI,text='Cutter Teeth').pack(pady=10)
v_cutter = StringVar()
v_cutter.set('66')
E1 = ttk.Entry(GUI,textvariable=v_cutter,font=('tahoma',20))
E1.pack(pady=10)

v_d = StringVar()
v_d.set('60')

v_c = StringVar()
v_c.set('60')

v_module = StringVar()
v_module.set('1.5')

L = ttk.Label(GUI,text='D Teeth').pack()
E3 = ttk.Entry(GUI,textvariable=v_d,font=('tahoma',20))
E3.pack(pady=10)

L = ttk.Label(GUI,text='C Teeth').pack()
E4 = ttk.Entry(GUI,textvariable=v_c,font=('tahoma',20))
E4.pack(pady=10)

L = ttk.Label(GUI,text='Module').pack()
E5 = ttk.Entry(GUI,textvariable=v_module,font=('tahoma',20))
E5.pack(pady=10)

def Calculate():
    cutter = float(v_cutter.get())
    work = float(v_work.get())
    d = float(v_d.get())
    c = float(v_c.get())
    module = float(v_module.get())

    a = work / (d/c)
    check = str(a)
    print(check)
    check = check.split('.')
    check = check[1][0]
    if c + d != 120:
        messagebox.showwarning('Wrong Calculate','C+D shoud be = 120')
        v_result.set('ERROR C+D')
    elif check != '0':
        messagebox.showwarning('Wrong Calculate','Ratio is Invalid!')
        v_result.set('ERROR RATIO')
    else:
        diameter = (work + 2) * module
        text = 'Change A={:.0f}\nGear Blank: {:,.2f} mm.'.format(a,diameter)
        v_result.set(text)

    


B1 = ttk.Button(GUI,text='Calculate',command=Calculate)
B1.pack(ipadx=30,ipady=20)
###############################

v_result = StringVar()
v_result.set('---------result---------')
E2 = ttk.Label(GUI,textvariable=v_result,font=('tahoma',20,'bold'))
E2.pack(pady=20)



GUI.mainloop()
from tkinter import *
from tkinter import ttk, DoubleVar,messagebox
from ttkthemes import ThemedTk

root = ThemedTk(theme="equilux")
root.title("E-liquid calculator")
import sys, os
def resource(relative_path):
    base_path = getattr(
        sys,
        '_MEIPASS',
        os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)
image = resource("flask.ico") #YOU HAVE TO ADD YOUR OWN ICON TO YOUR PROJECT FOLDER
root.iconbitmap(image)
mainframe = ttk.Frame(root, padding="3 3 5 5")
mainframe.grid(column=0, row=0,sticky="NEWS")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.resizable(False,False)
# INGREDIENT VARIABLES ---------------------------------------------------------------------------------------
total = DoubleVar(value=0)
pg_ratio = DoubleVar(value=0)
nic_percentage = DoubleVar(value=0)
pg = DoubleVar(value=0)
vg = DoubleVar(value=0)
nic_base = DoubleVar(value=0)
nic_total = DoubleVar(value=0)
# FLAVOR VARIABLES ------------------------------------------------------------------------------------------
flavor1 = DoubleVar(value=0)
flavor2 = DoubleVar(value=0)
flavor3 = DoubleVar(value=0)
flavor4 = DoubleVar(value=0)
flavor5 = DoubleVar(value=0)
flavor6 = DoubleVar(value=0)
flavor7 = DoubleVar(value=0)
flavor8 = DoubleVar(value=0)
flavor9 = DoubleVar(value=0)
flavor10 = DoubleVar(value=0)
# INGREDIENT ENTRIES ---------------------------------------------------------------------------------
total_entry = ttk.Entry(mainframe, width=6, textvariable=total)
pg_ratio_entry = ttk.Entry(mainframe, width=6, textvariable=pg_ratio)
nic_percentage_entry = ttk.Entry(mainframe, width=6, textvariable=nic_percentage)
nic_base_entry= ttk.Entry(mainframe, width=6, textvariable=nic_base)
# FLAVOR ENTRIES ------------------------------------------------------------------------------------
flavor1_entry= ttk.Entry(mainframe, width=6, textvariable=flavor1)
flavor2_entry= ttk.Entry(mainframe, width=6, textvariable=flavor2)
flavor3_entry= ttk.Entry(mainframe, width=6, textvariable=flavor3)
flavor4_entry= ttk.Entry(mainframe, width=6, textvariable=flavor4)
flavor5_entry= ttk.Entry(mainframe, width=6, textvariable=flavor5)
flavor6_entry= ttk.Entry(mainframe, width=6, textvariable=flavor6)
flavor7_entry= ttk.Entry(mainframe, width=6, textvariable=flavor7)
flavor8_entry= ttk.Entry(mainframe, width=6, textvariable=flavor8)
flavor9_entry= ttk.Entry(mainframe, width=6, textvariable=flavor9)
flavor10_entry= ttk.Entry(mainframe, width=6, textvariable=flavor10)

# INGREDIENT GRID ENTRIES -------------------------------------------------------------------------
total_entry.grid(column=2, row=1, sticky="WE")
pg_ratio_entry.grid(column=2, row=2, sticky="WE")
nic_base_entry.grid(column=2, row=3, sticky="WE")
nic_percentage_entry.grid(column=2, row=4, sticky="WE")
# FLAVOR GRID ENTRIES ---------------------------------------------------------------------------------
flavor1_entry.grid(column=3, row=1, sticky="WE")
flavor2_entry.grid(column=3, row=2, sticky="WE")
flavor3_entry.grid(column=3, row=3, sticky="WE")
flavor4_entry.grid(column=3, row=4, sticky="WE")
flavor5_entry.grid(column=3, row=5, sticky="WE")
flavor6_entry.grid(column=3, row=6, sticky="WE")
flavor7_entry.grid(column=3, row=7, sticky="WE")
flavor8_entry.grid(column=3, row=8, sticky="WE")
flavor9_entry.grid(column=3, row=9, sticky="WE")
flavor10_entry.grid(column=3, row=10, sticky="WE")

# INGREDIENT LABELS ----------------------------------------------------------------------------------
ttk.Label(mainframe, text="Total(ml)").grid(column=1, row=1, sticky=E)
ttk.Label(mainframe, text="PG ratio").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="Base"+"\n"+"nicotine"+"\n"+"(mg/ml)").grid(column=1, row=3, sticky=E)
ttk.Label(mainframe, text="Nicotine"+"\n"+"goal"+"(mg)").grid(column=1, row=4, sticky=E)
# FLAVOR LABELS ------------------------------------------------------------------------------------
ttk.Label(mainframe, text="Flavor 1").grid(column=4, row=1, sticky=E)
ttk.Label(mainframe, text="Flavor 2").grid(column=4, row=2, sticky=E)
ttk.Label(mainframe, text="Flavor 3").grid(column=4, row=3, sticky=E)
ttk.Label(mainframe, text="Flavor 4").grid(column=4, row=4, sticky=E)
ttk.Label(mainframe, text="Flavor 5").grid(column=4, row=5, sticky=E)
ttk.Label(mainframe, text="Flavor 6").grid(column=4, row=6, sticky=E)
ttk.Label(mainframe, text="Flavor 7").grid(column=4, row=7, sticky=E)
ttk.Label(mainframe, text="Flavor 8").grid(column=4, row=8, sticky=E)
ttk.Label(mainframe, text="Flavor 9").grid(column=4, row=9, sticky=E)
ttk.Label(mainframe, text="Flavor 10").grid(column=4, row=10, sticky=E)
# FUNCTIONS -------------------------------------------------------------------------------------------------
def reset():
    total.set(value=0)
    pg.set(value=0)
    vg.set(value=0)
    pg_ratio.set(value=0)
    nic_base.set(value=0)
    nic_total.set(value=0)
    nic_percentage.set(value=0)
    flavor1.set(value=0)
    flavor2.set(value=0)
    flavor3.set(value=0)
    flavor4.set(value=0)
    flavor5.set(value=0)
    flavor6.set(value=0)
    flavor7.set(value=0)
    flavor8.set(value=0)
    flavor9.set(value=0)
    flavor10.set(value=0)
def calculate():
    try:
        pg_amount= (pg_ratio.get() / 100) * total.get()# AMOUNT OF PG EXCLUDING FLAVORS,NICOTINE(BOTH ARE PG BASED)
        flavor1_final = flavor1.get() * (total.get() / 100)
        flavor2_final = flavor2.get() * (total.get() / 100)
        flavor3_final = flavor3.get() * (total.get() / 100)
        flavor4_final = flavor4.get() * (total.get() / 100)
        flavor5_final = flavor5.get() * (total.get() / 100)
        flavor6_final = flavor6.get() * (total.get() / 100)
        flavor7_final = flavor7.get() * (total.get() / 100)
        flavor8_final = flavor8.get() * (total.get() / 100)
        flavor9_final = flavor9.get() * (total.get() / 100)
        flavor10_final = flavor10.get() * (total.get() / 100)
        flavors_total = flavor1_final+flavor2_final+flavor3_final+flavor4_final+flavor5_final+flavor6_final+flavor7_final+flavor8_final+flavor9_final+flavor10_final
        nic_base_exc= (nic_percentage.get() / 100) * (total.get()) # NICOTINE , BASE MG EXCLUDED
        nic_final=round((nic_base_exc / nic_base.get()) * 100,2) # NICOTINE, BASE INCLUDED
        pg_final = round(pg_amount - nic_final - flavors_total, 2)
        vg_final = (round(total.get() - pg_amount, 2))
        def flavor_check():
            if flavor1.get() > 0 and flavor2.get()==0 and flavor3.get()==0:
                messagebox.showinfo(title="Result",message="PG(ml): "+str(pg_final)+"\n"+"VG(ml): "+str(vg_final)+"\n"+"Nicotine (ml): "+str(nic_final)+"\n"+"Flavor 1(ml): "+str(round(flavor1_final,2)))
            if flavor2.get() > 0 and flavor3.get()==0:
                messagebox.showinfo(title="Result",message="PG(ml): "+str(pg_final)+"\n"+"VG(ml): "+str(vg_final)+"\n"+"Nicotine(ml): "+str(nic_final)+"\n"+"Flavor 1(ml): "+str(round(flavor1_final,2))+"\n"+"Flavor 2(ml): "+str(round(flavor2_final,2)))
            if flavor3.get() > 0 and flavor4.get()==0:
                messagebox.showinfo(title="Result",message="PG(ml): "+str(pg_final)+"\n"+"VG(ml): "+str(vg_final)+"\n"+"Nicotine(ml): "+str(nic_final)+"\n"+"Flavor 1(ml): "+str(round(flavor1_final,2))+"\n"+"Flavor 2(ml): "+str(round(flavor2_final,2))+"\n"+"Flavor 3(ml): "+str(round(flavor3_final,2)))
            if flavor4.get() > 0 and flavor5.get()==0:
                messagebox.showinfo(title="Result",message="PG(ml): "+str(pg_final)+"\n"+"VG(ml): "+str(vg_final)+"\n"+"Nicotine(ml): "+str(nic_final)+"\n"+"Flavor 1(ml): "+str(round(flavor1_final,2))+"\n"+"Flavor 2(ml): "+str(round(flavor2_final,2))+"\n"+"Flavor 3(ml): "+str(round(flavor3_final,2))+"\n"+"Flavor 4(ml): "+str(round(flavor4_final,2)))
            if flavor5.get() > 0 and flavor6.get()==0:
                messagebox.showinfo(title="Result",message="PG(ml): "+str(pg_final)+"\n"+"VG(ml): "+str(vg_final)+"\n"+"Nicotine(ml): "+str(nic_final)+"\n"+"Flavor 1(ml): "+str(round(flavor1_final,2))+"\n"+"Flavor 2(ml): "+str(round(flavor2_final,2))+"\n"+"Flavor 3(ml): "+str(round(flavor3_final,2))+"\n"+"Flavor 4(ml): "+str(round(flavor4_final,2))+"\n"+"Flavor 5(ml): "+str(round(flavor5_final,2)))
            if flavor6.get() > 0 and flavor7.get()==0:
                messagebox.showinfo(title="Result",message="PG(ml): "+str(pg_final)+"\n"+"VG(ml): "+str(vg_final)+"\n"+"Nicotine(ml): "+str(nic_final)+"\n"+"Flavor 1(ml): "+str(round(flavor1_final,2))+"\n"+"Flavor 2(ml): "+str(round(flavor2_final,2))+"\n"+"Flavor 3(ml): "+str(round(flavor3_final,2))+"\n"+"Flavor 4(ml): "+str(round(flavor4_final,2))+"\n"+"Flavor 5(ml): "+str(round(flavor5_final,2))+"\n"+"Flavor 6(ml): "+str(round(flavor6_final,2)))
            if flavor7.get() > 0 and flavor8.get()==0:
                messagebox.showinfo(title="Result",message="PG(ml): "+str(pg_final)+"\n"+"VG(ml): "+str(vg_final)+"\n"+"Nicotine(ml): "+str(nic_final)+"\n"+"Flavor 1(ml): "+str(round(flavor1_final,2))+"\n"+"Flavor 2(ml): "+str(round(flavor2_final,2))+"\n"+"Flavor 3(ml): "+str(round(flavor3_final,2))+"\n"+"Flavor 4(ml): "+str(round(flavor4_final,2))+"\n"+"Flavor 5(ml): "+str(round(flavor5_final,2))+"\n"+"Flavor 6(ml): "+str(round(flavor6_final,2))+"\n"+"Flavor 7(ml): "+str(round(flavor7_final,2)))
            if flavor8.get() > 0 and flavor9.get()==0:
                messagebox.showinfo(title="Result",message="PG(ml): "+str(pg_final)+"\n"+"VG(ml): "+str(vg_final)+"\n"+"Nicotine(ml): "+str(nic_final)+"\n"+"Flavor 1(ml): "+str(round(flavor1_final,2))+"\n"+"Flavor 2(ml): "+str(round(flavor2_final,2))+"\n"+"Flavor 3(ml): "+str(round(flavor3_final,2))+"\n"+"Flavor 4(ml): "+str(round(flavor4_final,2))+"\n"+"Flavor 5(ml): "+str(round(flavor5_final,2))+"\n"+"Flavor 6(ml): "+str(round(flavor6_final,2))+"\n"+"Flavor 7(ml): "+str(round(flavor7_final,2))+"\n"+"Flavor 8(ml): "+str(round(flavor8_final,2)))
            if flavor9.get() > 0 and flavor10.get()==0:
                messagebox.showinfo(title="Result",message="PG(ml): "+str(pg_final)+"\n"+"VG(ml): "+str(vg_final)+"\n"+"Nicotine(ml): "+str(nic_final)+"\n"+"Flavor 1(ml): "+str(round(flavor1_final,2))+"\n"+"Flavor 2(ml): "+str(round(flavor2_final,2))+"\n"+"Flavor 3(ml): "+str(round(flavor3_final,2))+"\n"+"Flavor 4(ml): "+str(round(flavor4_final,2))+"\n"+"Flavor 5(ml): "+str(round(flavor5_final,2))+"\n"+"Flavor 6(ml): "+str(round(flavor6_final,2))+"\n"+"Flavor 7(ml): "+str(round(flavor7_final,2))+"\n"+"Flavor 8(ml): "+str(round(flavor8_final,2))+"\n"+"Flavor 9(ml): "+str(round(flavor9_final,2)))
            if flavor10.get() > 0:
                messagebox.showinfo(title="Result",message="PG(ml): "+str(pg_final)+"\n"+"VG(ml): "+str(vg_final)+"\n"+"Nicotine(ml): "+str(nic_final)+"\n"+"Flavor 1(ml): "+str(round(flavor1_final,2))+"\n"+"Flavor 2(ml): "+str(round(flavor2_final,2))+"\n"+"Flavor 3(ml): "+str(round(flavor3_final,2))+"\n"+"Flavor 4(ml): "+str(round(flavor4_final,2))+"\n"+"Flavor 5(ml): "+str(round(flavor5_final,2))+"\n"+"Flavor 6(ml): "+str(round(flavor6_final,2))+"\n"+"Flavor 7(ml): "+str(round(flavor7_final,2))+"\n"+"Flavor 8(ml): "+str(round(flavor8_final,2))+"\n"+"Flavor 9(ml): "+str(round(flavor9_final,2))+"\n"+"Flavor 10(ml): "+str(round(flavor10_final,2)))
        flavor_check()
    except TclError:
        messagebox.showerror(title="Error",message="Only numbers are allowed")
        reset()
    except ZeroDivisionError:
        messagebox.showerror(title="Error",message="Can't divide with zero")
        reset()
# --------------------------------------------------------------------------------------------------
ttk.Button(mainframe, text="Sum", width=6, command=calculate).grid(column=1, row=9, sticky=E)
ttk.Button(mainframe, text="Reset",width=6, command=reset).grid(column=1, row=10, sticky=E)
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=3)
total_entry.focus()
root.mainloop()
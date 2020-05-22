# -*- coding: utf-8 -*-
"""
Created on Thu May 21 15:20:52 2020

@author: SIMEON
"""

# import the datetime library to use date format
import datetime as dt
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
top = Tk()
top.title("BMI Calculator")
#top.geometry("300x300")

#display the intro
intro = Label(top, text ="This is a Body mass index calculator", font = 33)
intro.grid(row = 0, column = 0, sticky = W, pady = 2, columnspan = 2)

# function to display the current date
r_today = dt.date.today()

# format and print the current date in a readable way
s_today = f"{r_today: %A, %B %d, %Y the number %j day of %Y} "
Tdatealert = StringVar()
Tdate = Label(top, textvariable = Tdatealert, relief = RAISED )
Tdatealert.set ("Today's Date is \n" + s_today)
Tdate.grid( row = 1, column = 0, sticky = W, pady = 2, columnspan = 2)


#Entry for name 
name = Label(top, text = "What is Your name")
name.grid( row = 2, column = 0, sticky = W, pady = 2)

Ename = Entry(top)
Ename.grid(row = 2, column = 1, pady = 2)

#Ename.place(x=120, y=70)

'''
Enamevar = StringVar()
outname = Label(top, textvariable = Enamevar)
Enamevar.set (Ename)
outname.pack( side = LEFT)
'''

#Entry for Date of birth
dob = Label(top, text = "Let us get your Date of Birth")
dob.grid( row = 3, column = 0, sticky = W, pady = 2, columnspan = 2)
#dob.place(x=5, y=100)
yob = Label(top, text = "Year")
yob.grid( row = 4, column = 0, sticky = W, pady = 2 )
Eyob = Entry(top)
Eyob.grid(row = 4, column = 1, pady = 2 )
#r_yob = Eyob.get()

#month
mob = Label(top, text = "month")
mob.grid( row = 5, column = 0, sticky = W, pady = 2 )
#Emob = Entry(top)
#Emob.grid(row = 5, column = 1, pady = 2)
mmb = Spinbox(top, from_ = 1, to = 12)
mmb.grid (row = 5, column = 1, sticky = W, pady = 2)
#r_mob = mmb.get()
             
#day
ddob = Label(top, text = "Day")
ddob.grid( row = 6, column = 0, sticky = W, pady = 2)
#Eddob = Entry(top)
#Eddob.grid(row = 6, column = 1, pady = 2)
ddb = Spinbox(top, from_ = 1, to = 31)
ddb.grid (row = 6, column = 1, sticky = W, pady = 2)
#r_dob = ddb.get()

#output panel
output = Label (top, text = "Your Results Will show Here")
output.grid(row = 0, column = 3, pady = 2, rowspan = 10, columnspan = 5  )

#Entry height and weight
calcintro = Label(top, text = "Let us get your Height and Weight")
calcintro.grid( row = 7, column = 0, sticky = W, pady = 2, columnspan = 2)

#height
height = Label(top, text = "Your Height (in Meters)")
height.grid( row = 8, column = 0, sticky = W, pady = 2 )
Eheight = Entry(top)
Eheight.grid(row = 8, column = 1, pady = 2 )

#weight
weight = Label(top, text = "Your Weight (in KG)")
weight.grid( row = 9, column = 0, sticky = W, pady = 2 )
Eweight = Entry(top)
Eweight.grid(row = 9, column = 1, pady = 2 )

def bmi():
       
    try:
        Rname = Ename.get()
        r_yob = int(Eyob.get())
        r_mob = int(mmb.get())
        r_dob = int(ddb.get())
        
        dob = dt.date( r_yob, r_mob, r_dob)
        age = (r_today - dob)
# convert the the differences to days only
        age_days = age.days
# convert the number of days to years by using floor division
        years_old = age_days // 365
# convert the number of days to years by using modulus division, then to months by using floor
        months_old = (age_days % 365) // 30
        Yourage = Label( top, text =  f" {Rname} You are {years_old} years and {months_old} Months old")
        Yourage.grid(row = 5, column = 5)
    except:
         messagebox.showinfo( "Something is not right", "Please check your inputs")
    try:    
    #BMI calculate
        r_height = float (Eheight.get())
        r_weight = float (Eweight.get())
        
        bmi_calc = r_weight / (r_height * r_height)
        
        # using  f string to format the output. .2f=2 decimal place
        r_bmi = f""" your Body mass index is {bmi_calc:.2f} Kg/m\u00b2 """
        Yourbmi = Label (top, text =r_bmi)
        Yourbmi.grid(row = 6, column = 5)
        
    except:
        messagebox.showinfo( "Something is not right", "Please enter a numeric value")
        # check if overweight, Normal or Underweight
    ovw = 25.0
    if bmi_calc >= ovw:
        over = Label( top, text =  f" sorry {Rname} You are Overweight")
        over.grid(row = 7, column = 5)
       
    elif (bmi_calc >= 18.5 and bmi_calc <= 24.9):
        norm = Label( top, text =  f" Great {Rname} Your BMI Appears Normal")
        norm.grid(row = 7, column = 5)
       
    else:
        under = Label( top, text =  f" sorry {Rname} You are underweight")
        under.grid(row = 7, column = 5)
        
#Calculte button
calc = Button(top, text = "Calculate", command = bmi)
calc.grid(row = 10, column = 1, sticky = W, pady = 4)



top.mainloop()
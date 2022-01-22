# In[1]:


import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mess
import tkinter.simpledialog as tsd
import cv2,os
import csv
import numpy as np
from PIL import Image
import pandas as pd
import datetime
import time



def tick():
    time_string = time.strftime('%H:%M:%S')
    clock.config(text=time_string)
    clock.after(200,tick)



ts = time.time()
date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
day,month,year=date.split("-")

mont={'01':'January',
      '02':'February',
      '03':'March',
      '04':'April',
      '05':'May',
      '06':'June',
      '07':'July',
      '08':'August',
      '09':'September',
      '10':'October',
      '11':'November',
      '12':'December'
      }


# In[15]:


window = tk.Tk()
window.geometry("1280x720")
window.resizable(True,False)
window.title("Attendance System")
window.configure(background='#CAC9F2')

frame1 = tk.Frame(window, bg="#8985F2")
frame1.place(relx=0.11, rely=0.17, relwidth=0.39, relheight=0.80)

frame2 = tk.Frame(window, bg="#8985F2")
frame2.place(relx=0.51, rely=0.17, relwidth=0.38, relheight=0.80)

message3 = tk.Label(window, text="GHRCE ATTENDANCE SYSTEM" ,fg="Black",bg="#CAC9F2" ,width=55 ,height=1,font=('Kollektif', 29, ' bold '))
message3.place(x=15, y=10)

frame3 = tk.Frame(window, bg="#c4c6ce")
frame3.place(relx=0.52, rely=0.09, relwidth=0.13, relheight=0.07)

frame4 = tk.Frame(window, bg="#c4c6ce")
frame4.place(relx=0.36, rely=0.09, relwidth=0.18, relheight=0.07)

datef = tk.Label(frame4, text = day +"-"+ mont[month]+"-"+year+"  |", fg="Black",bg="#CAC9F2" ,width=55 ,height=1,font=('Kollektif', 18))
datef.pack(fill='both',expand=2)

clock = tk.Label(frame3,fg="Black",bg="#CAC9F2" ,width=55 ,height=1,font=('Kollektif', 18))
clock.pack(fill='both',expand=1)
tick()

head2 = tk.Label(frame2, text="                                 Sign-up                                                ", fg="black",bg="#FFD700" ,font=('Kollektif', 17, ' bold ') )
head2.grid(row=0,column=0)

head1 = tk.Label(frame1, text="                                     Login                                          ", fg="black",bg="#FFD700" ,font=('Kollektif', 17, ' bold ') )
head1.place(x=0,y=0)

lbl = tk.Label(frame2, text="Enter ID",width=20  ,height=1  ,fg="#FFFFFF"  ,bg="#8985F2" ,font=('Kollektif', 17, ' bold ') )
lbl.place(x=-70, y=55)

txt = tk.Entry(frame2,width=32 ,fg="black",font=('Kollektif', 15, ' bold '))
txt.place(x=30, y=88)

lbl2 = tk.Label(frame2, text="Enter Name",width=20  ,fg="#FFFFFF"  ,bg="#8985F2" ,font=('Kollektif', 17, ' bold '))
lbl2.place(x=-50, y=135)

txt2 = tk.Entry(frame2,width=32 ,fg="black",font=('Kollektif', 15, ' bold ')  )
txt2.place(x=30, y=173)

message1 = tk.Label(frame2, text=" Take Images  |  Save Profile" ,bg="#BCBCD1" ,fg="#FFFFFF"  ,width=36 ,height=1, activebackground = "yellow" ,font=('Kollektif', 15, ' bold '))
message1.place(x=20, y=230)

message = tk.Label(frame2, text="" ,bg="#BCBCD1" ,fg="#FFFFFF"  ,width=36,height=1, activebackground = "yellow" ,font=('Kollektif', 15, ' bold '))
message.place(x=20, y=465)

lbl3 = tk.Label(frame1, text="Attendance",width=20  ,fg="#FFFFFF"  ,bg="#8985F2"  ,height=1 ,font=('Kollektif', 17, ' bold '))
lbl3.place(x=105, y=106.5)

res=0
exists = os.path.isfile("StudentDetails\StudentDetails.csv")
if exists:
    with open("StudentDetails\StudentDetails.csv", 'r') as csvFile1:
        reader1 = csv.reader(csvFile1)
        for l in reader1:
            res = res + 1
    res = (res // 2) - 1
    csvFile1.close()
else:
    res = 0
message.configure(text='Total Registrations  : '+str(res))


# In[16]:


menubar = tk.Menu(window,relief='ridge')
filemenu = tk.Menu(menubar,tearoff=0)
filemenu.add_command(label='Change Password')
filemenu.add_command(label='Contact Us')
filemenu.add_command(label='Exit')
menubar.add_cascade(label='Help',font=('times', 29, ' bold '),menu=filemenu)


# In[17]:


################## TREEVIEW ATTENDANCE TABLE ####################

tv= ttk.Treeview(frame1,height =13,columns = ('name','date','time'))
tv.column('#0',width=82)
tv.column('name',width=130)
tv.column('date',width=133)
tv.column('time',width=133)
tv.grid(row=2,column=0,padx=(0,0),pady=(150,0),columnspan=4)
tv.heading('#0',text ='ID')
tv.heading('name',text ='NAME')
tv.heading('date',text ='DATE')
tv.heading('time',text ='TIME')


# In[18]:


###################### SCROLLBAR ################################

scroll=ttk.Scrollbar(frame1,orient='vertical',command=tv.yview)
scroll.grid(row=2,column=4,padx=(0,100),pady=(150,0),sticky='ns')
tv.configure(yscrollcommand=scroll.set)


# In[19]:


###################### BUTTONS ##################################

clearButton = tk.Button(frame2, text="Clear",fg="black"  ,bg="#BCBCD1"  ,width=11 ,activebackground = "white" ,font=('times', 11, ' bold '))
clearButton.place(x=335, y=86)
clearButton2 = tk.Button(frame2, text="Clear" ,fg="black"  ,bg="#BCBCD1"  ,width=11 , activebackground = "white" ,font=('times', 11, ' bold '))
clearButton2.place(x=335, y=172)    
takeImg = tk.Button(frame2, text="Take Images",fg="black"  ,bg="#FFD700"  ,width=34  ,height=1, activebackground = "white" ,font=('Kollektif', 15))
takeImg.place(x=50, y=300)
trainImg = tk.Button(frame2, text="Save Profile",fg="black"  ,bg="#FFD700"  ,width=34  ,height=1, activebackground = "white" ,font=('Kollektif', 15))
trainImg.place(x=50, y=380)
trackImg = tk.Button(frame1, text="Take Attendance"  ,fg="black"  ,bg="#BCBCD1"  ,width=35  ,height=1, activebackground = "white" ,font=('Kollektif', 15, ' bold '))
trackImg.place(x=35,y=55)
quitWindow = tk.Button(frame1, text="Quit"  ,fg="#FFFFFF"  ,bg="#CD1C1C"  ,width=35 ,height=1, activebackground = "white" ,font=('Kollektif', 15, ' bold '))
quitWindow.place(x=30, y=450)


# In[20]:


##################### END ######################################

window.configure(menu=menubar)
window.mainloop()

####################################################################################################


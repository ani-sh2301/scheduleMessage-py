from tkinter import *
from tkinter.scrolledtext import ScrolledText
import pywhatkit as pwk

mainWin=Tk()
mainWin.title("Schedule Whatsapp Message")
mainWin.configure(bg="White")
mainWin.minsize(width=600,height=500)

mobile_num=StringVar()
time_hours=StringVar()
time_min=StringVar()
message_text=StringVar()
CheckVar1 = IntVar()
var = StringVar()



def clr():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(1.0,END)

#def close_tab():

def send():
    num=mobile_num.get()
    t_h=int(time_hours.get())
    t_m=int(time_min.get())
    close=CheckVar1.get()
    message_text=e4.get('1.0', 'end-1c')

    try:
        if(close):
            pwk.sendwhatmsg("+91"+num,message_text,t_h,t_m,15,True,5)
        else:
           pwk.sendwhatmsg(num,message_text,t_h,t_m,15,False)

        var.set("Message Sent")
    except:
        var.set("Message NOT Sent")




headFrame=Frame(mainWin,bg="White",bd="0")
headFrame.pack()
l1=Label(headFrame,text="SCHEDULE YOUR WHATSAPP MESSAGE", font=("Calibri", 18), fg="Green",bd="0",bg="White")
l1.grid(row="1",column="1",pady="16")

Logo=PhotoImage(file="C:/Users/Aniket/Pictures/Wlogo.png")
im=Label(headFrame, image=Logo, bd="0")
im.grid(row="1",column="2",padx="16",pady="16")


detailFrame=Frame(mainWin,bg="White",pady="30")
detailFrame.place(x="64",y="100")
#-----------------------------------------------------
ck1=Frame(detailFrame,bg="White",pady="30")
ck1.pack(side=LEFT)

d1=Label(ck1,text="Mobile Number", bg="White",font=("Bold"))
d1.grid(row="0",column="1")

e1=Entry(ck1,bd="1", bg="White",textvariable=mobile_num)
e1.grid(row="0",column="2", padx="16")
#---------------------------------------------------
#Time heading
sh=Label(ck1,text="   TIME    ", bg='White',font=("Bold"))
sh.grid(row="1",column="1",pady="16")
#----------------------------------------------------

d2=Label(ck1,text="Hours", bg="White",font=("Bold"))
d2.grid(row="2",column="1",pady="16")

e2=Spinbox(ck1,from_="00",textvariable=time_hours,to="22",bd="1", bg="White",width="4")
e2.grid(row="2",column="2", padx="16")

#-----------------------------------------------------
d3=Label(ck1,text="Minutes", bg="White",font=("Bold"))
d3.grid(row="3",column="1",pady="16")

e3=Spinbox(ck1,from_="00",textvariable=time_min,to="60",bd="1", bg="White",width="4")
e3.grid(row="3",column="2", padx="16")

#----------------------------------------------------
#Message
ck2=Frame(detailFrame,bg="White",pady="30")
ck2.pack(side=LEFT,padx="32")

d4=Label(ck2,text="Message", bg='White',font=("Bold"))
d4.grid(row="0",column="1",pady="16")

e4=ScrolledText(ck2,wrap=WORD,width=50, height=8)
e4.grid(row="0",column="2",pady="16",padx="16")
e4.focus()

ct = Checkbutton(ck2, text = "Close Tab After Sending Message", variable = CheckVar1,onvalue = 1, offvalue = 0,bg="White")
ct.grid(row="3",column="2")

clear_button=Button(ck2,text="Clear",command=clr)
clear_button.grid(row="5",column="3",pady="32")

send_button=Button(ck2,text="Send",bg="Green",fg="white",command=send)
send_button.grid(row="5",column="4",padx="24",pady="32")

label = Message( ck2, textvariable=var, relief=RAISED,font=("Bold"),fg="Blue" , width="10")
label.grid(row="6",column="2")


#---------------------------------------------------------







mainWin.mainloop()

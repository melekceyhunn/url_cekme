from tkinter import *
import datetime
def check_it():
    dosya=open("usom.txt","r")
    icerik=dosya.read()
    dosya.close()
    ip=entry1.get()
    bugun=datetime.datetime.now()
    if str(ip) in icerik:
       dosya=open("log.txt","a")
        yazi=str(ip)+"zararli\ntarih:"+str(bugun)+"\n"
        dosya.write(yazi)
        dosya.close()
        v.set("ip zaralidir")
    else:
        dosya= open("log.txt","a")
        yazi=str(ip)+"zararli değil\n tarih:"+str(bugun)+"\n"
        dosya.write(yazi)
        dosya.close()
        v.set("ip zararli değildir")

top=Tk()
top.title("USOM IP CHECK")
B=Button(top,text="check it",command="check_it")
B.place(x=50,y=50)
B.pack()
label1=Label(top,text="enter the ip address to check")
label1.place(x=50,y=80)
label1.pack()
entry1=Entry(top)
entry1.place(x=50,y=90)
entry1.pack()
v=StringVar()
entry2=Entry(top,textvariable=v)
entry2.place(x=0,y=100)
entry2.pack()
top.mainloop()

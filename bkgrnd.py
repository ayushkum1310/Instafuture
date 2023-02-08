from tkinter import *
import pymongo
import pandas as pd
from tkinter import filedialog
import tkinter.messagebox as tmsg
from PIL import Image,ImageTk

root=Tk()
root.geometry("450x450")
root.maxsize(450,450)
root.minsize(300,300)
root.iconbitmap(default="1.ico")
root.title("Instafuture")
root.configure(bg="#EEEE3B")


image=Image.open("3.jpg")
photo=ImageTk.PhotoImage(image)
c=Canvas(root,bg="#EEEE3B")
# filename=PhotoImage(file="photo")
bg=Label(root,image=photo)
bg.place(x=0,y=0,relheight=1,relwidth=1)



def fileopen():
    global a
    a=filedialog.askopenfilename(title="Select your csv file",filetypes=[("Csv","*.csv"),("Excel","*.xlsx")])
    tmsg.showinfo("Sucessfull","Your precious data is sucessfully loaded in our system")
         
def sendpacket():
    
    client=pymongo.MongoClient("mongodb://localhost:27017/")
    db=client[name.get().replace(" ","_")]
    collection=db[name.get()]
    distis={
        "Name":name.get(),
        "Phoneno":number.get(),
        "Mail":mail.get(),
        "Gender":sex.get(),
        "Addres":ex.get(),
        "Problem_Statement":problem.get()
    }
    collection.insert_one(distis)
    collection2=db[f"data{collection}"]
    Dictonar=pd.read_csv(f"{a}",index_col=[0])
    all=Dictonar.to_dict(orient='records')
    
    
    collection2.insert_many(all)
    tmsg.showinfo("Sucessfully","Your data is sucessfully uploaded to our system")

    

def quit():

    global root

    root.quit()

# Photo=PhotoImage(file="1.png")
# L1=Label(image=Photo)
# L1.pack(row=1,column=6)
Label(root,text="Enter Name :",font="Trajan 14 bold",fg="#adff2f",bg="#181c1d").grid(row=0,column=2)
Label(root,text="Enter Contact no :",font="Trajan 14 bold",fg="#adff2f",bg="#181c1d").grid(row=1,column=2)
Label(root,text="Enter email:",font="Trajan 14 bold",fg="#adff2f",bg="#191d1e").grid(row=2,column=2)
Label(root,text="Enter Gender :",font="Trajan 14 bold",fg="#adff2f",bg="#191d1e").grid(row=3,column=2)
Label(root,text="Enter Address:",font="Trajan 14 bold",fg="#adff2f",bg="#181c1d").grid(row=4,column=2)
Label(root,text="Problem statement :",font="Trajan 14 bold",fg="#adff2f",bg="#181c1d").grid(row=5,column=2)

name=StringVar()
number=StringVar()
mail=StringVar()
sex=StringVar()
ex=StringVar()
Choice=IntVar()
problem=StringVar()


nameentry=Entry(root,textvariable=name,bg="#ebebe0")
numberentry=Entry(root,textvariable=number,bg="#ebebe0")
mailentry=Entry(root,textvariable=mail,bg="#ebebe0")
sexentry=Entry(root,textvariable=sex,bg="#ebebe0")
exentry=Entry(root,textvariable=ex,bg="#ebebe0")
Problementry=Entry(root,textvariable=problem,bg="#ebebe0")
Choiseentry=Checkbutton(root,text="I accept's all T&c",font="bold",variable=Choice,bg="#181c1d",fg="#adff2f")



nameentry.grid(row=0,column=4)
numberentry.grid(row=1,column=4)
mailentry.grid(row=2,column=4)
sexentry.grid(row=3,column=4)
exentry.grid(row=4,column=4)
Problementry.grid(row=5,column=4)

Label(root,text="choose your data you want to send",font="Trajan 8 bold",pady=5,bg="#191d1e",fg="#adff2f").grid(row=7,column=2)
F1=Frame(root,border=10,relief=RAISED,bg="#181c1d")
# root.wm_attributes("-transparentcolor",F1)


F1.grid(row=8,column=2,sticky="w")
b1=Button(F1,text="Browse",command=fileopen,bg="#181c1d",fg="#adff2f")

b1.pack(padx=20)
Label(F1,text="Selct only csv file format",font="Trajan 8 bold",pady=10,fg="#adff2f",bg="#181c1d").pack(side=TOP)


Choiseentry.grid(row=10,column=2,sticky="w",padx=5)

Label(root,text="Press submit To submit your data",font="Trajan 8 bold",pady=10,bg="#181c1d",fg="#adff2f").grid(row=12,column=2)

f2=Frame(root,border=12,relief=SUNKEN,bg="#181c1d")
f2.grid(row=15,column=2,sticky="w")

b2=Button(f2,text="Submit",command=sendpacket,bg="#adff2f").pack()

f3=Frame(root,border=10,bg="#181c1d")
f3.grid(row=22,column=8,sticky="e")
eve=Button(f3,text="Quit",bg="#adff2f",fg="black",command=quit)

eve.pack()



# def khali():
#     print("hello")

# mainmenu=Menu(root)
# m1=Menu(mainmenu,tearoff=0)
# m1.add_command(label="new",command=khali)    
# m1.add_command(label="open",command=khali)    
# m1.add_command(label="save",command=khali)    
# m1.add_command(label="saveas",command=khali)  
# root.config(menu=mainmenu)
# mainmenu.add_cascade(label="file",menu=m1)  


Label(root,text="You will get your result at your mail Id ",font="Trajan 8 bold",pady=10,bg="#181c1d",fg="#adff2f").grid(row=22,column=2,sticky="s")

root.mainloop()
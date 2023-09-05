import random
import string
from tkinter import *
import customtkinter

codsoft = Tk()

codsoft.title("Random Password Generate Application")
codsoft.geometry("350x450")
codsoft.maxsize(350,450)
codsoft.minsize(350,450)
codsoft.config(bg="#14193c")

label_title = Label(codsoft, text="Password Generator",fg="white",bg="#14193c", padx="113", font=("white, Arial Black Underline",19))
label_title.pack()
label_password = Label(codsoft, text="Select Your Password",fg="white",font= ('Arial  12 underline'))
label_password.config(bg="#14193c")
label_password.pack()
def selection():
    selection = choice_password.get()

choice_password = IntVar()
radio_button = Radiobutton(codsoft, text=" Poor password",variable= choice_password ,value=1, font=("Bell MT ",12 ), pady=2,command=selection)
radio_button.pack(pady=2)
radio_button.config(bg="#14193c",fg="white")
radio_button = Radiobutton(codsoft, text=" Average password",variable= choice_password ,value=2, font=("Bell MT ",12), pady=2,command=selection)
radio_button.pack(side=TOP, fill=X,pady=2)
radio_button.config(bg="#14193c",fg="white",pady=2)
radio_button = Radiobutton(codsoft, text=" Strong password",variable= choice_password ,value=3,  font=("Bell MT ",12), pady=2,command=selection)
radio_button.pack(pady=2)
radio_button.config(bg="#14193c",fg="white")
Label_text = Label(codsoft,text="Enter Your Password")
Label_text.config(bg="#14193c",fg="white")
Label_text.pack(pady=10)

val = IntVar()
spinlength = Spinbox(codsoft,from_=8,to_=29,textvariable = val,width=30,bg="#14193c")
spinlength.config(bg="#14193c",fg="white")
spinlength.pack(pady=5)
def callback():
    result.config(text=passgen())

result = Message(codsoft,text="                            ",relief=RAISED, width=200, font="bold 15",pady=8,)
result.config(bg="#84e0fc")
button_submit = customtkinter.CTkButton(master=codsoft,text="Password Generate",corner_radius=8,width=200,height=30,font=("Arial",20),border_spacing=10,command=callback)
button_submit.pack(padx=20,pady=40)
result.pack()

Poor_Password = string.ascii_uppercase + string.ascii_lowercase
Average_Password = string.ascii_uppercase + string.ascii_lowercase + string.digits
Strong_Password = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
def passgen():
    if choice_password.get() == 1:
        return "".join(random.sample(Poor_Password,val.get()))
    elif choice_password.get() == 2:
        return "".join(random.sample(Average_Password,val.get()))
    elif choice_password.get() == 3:
        return "".join(random.sample(Strong_Password,val.get()))

codsoft.mainloop()

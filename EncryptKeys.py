from tkinter import *
import base64
from tkinter import messagebox
import tkinter.font as font

def encode(key, messg):                         # Defining a function
    enc = []                                    # Waiting for call
    for i in range(len(messg)):                 # In range of .. 
        list_key = key(i % len(key))            
        list_encd = chr((ord(messg[i]) +        
                    ord(list_key)) % 256)
        enc.append(list_encd)                   # Calling "enc" to append list_encd 
    return base64.urlsafe_b64decode("".join(enc).encode()).decode()

def decode(key, code):
    dec = []
    enc = base64.urlsafe_b64decode(code).decode()
    for i in range(len(enc)):
        list_key = key(i % len(key))
        list_dec = chr((256 + ord(enc[i]) - ord(list_key)) % 256)

        dec.append(list_dec)
    return "".join(dec)

wn = Tk()
wn.geometry("500x500")
wn.configure(bg='antique white')
wn.title("Aisak - Encrypt and Decrypt Messages")

Messages = StringVar()
key = StringVar()
mode = IntVar()
Output = StringVar()

headingFrame1 = Frame(wn,bg="gray91",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.7,relheight=0.16)

headingLabel1 = Label(headingFrame1, text=" Welcome to Encryption and \n Decryption", fg='gray19', 
font=('Courier',15,'bold'))
headingLabel1.place(relx=0,rely=0, relwidth=1,relheight=1)


label1 = Label(wn, text="Enter the Message", font=('Courier',10))
label1.place(x=10, y=150)

msg = Entry(wn, textvariable=Message, width=35, font=('calibre',10,'normal'))
msg.place(x=200, y=150)

label2 = Label(wn, text='Enter the key',font=('Courier',10))
label2.place(x=10, y=200)

InpKey = Entry(wn, textvariable=key, width=35, font=('calibre',10,'normal'))
InpKey.place(x=200, y=200)

label3 = Label(wn, text="Check one of encrypt or decrypt", font=('Courier',10))
label3.place(x=10, y=250)

Radiobutton(wn, text="Encrypt", variable=mode, value=1).place(x=100, y=300)
Radiobutton(wn, text="Decrypt", variable=mode, value=2).place(x=200, y=300)

label3 = Label(wn, text="Result", font=('Courier',10))
label3.place(x=10, y=350)

res = Entry(wn, textvariable=Output, width=35, font=('calibre',10))
res.place(x=200, y=350)

#Show message function
def Result():
    msg = Message.get()
    k = key.get()
    i = mode.get()
    if (i==1):
        Output.set(encode(k, msg))
    elif (i==2):
        Output.set(decode(k, msg))
    else:
        messagebox.showinfo("Please choose one of 'Encryption' or 'Decryption'. Try again. ")

#Reset function
def Reset():
    Message.set("")
    key.set("")
    mode.set("")
    Output.set("")


ShowBtn = Button(wn, text = "Show Message", bg = 'blue',
fg = 'dark cyan', width = 15, height = 1, command = Result)
ShowBtn['font'] = font.Font( size = 12)
ShowBtn.place(x=180, y = 400)

ResetBtn = Button(wn, text = "Reset", bg = 'lavender', fg = 'black', width = 15, height = 1, command =Reset)
ResetBtn['font'] = font.Font( size = 12)
ResetBtn.place(x=15, y=400)

ExitBtn = Button(wn, text = "Exit", bg ='old lace', fg = 'black', width = 15, height = 1, command = wn.destroy)
ExitBtn['font'] = font.Font( size = 12)
ExitBtn.place(x=345, y=400)


wn.mainloop()
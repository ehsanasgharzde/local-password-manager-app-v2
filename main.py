# ---------------------------- LIBRARIES ------------------------------- #
from tkinter import *
from random import *
from tkinter import messagebox
import json
import pyperclip


# ---------------------------- CONSTANTS ------------------------------- #
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '(', ')', '*', '+', '-', '_']
DARKBLUE = "#001E6C"
BLUE = "#035397"
LIGHTBLUE = "#5089C6"
GRAY = '#787A91'
WHITE = '#F9F9F9'

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def passwordgenerator():
    passwordinput.delete(0, END)
    
    letterlist = [choice(LETTERS) for char in range(randint(8, 10))]
    numberlist = [choice(NUMBERS) for char in range(randint(2, 4))]
    symbollist = [choice(SYMBOLS) for char in range(randint(2, 4))]

    charlist = letterlist + numberlist + symbollist
    shuffle(charlist)
    
    password = ''.join(charlist)

    passwordinput.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = websiteinput.get().title()
    username = usernameinput.get()
    password = passwordinput.get()

    datadict = {
        website: {
            'e-mail': username,
            'password': password,
        }
    }

    if len(website) != 0 and len(username) != 0 and len(password) != 0:

        confirm = messagebox.askokcancel(title=website, message=f'These are the entered details: \nUsername/e-mail: {username} '
                                                                    f'\nPassword: {password} \nDo you confirm?')
        if confirm:
            try:
                with open('PasswordLog.json', 'r') as file:
                    log = json.load(file)

            except FileNotFoundError:
                with open('PasswordLog.json', 'w') as file:
                    json.dump(datadict, file, indent=4)
            else:
                log.update(datadict)
                with open('PasswordLog.json', 'w') as file:
                    json.dump(log, file, indent=4)
            finally:
                websiteinput.delete(0, END)
                usernameinput.delete(0, END)
                passwordinput.delete(0, END)
    else:
        messagebox.showerror(title='Error: Empty Fields!', message='Please fill in all fildes.')

# ---------------------------- SEARCH ENGINE ------------------------------- #
def search():
    web = websiteinput.get().title()
    try:
        with open('passwordLog.json', 'r') as file:
            log = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title='Error: File not found!', message='No Data file found.')
    else:
        if web in log:
            value = log[web]
            email = value['e-mail']
            pword = value['password']
            messagebox.showinfo(title=web, message=f'Username/e-mail: {email}\nPassword: {pword}')

        elif web not in log.items():
            messagebox.showerror(title='Error: Data not found!', message='There is no Data related to this site.')
            

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.minsize(512, 512)
window.config(bg=LIGHTBLUE)

canvas = Canvas(width=256, height=256, highlightthickness=0, bg=LIGHTBLUE)
image = PhotoImage(file='locklogo.png')
canvas.create_image(128, 128, image=image)
canvas.place(x=128, y=50)

websitelabel = Label(text='Website:', highlightthickness=0, bg=LIGHTBLUE)
websitelabel.place(x=25, y=340)

usernamelabel = Label (text='Username/e-mail:', highlightthickness=0, bg=LIGHTBLUE)
usernamelabel.place(x=25, y=370)

passwordlabel = Label (text='Password:', highlightthickness=0, bg=LIGHTBLUE)
passwordlabel.place(x=25, y=400)

searchbutton = Button(text='Search', highlightthickness=0, width=14, bg=LIGHTBLUE, activebackground=BLUE, command=search)
searchbutton.place(x=370, y=338)

passbutton = Button(text='Generate Password', highlightthickness=0, bg=LIGHTBLUE, activebackground=BLUE, command=passwordgenerator)
passbutton.place(x=370, y=398)

addbutton = Button(text='Add', highlightthickness=0, width=48, bg=LIGHTBLUE, activebackground=BLUE, command=save)
addbutton.place(x=135, y=430)

websiteinput = Entry(width=37, bg=GRAY)
websiteinput.place(x=135, y=340)
websiteinput.focus()

usernameinput = Entry(width=56, bg=GRAY)
usernameinput.insert(0, 'ehsanasgharzadeh.asg@gmail.com')
usernameinput.place(x=135, y=370)

passwordinput = Entry(width=37, bg=GRAY)
passwordinput.place(x=135, y=400)

window.mainloop()
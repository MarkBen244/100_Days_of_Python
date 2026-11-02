from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip 
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list= password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password="".join(password_list)
    password_input.insert(0,password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website=website_input.get()
    email=username_input.get()
    password=password_input.get()

    if len(website)==0 or len(email)==0 or len(password)==0:
        messagebox.showinfo(title="Error",message="Please dont leave any feilds empty")

    else:
        is_ok=messagebox.askokcancel(title=website,message=f"These are the detsils you entered: \nEmail: {email}  \nPassword: {password} \nWould you like to save")

        if is_ok:
            with open ("D:/Documents/100Days of Python/Day 29--Password Generator GUI/passwords.txt","a")as data_file:
                data_file.write(f"{website}  |  {email}  |  {password} \n")
                website_input.delete(0,END)
                password_input.delete(0,END)




# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas=Canvas(height=200,width=200)
logo_img=PhotoImage(file="D:/Documents/100Days of Python/Day 29--Password Generator GUI/logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(column=1,row=0)

website_label = Label(text="Website", font=("Arial", 10))
website_label.grid(column=0, row=1)
website_input = Entry(width=35)
website_input.grid(column=1, row=1,columnspan=2)
website_input.focus()

username_label = Label(text="Email/Username", font=("Arial", 10))
username_label.grid(column=0, row=2)
username_input = Entry(width=35)
username_input.grid(column=1, row=2,columnspan=2)
username_input.insert(0,"mark@gmail.com")

password_label = Label(text="Password", font=("Arial", 10))
password_label.grid(column=0, row=3)
password_input = Entry(width=35)
password_input.grid(column=1, row=3,columnspan=2)


genaret_button = Button(text="Generate",command=generate_password)
genaret_button.grid(column=2, row=3)

add_button= Button(text="Add",width=36,command=save)
add_button.grid(column=1, row=4,columnspan=2)

window.mainloop()



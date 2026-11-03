from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip 
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    password_input.delete(0, END)
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
# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website=website_input.get()
    try:
        with open("D:/Documents/100Days of Python/Day 29--Password Generator GUI/passwords.json") as data_file:
            data=json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data Found")        
    else:
        if website in data:
            email=data[website]["email"]
            password=data[website]["password"]
            messagebox.showinfo(title= website,message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error",message=f"No details for {website} exists")

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website=website_input.get()
    email=username_input.get()
    password=password_input.get()
    new_data= {
        website: {
            "email":email,
            "password":password,
        }
    }

    if len(website)==0 or len(email)==0 or len(password)==0:
        messagebox.showinfo(title="Error",message="Please dont leave any feilds empty")

    else:
        try:
            with open ("D:/Documents/100Days of Python/Day 29--Password Generator GUI/passwords.json","r")as data_file:
                # Reading old data
                data=json.load(data_file)
        except FileNotFoundError,json.JSONDecodeError:
            with open ("D:/Documents/100Days of Python/Day 29--Password Generator GUI/passwords.json","w")as data_file:
                data={}
                json.dump(new_data,data_file,indent=4)
        else: 
            # Updating the old data with new data
            data.update(new_data)
            
            with open ("D:/Documents/100Days of Python/Day 29--Password Generator GUI/passwords.json","w")as data_file:
                json.dump(data, data_file,indent=4)
        finally:
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
website_input = Entry(width=21)
website_input.grid(column=1, row=1,)
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


search_button = Button(text="Search",width=13,command=find_password)
search_button.grid(column=2, row=1)

genaret_button = Button(text="Generate",command=generate_password)
genaret_button.grid(column=2, row=3)

add_button= Button(text="Add",width=36,command=save)
add_button.grid(column=1, row=4,columnspan=2)

window.mainloop()



from tkinter import *


def button_clicked():
    new_text = float(input.get())
    value = new_text*1.609
    my_label2.config(text=f"{value}")


window = Tk()
window.title("My First GUI")
window.config(padx=20, pady=20)

# Label 1
my_label = Label(text="I am a Label", font=("Arial", 12))
my_label["text"] = "is equal to"
my_label.grid(column=0, row=1)

# Label 2
my_label2 = Label(text=0, font=("Arial", 12))
my_label2.grid(column=1, row=1)

# Label 3
my_label3 = Label(font=("Arial", 12))
my_label3["text"] = "Km"
my_label3.grid(column=2, row=1)

# Label 4
my_label4 = Label(font=("Arial", 12))
my_label4["text"] = "Miles"
my_label4.grid(column=2, row=1)


# Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)


# Entry
input = Entry(width=7)
input.grid(column=1, row=0)

window.mainloop()

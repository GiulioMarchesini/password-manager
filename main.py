from tkinter import * #import only the tkinter module
from tkinter import messagebox #this module was not imported by the previous line
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, END)#delete the text in the entry box
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10) #random number between 8 and 10 for the letters
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    letters_list= [random.choice(letters) for _ in range(nr_letters)] # _ is a variable that we don't care about, we just want to loop through the range
    symbols_list= [random.choice(symbols) for _ in range(nr_symbols)]
    numbers_list= [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = letters_list + symbols_list + numbers_list
    random.shuffle(password_list)#shuffle the list

    password = "".join(password_list)#convert the list into a string
    password_entry.insert(0, password)#insert the password in the entry box
    pyperclip.copy(password)#copy the password in the clipboard

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        print("empty")
        messagebox.showwarning(title="Warning", message="The fields cannot be empty")
    else:
        response= messagebox.askyesno(title=website, message=f"save username:{username}\npassword:{password} for {website}?")
        if response:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {username} | {password}\n")
                messagebox.showinfo(title="Awsome", message="Password saved!")

            website_entry.delete(0, END)
            password_entry.delete(0, END)
            username_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
windows = Tk()
windows.title("Password Generator")
windows.minsize(width=300, height=300)
windows.config(padx=20, pady=20)
windows.config(bg="white")

# canvas
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# website
website_label = Label(text="Website:", bg="white")
website_label.grid(column=0, row=1)

website_entry = Entry(width=40) #TODO variable non funziona, cerca come fare
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

# email/username
username_label = Label(text="Email/Username:",bg="white")
username_label.grid(column=0, row=2)

username_entry = Entry(width=40)
username_entry.grid(column=1,row=2, columnspan=2)

#password
password_label = Label(text="Password:", bg="white")
password_label.grid(column=0,row=3)

password_entry = Entry(width=21)
password_entry.grid(column=1,row=3)

password_button = Button(text="Generate Password", width=15, bg="white", command=generate_password)
password_button.grid(column=2, row=3)

# add
add_button = Button(text="Add",width=20 ,bg="white", command=save_password)
add_button.grid(column=1, row=4, columnspan=2)


windows.mainloop()
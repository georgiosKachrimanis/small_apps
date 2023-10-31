from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip



def password_generator():
    
    password_entry.delete(0, END) # Clear any entries left on the Entry

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '-', '<', '=', '>', '?', '@', '^', '_']


    password_list = []

    password_letters = [choice(alphabet) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]


    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    suggested_password = "".join(password_list)
    password_entry.insert(0, suggested_password)
    pyperclip.copy(suggested_password)



def save_logins():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Empty Field", message="Please check the information you provided, either website of password is empty!")
    
    else:
        
        is_ok = messagebox.askokcancel(title="Confirmation", message=f"Do you want to add the Password:{password} for the Website: {website}")

        if is_ok:
            with open('p422_w0r6.txt', 'a') as file:
                file.write(f"|| Website: {website} | Username: {username}| Password: {password} ||\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)
    


window = Tk()

window.title("Password Manager")
window.config( padx=50, pady=50, bg="white")

#MyPass image
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo_img= PhotoImage(file="panager/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Website Label and Entry
website_label = Label(text="Website:", bg= "white", font=("Courier"), foreground="black", width=20, anchor="e", pady=2)
website_label.grid(row=1, column=0)

website_entry = Entry(width=40, bg="white", borderwidth=1, highlightthickness=1, foreground="darkblue")
website_entry.grid(row=1, column=1, columnspan=2, pady=2)
website_entry.focus()

# Email/Username Label and Entry
username_label = Label(text="Email/Username:", bg= "white", font=("Courier"), foreground="black", width=20, anchor="e", pady=2)
username_label.grid(row=2, column=0)

username_entry = Entry(width=40, bg="white", borderwidth=1, highlightthickness=1, fg="darkblue")
username_entry.grid(row=2, column=1, columnspan=2, pady=2)
username_entry.insert(0, "enter@your_email.here")

# Password Label and Entry
password_label = Label(text="Password:", bg= "white", font=("Courier"), foreground="black", width=20, anchor="e", pady=2)
password_label.grid(row=3, column=0)

password_entry = Entry(width=22, bg="white", borderwidth=1, highlightthickness=1, fg="darkblue")
password_entry.grid(row=3, column=1, columnspan=1, pady=2)

# Generate password button
generate_pass = Button(text="Generate Password", borderwidth=0, highlightthickness=1, width=14, pady=2, command=password_generator)
generate_pass.grid(row=3, column=2, columnspan=1)

# Add button
add_button = Button(text="Add", borderwidth=0, highlightthickness=1, width=37, pady=2, command=save_logins)
add_button.grid(row=4, column=1, columnspan=2)



window.mainloop()
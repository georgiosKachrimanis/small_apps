from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip
import json



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
    username = email.get() # This is usually the email of the user.
    password = password_entry.get()
    new_data = {
        website: {
            "email": username,
            "password": password,     
        }      
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Empty Field", message="Please check the information you provided, either website of password is empty!")
    else:
        try:
            with open('panager/p422_w0r6.json', 'r') as data_file:
                data = json.load(data_file)          
        except FileNotFoundError:
            with open('panager/p422_w0r6.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)   
        else:
            data.update(new_data)
            with open('panager/p422_w0r6.json', 'w') as data_file:
                json.dump(data, data_file, indent=4)
        finally:        
            website_entry.delete(0, END)
            password_entry.delete(0, END)

def find_password():
    website = website_entry.get() 
    
    if len(website) == 0:
        messagebox.showerror(title="Empty Field", message="Please check the information you provided, the field is empty!")
    else:
        try:
            with open('panager/p422_w0r6.json', 'r') as data_file:
                data = json.load(data_file)
                
        except FileNotFoundError:
            messagebox.showerror(title="Empty Field", message="No Data file found")
        else:
            if website in data:
                    website_email = data[website]['email']
                    website_password = data[website]['password']
                    messagebox.showinfo(title=website, message=f"The Username is: {website_email}\nThe password is: {website_password}")
            else:
                messagebox.showerror(title="No Account", message=f"No Account for {website} Found")
            website_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

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

website_entry = Entry(width=22, bg="white", borderwidth=1, highlightthickness=1, foreground="darkblue")
website_entry.grid(row=1, column=1, columnspan=1, pady=2)
website_entry.focus()

# Search Button
search_button = Button(text="Search", borderwidth=0, highlightthickness=1, width=14, pady=2, command=find_password)
search_button.grid(row=1, column=2, columnspan=1)
# Email/Username Label and Entry
email_label = Label(text="Email/Username:", bg= "white", font=("Courier"), foreground="black", width=20, anchor="e", pady=2)
email_label.grid(row=2, column=0)

email = Entry(width=40, bg="white", borderwidth=1, highlightthickness=1, fg="darkblue")
email.grid(row=2, column=1, columnspan=2, pady=2)
email.insert(0, "enter@your_email.here")

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
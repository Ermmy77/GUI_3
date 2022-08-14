# ------------------ Import ------------------

from tkinter import *

# ------------------ Creating a window ------------------
sign_up = Tk()
sign_up.title("Sign Up")
sign_up.geometry('350x250')

# ------------------ DEF ------------------


# function to check whether the show password button is clicked
def check():
    if button_value.get() == 1:
        password_entry.config(show='')
    else:
        password_entry.config(show='*')


# function used to save username entered to text file and for error handling
def save_username():
    assessment_file = open("username.txt", "a")
    if username_entry.get() == "":
        print("Please enter a valid username")
    elif username_entry.get().isdigit():
        print("Please enter a valid username")
    else:
        assessment_file.write(username_entry.get())
        assessment_file.write("\n")
    assessment_file.close()


# function to save password entered to text file and for error handling
def save_password():
    assessment_file = open("password.txt", "a")
    if password_entry.get() != "":
        assessment_file.write(password_entry.get())
        assessment_file.write("\n")
        sign_up.destroy()
    else:
        print("Please enter a valid password")
    assessment_file.close()


# ------------------ Create text ------------------
text = Label(sign_up, text="Join Now", fg="black")
text.grid(column=1, row=0, padx=20, columnspan=3)
text.configure(font=("Times New Roman", 20))

title = Label(sign_up, text="and start managing you time efficiently",
              fg="black")
title.grid(column=1, row=1, padx=20, pady=5, columnspan=3)
title.configure(font=("Times New Roman", 10))

# text to show information is kept confidential
third_text = Label(sign_up, text="Log in to save your progress. \nWe won't "
                                 "post anything anywhere.", fg="black")
third_text.grid(column=1, row=2, columnspan=3)
third_text.configure(font=("Times New Roman", 15))

# text to show what should go in the entry box
username_text = Label(sign_up, text="Username:", fg="black")
username_text.grid(column=1, row=3, sticky="E")

# text to show what should go in the entry box
password_text = Label(sign_up, text="Password:", fg="black")
password_text.grid(column=1, row=4, sticky="E")

# ------------------ Create entry boxes ------------------

# creates entry box which allows the user to input their username
username_entry = Entry(sign_up, fg="black")
username_entry.grid(column=2, row=3)

# creates an entry box which allows the user to input their username
password_entry = Entry(sign_up, show="*", fg="black")
password_entry.grid(column=2, row=4)

# ------------------ Create button for sign in ------------------

# creates a sign-up button which saves the username and password and also
# closes the window when clicked
sign_up_button = Button(sign_up, text="Sign In", fg="black",
                        command=lambda: [save_username(), save_password()])
sign_up_button.grid(column=2, row=5, pady=5)

# sets value for the show password button
button_value = IntVar(value=0)

# creates a button for the show password
check_button = Checkbutton(sign_up, text='Show Password',
                           variable=button_value, onvalue=1, offvalue=0,
                           command=check, fg="black")
check_button.grid(row=5, column=1)

# ------------------ Run the mainloop ------------------
sign_up.mainloop()

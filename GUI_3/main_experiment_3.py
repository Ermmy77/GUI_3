# ------------------ IMPORTS ------------------
from tkinter import *
from subprocess import call
import webbrowser

# ------------------ Creating a window ------------------

root = Tk()
root.title("My Website")


# ------------------ DEF -----------------

# function to go from home page to sign-up page
def sign_in_window():
    call(["python", "sign_up_3.py"])


# function to go from home page to about us page
def about_us_window():
    root.destroy()
    call(["python", "about_us_3.py"])


# function to open calendar window
def time_entry_window():
    call(["python", "time_entry_refined_3.py"])


# function to go from home page to assessments page
def assessments_window():
    root.destroy()
    call(["python", "assessments_3.py"])


# function to link url to instagram button
def callback(url):
    webbrowser.open_new(url)


# function to save assessment name input to a text file and for error handling
def save_assessment_name():
    special_char = StringVar()
    special_char.set("!@#$%^&*()+=:;<>?/.,|")
    assessment_file = open("assessment_3.txt", "a")
    if assessment_entry.get() != "":
        assessment_file.write(assessment_entry.get())
        assessment_file.write("\n")
    elif assessment_entry.get() == special_char:
        print("Please enter a valid assessment name")
    else:
        print("Please enter a valid assessment name")
    assessment_file.close()


# function for resetting the assessment entry box after submit
def reset_assessment_entry():
    assessment_entry.delete(0, END)


# ------------------ MAKE FRAMES ------------------
top_frame = LabelFrame(root, bg="black")
top_frame.grid(column=0, row=0, columnspan=5, padx=10, pady=10, sticky="NSEW")

middle_frame = LabelFrame(root, bg="#88b589")
middle_frame.grid(column=0, row=1, columnspan=5, rowspan=7, padx=10, sticky="NSEW")

footer = LabelFrame(root, bg="#88b589")
footer.grid(column=0, row=8, columnspan=5, padx=10, pady=10, sticky="NSEW")

# ------------------ Upload images ------------------
logo_image = PhotoImage(file="/Users/malam/PycharmProjects/Website/img/theotherone.png")
button_image = PhotoImage(file="/Users/malam/PycharmProjects/Website/img/back_to_top_button.jpeg")
instagram = PhotoImage(file="/Users/malam/PycharmProjects/Website/img/Untitled.png")

# ------------------ Making Buttons ------------------
# logo button for logo
logo_button = Button(root, image=logo_image, borderwidth=0, relief="raised", bg="black")
logo_button.grid(column=0, row=0, pady=10, padx=15)

# creates button for home page
home_button = Button(root, text="Home", fg="white", bg="black", relief="raised")
home_button.grid(column=1, row=0, padx=40)

# creates button for going to about us page
about_us_button = Button(root, text="About Us", fg="white", bg="black", relief="raised", command=about_us_window)
about_us_button.grid(column=2, row=0, padx=40)

# creates button to go from home page to assessments page
assessments = Button(root, text="Assessments", fg="white", bg="black", relief="raised", command=assessments_window)
assessments.grid(column=3, row=0, padx=40)

# creates button to open sign-up window
sign_up_button = Button(root, text="Sign Up", fg="white", bg="black", relief="raised", command=sign_in_window)
sign_up_button.grid(column=4, row=0, padx=40)

# creates button to go back to top of page
back_to_top = Button(root, image=button_image, bg="green", relief="raised", borderwidth=0)
back_to_top.grid(column=4, row=7)

# creates button linked to instagram account
instagram_button = Button(root, image=instagram, borderwidth=0, relief="raised", bg="#88b589")
instagram_button.grid(column=4, row=8, pady=20, padx=20)
instagram_button.bind("<Button-1>", lambda e: callback("https://www.instagram.com/marickmalamala"))

# creates button to submit assessment entries
submit_button = Button(root, text="Submit", bg="#88b589", relief="raised", command=lambda: [save_assessment_name(),
                                                                                            reset_assessment_entry()])
submit_button.grid(column=3, row=6, rowspan=2, sticky="NSEW", pady=5, padx=10)

# ------------------ Creating Text boxes ------------------
title = Label(root, text="Time Org", bg="#88b589", fg="black", border=0)
title.grid(column=0, row=1, padx=20, pady=10)
title.configure(font=("Times New Roman", 25))

second_text = Label(root, text="A place to take your weakness and refine it into a strength.", bg="#88b589",
                    fg="black")
second_text.grid(column=0, row=2, padx=20)
second_text.configure(font=("Arial", 10))

header = Label(root, text="What is TimeOrg?", bg="#88b589")
header.grid(column=1, row=4, columnspan=2)
header.configure(font=("Times New Roman", 20))

explanation = Label(root, text="TimeOrg is a programme designed to help students who \nare struggling to juggle their "
                               "time between school work and hobbies.", bg="#88b589")
explanation.grid(column=1, row=5, columnspan=2, pady=20)

copyright_label = Label(root, text=u"\u00A9" + 'TimeOrg Ltd 2022.', bg='#88b589')
copyright_label.grid(column=0, row=8)
copyright_label.configure(font=("Times New Roman", 25))

assessment_label = Label(root, text="Assessment Name:", bg='#88b589')
assessment_label.grid(row=6, column=0, sticky="E")
assessment_label.configure(font=("Times New Roman", 20))

time_label = Label(root, text="Deadline:", bg='#88b589')
time_label.grid(row=7, column=0, sticky="E")
time_label.configure(font=("Times New Roman", 20))

# ------------------ Entry Field ------------------
# creates entry box so user can enter assessment name
assessment_entry = Entry(root, font=('Times New Roman', 15), relief="raised")
assessment_entry.grid(row=6, column=1, columnspan=2, sticky="EW")

# creates entry box so user can select due date
time_button = Button(root, command=time_entry_window, text="Select...")
time_button.grid(row=7, column=1, columnspan=2, sticky="EW")


# ------------------ Run the mainloop ------------------
root.mainloop()

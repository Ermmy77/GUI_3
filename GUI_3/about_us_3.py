# ------------------ Imports ------------------
from tkinter import *
from subprocess import call
from tkinter import PhotoImage
import webbrowser

# ------------------ Create Window ------------------
about_us = Tk()
about_us.title("About Us")

# ------------------ DEF ------------------

# function to destroy about us window and go back home
def about_us_home():
    about_us.destroy()
    call(["python", "main_experiment_3.py"])


# function to link url to button
def callback(url):
    webbrowser.open_new(url)


# function to pop up the sign-up page
def about_us_sign_in():
    call(["python", "sign_up_3.py"])


# function to go from about us page to assessments page
def about_us_assessments():
    about_us.destroy()
    call(["python", "assessments_3.py"])


# ------------------ Make Frames ------------------
# creates frame for navigation bar
top_frame = LabelFrame(about_us, bg="black")
top_frame.grid(column=0, row=0, columnspan=5, padx=10, pady=10, sticky="NSEW")

# creates frame for middle section of program
middle_frame = LabelFrame(about_us, bg="#88b589")
middle_frame.grid(column=0, row=1, columnspan=5, rowspan=6, padx=10, sticky="NSEW")

# creates frame for the footer
footer = LabelFrame(about_us, bg="#88b589")
footer.grid(column=0, row=7, columnspan=5, padx=10, pady=10, sticky="NSEW")

# ------------------ Upload images ------------------
logo_image = PhotoImage(file="/Users/malam/PycharmProjects/Website/img/theotherone.png")
button_image = PhotoImage(file="/Users/malam/PycharmProjects/Website/img/back_to_top_button.jpeg")
instagram = PhotoImage(file="/Users/malam/PycharmProjects/Website/img/Untitled.png")
founder = PhotoImage(file="/Users/malam/PycharmProjects/Website/img/realfounder.png")
co_founder = PhotoImage(file="/Users/malam/PycharmProjects/Website/img/Co-Founder.png")
coo = PhotoImage(file="/Users/malam/PycharmProjects/Website/img/coo.png")

# ------------------ Making Buttons ------------------
# creates button to go from about us page to home page
logo_button = Button(about_us, image=logo_image, borderwidth=0, relief="raised", bg="black", command=about_us_home)
logo_button.grid(column=0, row=0, pady=10, padx=15)

# creates button to go from about us page to home page
home_button = Button(about_us, text="Home", fg="white", bg="black", relief="raised", command=about_us_home)
home_button.grid(column=1, row=0, padx=70)

# creates button for about us page
about_us_button = Button(about_us, text="About Us", fg="white", bg="black", relief="raised")
about_us_button.grid(column=2, row=0, padx=70)

# creates button to go from about us page to assessments page
assessment_button = Button(about_us, text="Assessments", fg="white", bg="black", relief="raised",
                           command=about_us_assessments)
assessment_button.grid(column=3, row=0, padx=70)

# creates button to go from about us page to sign-up page
sign_up_button = Button(about_us, text="Sign In", fg="white", bg="black", relief="raised", command=about_us_sign_in)
sign_up_button.grid(column=4, row=0, padx=70)

# creates button to go back to top of page
back_to_top = Button(about_us, image=button_image, bg="green", relief="raised", borderwidth=0)
back_to_top.grid(column=4, row=6)

# creates button linked to instagram account
instagram_button = Button(about_us, image=instagram, borderwidth=0, relief="raised", bg="#88b589")
instagram_button.grid(column=4, row=7, pady=20, padx=20)
instagram_button.bind("<Button-1>", lambda e: callback("https://www.instagram.com/marickmalamala"))

# ------------------ Create Labels ------------------

header = Label(about_us, text="About Us Page", bg="#88b589")
header.grid(column=0, row=2, pady=10, padx=10, columnspan=3)
header.configure(font=("Times New Roman", 20))

text = Label(about_us, text="Hello, my name is Ermmy and at TimeOrg we look to help students\n who are struggling with "
                            "time management.", bg="#88b589")
text.grid(column=0, row=3, pady=10, padx=10, columnspan=3)
text.configure(font=("Times New Roman", 15))

top_text = Label(about_us, text="Our Team", bg="#88b589")
top_text.grid(column=1, row=4, pady=10)
top_text.configure(font=("Times New Roman", 20))

founder_label = Label(about_us, image=founder, borderwidth=0, bg="#88b589")
founder_label.grid(column=0, row=5, pady=10)

founder_text = Label(about_us, text="Ben Trum \nCEO & Founder\n My name is Ben and I am the founder of TimeOrg. "
                                    "Growing up, I found it quite challenging to \nmange my time so I decided to make "
                                    "this program to help the generations of the future.", bg="#88b589")
founder_text.grid(column=0, row=6, pady=10, padx=10)
founder_text.configure(font=("Times New Roman", 10, "bold"))

co_founder_label = Label(about_us, image=co_founder, borderwidth=0, bg="#88b589")
co_founder_label.grid(column=1, row=5, pady=10, padx=5)

co_founder_text = Label(about_us, text="Brandon Dioppo \nCo-Founder \nMy name is Brandon and ever since "
                                       "I was a young boy, I always found many \nthings interesting and so trying to "
                                       "distribute my time evenly between my hobbies \nwas a struggle. It wasn't until"
                                       " I was about the age of 23 did I fully master the arts of \ntime management. "
                                       "Since I know that many people don't have 3 years to master this \ntechnique, "
                                       "I teamed up with Ben to ensure that you don't have to go through the \nstruggle"
                                       " of poor time management.", bg="#88b589")
co_founder_text.grid(column=1, row=6)
co_founder_text.configure(font=("Times New Roman", 10, "bold"))

coo_label = Label(about_us, image=coo, borderwidth=0, bg="#88b589")
coo_label.grid(column=2, row=5, pady=10, padx=5)

coo_text = Label(about_us, text="Quintus Novogratz \nCOO \nMy name is Quintus, otherwise known by the numeric value"
                                "of my name five. \nI came up with the idea of taking the assessment time and moving "
                                "it up a few \ndays in order to give students who procrastinate that late study boost"
                                " without \nthe actual deadline being due. ", bg="#88b589")
coo_text.grid(column=2, row=6)
coo_text.configure(font=("Times New Roman", 10, "bold"))

copyright_about_us = Label(about_us, text=u"\u00A9" + 'TimeOrg Ltd 2022.', bg='#88b589')
copyright_about_us.grid(column=0, row=7)
copyright_about_us.configure(font=("Times New Roman", 25))


# ------------------ Run the mainloop ------------------

about_us.mainloop()

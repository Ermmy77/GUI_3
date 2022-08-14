# ------------------ Imports ------------------
from tkinter import *
from subprocess import call
import webbrowser
import datetime

# ------------------ Creating Window ------------------

assessment = Tk()
assessment.title("Assessments")


# ------------------ DEF ------------------


# function to go from assessments page to home page
def assessments_home():
    assessment.destroy()
    call(["python", "main_experiment_3.py"])


# function to open sign-up page
def assessments_sign_in():
    call(["python", "sign_up_3.py"])


# function to go from assessments page to about us page
def assessments_about_us():
    assessment.destroy()
    call(["python", "about_us_3.py"])


# function to link url to instagram button
def callback(url):
    webbrowser.open_new(url)


# ------------------ Frames ------------------

# creates a frame for the navigation bar
top_frame = LabelFrame(assessment, bg="black")
top_frame.grid(column=0, row=0, columnspan=5, padx=10, pady=10, sticky="NSEW")

# creates a frame for the middle section of the program
middle_frame = LabelFrame(assessment, bg="#88b589")
middle_frame.grid(column=0, row=1, columnspan=5, padx=10, sticky="NSEW")

# creates a frame for the footer
footer = LabelFrame(assessment, bg="#88b589")
footer.grid(column=0, row=2, columnspan=5, padx=10, pady=10, sticky="NSEW")

# ------------------ Upload images ------------------
logo_image = PhotoImage(file="/Users/malam/PycharmProjects/Website/img/theotherone.png")
instagram = PhotoImage(file="/Users/malam/PycharmProjects/Website/img/Untitled.png")

# ------------------ Making Buttons ------------------
# logo button for returning to front page
logo_button = Button(assessment, image=logo_image, borderwidth=0, relief="raised", bg="black", command=assessments_home)
logo_button.grid(column=0, row=0, pady=10, padx=15)

# home button for returning to front page
home_button = Button(assessment, text="Home", fg="white", bg="black", relief="raised", command=assessments_home)
home_button.grid(column=1, row=0, padx=40)

# creates button to go assessments home page to about us page
about_us_button = Button(assessment, text="About Us", fg="white", bg="black", relief="raised",
                         command=assessments_about_us)
about_us_button.grid(column=2, row=0, padx=40)

# creates button for assessments page
assessments = Button(assessment, text="Assessments", fg="white", bg="black", relief="raised")
assessments.grid(column=3, row=0, padx=40)

# creates button to go from assessments page to sign-up page
sign_in_button = Button(assessment, text="Sign Up", fg="white", bg="black", relief="raised",
                        command=assessments_sign_in)
sign_in_button.grid(column=4, row=0, padx=40)

# creates button which is linked to instagram account
instagram_button = Button(assessment, image=instagram, borderwidth=0, relief="raised", bg="#88b589")
instagram_button.grid(column=4, row=2, pady=20, padx=20)
instagram_button.bind("<Button-1>", lambda e: callback("https://www.instagram.com/marickmalamala"))

# ------------------ Text Labels ------------------
copyright_label = Label(assessment, text=u"\u00A9" + 'TimeOrg Ltd 2022.', bg='#88b589')
copyright_label.grid(column=0, row=2)
copyright_label.configure(font=("Times New Roman", 25))

# ------------------ Display assessment name ------------------
# opens the assessment text file and reads it
open_assessment_file = open("assessment_3.txt")
assessment_data = open_assessment_file.read()
open_assessment_file.close()
# displays the assessment name
first_assessment = Label(assessment, text=assessment_data, bg="#88b589", font=("Times New Roman", 20))
first_assessment.grid(column=0, row=1, pady=5, columnspan=2)

# ------------------ Display time ------------------
# opens the time text file and reads it
open_time_file = open("time_3.txt")
time_data = open_time_file.read()
open_time_file.close()
# displays time selected
first_time = Label(assessment, text=time_data, bg="#88b589", font=("Times New Roman", 20))
first_time.grid(column=2, row=1, pady=5, columnspan=2)

# ------------------ Run the mainloop ------------------
assessment.mainloop()

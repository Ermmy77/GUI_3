# ------------------ Import ------------------
import datetime
from tkinter import *
from tkcalendar import Calendar

# ------------------ Create Window ------------------
time = Tk()

# ------------------ Set geometry ------------------
time.geometry("400x400")


# ------------------ DEF ------------------


# function to save entered time and check if the time selected is in the past.
def save_time():
    date = '10/14/22'
    date_object = datetime.datetime.strptime(date, "%m/%d/%y")
    date_string = datetime.datetime.strftime(date_object, "%m/%d/%y")
    time_file = open("time_3.txt", "a")
    if calendar.get_date() < date_string:
        print("Please enter a valid date")
    else:
        time_file.write(calendar.get_date())
        time_file.write("\n")
        time.destroy()
    time_file.close()


# ------------------ Add Calendar ------------------
# creates calendar for the user to pick a date
calendar = Calendar(time, selectmode='day', year=2022, month=10, day=14)
# packs the calendar
calendar.pack(pady=20)

# ------------------ Add Button and Label ------------------
# creates a button which saves the user input when clicked
select_button = Button(time, text="Select Date", command=lambda: [save_time()])
# packs button
select_button.pack(pady=20)


# ------------------ Run mainloop ------------------
time.mainloop()

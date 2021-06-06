import datetime as dt
import pandas as pd
import smtplib
import random

# ----------------------------------- BIRTHDAY DATE CHECK ----------------------------- #

# Configuring the required data
letter_list = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
data = pd.read_csv("birthdays.csv")
my_email = ""
password = ""
PLACE_HOLDER = "[NAME]"

# Getting hold of today's date
today = dt.datetime.now()
month = today.month
day = today.day

# Importing Data from CSV
for index, row in data.iterrows():
    person_name = row['name']
    person_email = row["email"]

    # Comparing date of birth with today's date
    if row['month'] == month and row['day'] == day:
        letter_number = random.choice(letter_list)
        with open(f"letter_templates/{letter_number}") as message:
            email_message = message.read()

        # Editing Mail content
        email_message = email_message.replace(PLACE_HOLDER, person_name)

        # Initiating the mail
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=row["email"],
                msg=f"Subject:Surprise \n\n{email_message}")



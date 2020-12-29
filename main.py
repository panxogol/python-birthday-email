# --- IMPORTS ---
import pandas as pd
import datetime as dt
from random import choice
import smtplib as smtp
from config import *

# --- CONSTANTS ---
LETTERS = [
    "letter_templates/letter_1.txt",
    "letter_templates/letter_2.txt",
    "letter_templates/letter_3.txt"
]


# --- FUNCTIONS ---
def main():
    # todo 1. Update the birthdays.csv
    birthday_data_df = pd.read_csv(filepath_or_buffer="birthdays.csv")
    birthday_data_dict = birthday_data_df.to_dict(orient="records")
    today = dt.datetime.now()

    # THE NEXT LINES ARE FOR TESTING PURPOSE
    new_person = {
        "name": USER_NAME,
        "email": USER_EMAiL,
        "year": 2020,
        "month": today.month,
        "day": today.day
    }
    if new_person not in birthday_data_dict:
        birthday_data_dict.append(new_person)

    new_bd_df = pd.DataFrame(birthday_data_dict)
    new_bd_df.to_csv("birthdays.csv", index=False)

    print(birthday_data_dict)
    # todo 2. Check if today matches a birthday in the birthdays.csv
    birthday_people = [data for data in birthday_data_dict
                       if data["month"] == today.month and data["day"] == today.day]
    print(birthday_people)
    # todo 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's
    #  actual name from birthdays.csv
    if len(birthday_people) > 0:
        for person in birthday_people:
            with open(choice(LETTERS)) as file:
                letter = file.read()
            letter = letter.replace("[NAME]", person["name"])
            letter = letter.replace("[USER_NAME]", USER_NAME)

        # todo 4. Send the letter generated in step 3 to that person's email address.
            with smtp.SMTP(host=USER_HOST) as connection:
                # Security
                connection.starttls()

                # Login
                connection.login(user=USER_EMAiL, password=USER_PASSWORD)

                # Send Message
                connection.sendmail(
                    from_addr=USER_EMAiL,
                    to_addrs=person["email"],
                    msg=f"Subject: Happy Birthday {person['name']}\n\n"
                        f"{letter}"
                )


# --- RUN ---
if __name__ == '__main__':
    main()

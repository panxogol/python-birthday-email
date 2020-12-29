# Automated Email Send on friends and family Birthdays
## Built using Python 3.8 and pandas

Download, then go to project repo and open a terminal there:

Create a `config.py` file in the project folder and add this lines:

`USER_EMAiL = "your_email@email.com"`

`USER_PASSWORD = "your-password"`

`USER_HOST = "the-smtp-adress-of-your-email-server"` (e.g: smtp.gmail.com)

`USER_NAME = "Your Name"`

run:

`$ virtualenv venv`

then:

in Windows:`$ venv\Scripts\activate`

In linux or mac: ` $ source venv/Scripts/activate`

then: `pip install -r requirements.txt`
or `$ pip install pandas`

Now the project will be ready to work with pandas.
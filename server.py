"""
Written by Gabriel Brown
"""
# Base Python libraries
import json
import time

# Flask and server libraries
from flask import Flask, render_template, make_response, request

# My classes
from supporting_classes.message import Message
from supporting_classes.guest import Guest
from supporting_classes.reservation import Reservation
from supporting_classes.company import Company

app = Flask(__name__)


guests = []
companies = []


# Load in Guest and reservation data

with open("./json/Guests.json") as json_file:

    guest_res_data = json.load(json_file)

    for guest_object in guest_res_data:

        # Generate the reservation object
        roomNumber = guest_object["reservation"]["roomNumber"]
        startTime = guest_object["reservation"]["startTimestamp"]
        endTime = guest_object["reservation"]["endTimestamp"]

        reservation = Reservation(roomNumber, startTime, endTime)

        # Generate the guest object
        ID = guest_object["id"]
        firstName = guest_object["firstName"]
        lastName = guest_object["lastName"]

        guest = Guest(ID, firstName, lastName, reservation)
        guests.append(guest)


for guest in guests:

    print(guest)



# Load in Company data

with open("./json/Companies.json") as json_file:

    company_data = json.load(json_file)

    for company_obj in company_data:

        ID = company_obj["id"]
        name = company_obj["company"]
        city = company_obj["city"]
        timezone = company_obj["timezone"]

        company = Company(ID, name, city, timezone)
        companies.append(company)

for company in companies:

    print(company)

# Load in Template data



# Routes
@app.route("/")
def index():

    return app.send_static_file("index.html")
    #return render_template("index.html")


# Other methods
def determine_greeting():
    """
    Return string representing a greeting that is appropriate for the current time and timezone, i.e.
    Good morning, Good afternoon, good evening
    """
    localtime = time.localtime(time.time())
    hour = localtime[3]

    if hour >= 5 and hour < 12:

        return "Good morning"

    elif hour >= 12 and hour < 5:

        return "Good afternoon"

    else:

        return "Good evening"




if __name__ == "__main__":
    # debug mode makes changes instantly visible
    app.run(debug=True)




















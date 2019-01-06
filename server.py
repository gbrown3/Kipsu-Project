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
from supporting_classes.templates import Template
from supporting_classes.guest import Guest
from supporting_classes.reservation import Reservation
from supporting_classes.company import Company

app = Flask(__name__)


guests = {}
companies = {}
templates = {} # Each template is an ordered list of message parts, with variables as seperate elements in the list
# TODO: explain my template system better somewhere


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
        guests[ID] = guest



# Load in Company data

with open("./json/Companies.json") as json_file:

    company_data = json.load(json_file)

    for company_obj in company_data:

        ID = company_obj["id"]
        name = company_obj["company"]
        city = company_obj["city"]
        timezone = company_obj["timezone"]

        company = Company(ID, name, city, timezone)
        companies[ID] = company


# Load in Template data
with open("./json/Templates.json") as json_file:

    template_data = json.load(json_file)

    for template_obj in template_data:

        ID = template_obj["id"]
        parts = template_obj["parts"]

        template = Template(ID, parts)
        templates[ID] = template



# Routes
@app.route("/")
def index():

    

    # Make a sample message
    # message = Message(templates[0], guests[0], companies[0])
    # print(message.message)

    return render_template("index.html", guests=guests, companies=companies, templates=templates)


@app.route("/create_message", methods=["GET"])
def create_message():

    Message.greeting = determine_greeting()

    guest_id = int(request.args.get('guestID'))
    company_id = int(request.args.get('companyID'))
    template_id = int(request.args.get('templateID'))

    # TODO: put in some form of error handling in case one or more of the query parameters is missing


    # Access those dictionaries with the ids pulled from the request args, then get the
    # appropriate data, generate the message, and return that string
    guest = guests[guest_id]
    company = companies[company_id]
    template = templates[template_id]

    message = Message(template, guest, company)

    return message.message

@app.route("/new_template", methods=["POST"])
def new_template():

    # TODO: process template info

    template_data = request.args.get("text")

    print(template_data)

    parts = []

    split_string = template_data.split()

    for string in split_string:

        #TODO: As of the current moment, this method doesn't really handle long strings with one of the
        # keywords incorporated into it, such as an email with the company's name in it.
        # To be honest, I'm not sure you'd ever want to make a template with an email where
        # you can swap out the company name, as it would probably make more sense to have an EMAIL
        # keyword that corresponded to another attribute stored in company objects.

        if "GREETING" in string:

            parts.append("GREETING")
            other_chars = string.replace("GREETING", "")
            parts.append(other_chars)

        elif "FIRSTNAME" in string:

            parts.append("FIRSTNAME")
            other_chars = string.replace("FIRSTNAME", "")
            parts.append(other_chars)

        elif "LASTNAME" in string:

            parts.append("LASTNAME")
            other_chars = string.replace("LASTNAME", "")
            parts.append(other_chars)

        elif "ROOMNUMBER" in string:

            parts.append("ROOMNUMBER")
            other_chars = string.replace("ROOMNUMBER", "")
            parts.append(other_chars)

        elif "COMPANYNAME" in string:

            parts.append("COMPANYNAME")
            other_chars = string.replace("COMPANYNAME", "")
            parts.append(other_chars)

        elif "CITY" in string:

            parts.append("CITY")
            other_chars = string.replace("CITY", "")
            parts.append(other_chars)

        elif "TIMEZONE" in string:

            parts.append("TIMEZONE")
            other_chars = string.replace("TIMEZONE", "")
            parts.append(other_chars)

        else:

            parts.append(string)

    print(parts)

    

    return ""



# Other methods

# TODO: it would be cool to let this take in a local time as well,
# so that users connecting to the server from different time zones
# could pass in their local time and still get an appropriate greeting,
# not just a greeting appropriate to wherever the server is located
def determine_greeting():
    """
    Return string representing a greeting that is appropriate for the current time and timezone, i.e.
    Good morning, Good afternoon, Good evening
    """
    localtime = time.localtime(time.time())
    hour = localtime[3]

    if hour >= 5 and hour < 12:

        return "Good morning"

    elif hour >= 12 and hour < 17:

        return "Good afternoon"

    else:

        return "Good evening"




if __name__ == "__main__":
    # debug mode makes changes instantly visible
    app.run(debug=True)




















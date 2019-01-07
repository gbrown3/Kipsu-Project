"""
The main Flask server, where requests are handled and requests for new messages are processed

Written by Gabriel Brown
"""
# Base Python libraries
import json
import time

# Flask and server libraries
from flask import Flask, render_template, make_response, request, jsonify

# My classes
from supporting_classes.message import Message
from supporting_classes.templates import Template
from supporting_classes.guest import Guest
from supporting_classes.reservation import Reservation
from supporting_classes.company import Company



app = Flask(__name__)


guests = {}
companies = {}
templates = {}

# Each keyword corresponds to a specific variable in guest, company, reservation objects, etc.
keywords = ["GREETING", "FIRSTNAME", "LASTNAME", "ROOMNUMBER", "COMPANYNAME", "CITY", "TIMEZONE"]


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

        # I assigned IDs this way to make room for new templates.
        # If I allowed the IDs to be asigned in JSON I would have to 
        # look through every id and keep track of what new ones are available,
        # or use something like UUID which seems a bit overkill.
        # I'm also using a dictionary rather than a list because I didn't want the
        # client side to start with Template 0, and I wanted that to be reflected
        # in the way these templates are stored in the server as well.

        ID = len(templates) + 1
        parts = template_obj["parts"]

        template = Template(ID, parts)
        templates[ID] = template



# Routes

# Returns the main page, rendered from an HTML template so it can be populated with information 
# about different guests, companies and message templates
@app.route("/")
def index():

    return render_template("index.html", guests=guests, companies=companies, templates=templates)


# Handles AJAX requests for new messages
@app.route("/create_message", methods=["GET"])
def create_message():

    Message.greeting = determine_greeting()

    guest_id = int(request.args.get('guestID'))
    company_id = int(request.args.get('companyID'))
    template_id = int(request.args.get('templateID'))

    # TODO: put in some form of error handling in case one or more of the query parameters is missing

    guest = guests[guest_id]
    company = companies[company_id]
    template = templates[template_id]

    message = Message(template, guest, company)

    return message.message


# Handles AJAX requests to add new templates
@app.route("/new_template", methods=["POST"])
def new_template():

    template_data = request.args.get("text")

    # TODO: add some error handling here

    parts = []
    split_string = template_data.split()

    for string in split_string:

        # As of the current moment, this method doesn't really handle long strings with one of the
        # keywords incorporated into it, such as an email with the company's name in it.
        # To be honest, I'm not sure you'd ever want to make a template with an email where
        # you can swap out the company name, as it would probably make more sense to have an EMAIL
        # keyword that corresponded to another attribute stored in company objects.

        keyword_found = False

        for keyword in keywords:

            if keyword in string:
                parts.append(keyword)
                other_chars = string.replace(keyword, "")
                parts.append(other_chars)
                keyword_found = True
                break

        if not keyword_found:
            parts.append(string)


        parts.append(" ")


    ID = len(templates) + 1
    template = Template(ID, parts)
    templates[ID] = template

    return jsonify(template.serialize())



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




















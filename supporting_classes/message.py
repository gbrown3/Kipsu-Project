"""
Written by Gabriel Brown
"""

class Message:

    # This should be changed by the server, based on the current time of day for the server
    # (Or hopefully the individual client's time of day with further implementation)
    greeting = "PLACEHOLDER GREETING"

    def __init__(self, template, guest, company):
        """"""

        self.template = template
        self.guest = guest
        self.company = company

        self.message = self.generate_message()


    def generate_message(self):
        """"""

        message = ""

        for part in self.template.parts:

            if part == "GREETING":

                message += Message.greeting

            elif part == "FIRSTNAME":

                message += self.guest.firstName

            elif part == "LASTNAME":

                message += self.guest.lastName

            elif part == "ROOMNUMBER":

                message += str(self.guest.reservation.roomNumber)

            elif part == "COMPANYNAME":

                message += self.company.name

            elif part == "CITY":

                message += self.company.city

            elif part == "TIMEZONE":

                message += self.company.timezone

            else:

                message += part

        return message

"""
Written by Gabriel Brown
"""

class Message:

    def __init__(self, template, guest, reservation, company, city, timezone):
        """"""

        self.template = template
        self.guest = guest
        self.reservation = reservation
        self.company = company
        self.city = city
        self.timezone = timezone

        self.message = self.generate_message()


    def generate_message(self):
        """"""

        message = ""

        print("Template: ")
        print(self.template)

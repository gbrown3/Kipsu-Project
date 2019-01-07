"""
Represents one guest with a reservation

Written by Gabriel Brown
"""

class Guest:

    def __init__(self, id, firstName, lastName, reservation):

        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.reservation = reservation

    def __str__(self):

        return "ID: " + str(self.id) + "\n\n" + "First Name: " + self.firstName + "\n\n" + "Last Name: " + self.lastName + "\n\n" + str(self.reservation) + "\n\n\n"
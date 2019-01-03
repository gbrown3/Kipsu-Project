"""
Written by Gabriel Brown
"""

class Company:

    def __init__(self, id, name, city, timezone):

        self.id = id
        self.name = name
        self.city = city
        self.timezone = timezone

    def __str__(self):

        return "ID: " + str(self.id) + "\n\n" + "Name: " + self.name + "\n\n" + "City: " + self.city + "\n\n" + "Timezone: " + self.timezone + "\n\n\n"
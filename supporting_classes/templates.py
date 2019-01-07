"""
A template for a message.

Written by Gabriel Brown
"""

class Template:

    def __init__(self, id, parts):

        self.id = id
        self.parts = parts

        # parts is a list of different parts of the template. It doesn't matter much how 
        # other parts of overall message are split up, but it is assumed that every keyword is
        # a single element and seperated from all other character when in this list

    def serialize(self):
        """
        Returns a dictionary with all the template information, this makes it
        easier to turn into a JSON object and pass between the client and server
        """

        return {
            "id": self.id,
            "parts": self.parts 
        }
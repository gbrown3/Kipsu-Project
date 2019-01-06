"""
Written by Gabriel Brown
"""

class Template:

    def __init__(self, id, parts):

        self.id = id
        self.parts = parts

    def serialize(self):

        return {
            "id": self.id,
            "parts": self.parts
        }
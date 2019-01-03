"""
Written by Gabriel Brown
"""

class Reservation:

    def __init__(self, roomNumber, startTime, endTime):

        self.roomNumber = roomNumber
        self.startTime = startTime
        self.endTime = endTime

    def __str__(self):

        return "Room number: " + str(self.roomNumber) + "\n\n" + "Start time: " + str(self.startTime) + "\n\n" + "End time: " + str(self.endTime) + "\n\n\n"
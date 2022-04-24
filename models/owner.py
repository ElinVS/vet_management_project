import re


class Owner:
    def __init__(self, first_name,last_name, email, phone_number, adress, postcode,registered, id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.adress = adress
        self.postcode = postcode
        self.registered = registered
        self.id = id


def mark_registered(self):
    self.registered = True

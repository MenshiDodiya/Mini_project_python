#Phone number details using python

import phonenumbers
from phonenumbers import timezone,geocoder,carrier

number = input("Enter your number with +__: ")
phone=phonenumbers.parse(number)
time=timezone.time_zones_for_number(phone)
car=carrier.name_for_number(phone,"en")
reg=geocoder.description_for_number(phone,"en")
print(f"Time:{time}")
print(f"Phone number:{phone}")
print(f"Carrier:{car}")
print(f"Description:{reg}")
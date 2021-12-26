import phonenumbers
from phonenumbers import carrier, geocoder, timezone

mobileNo = input("Mobile NUmber: ")
mobileNo=phonenumbers.parse(mobileNo)
print(timezone.time_zones_for_number(mobileNo))
print(carrier.name_for_number(mobileNo, "en"))
print(geocoder.description_for_number(mobileNo, "en"))
print("Valid Mobile Number:",phonenumbers.is_valid_number(mobileNo))
print("Checking possiblity of number:",phonenumbers.is_possible_number(mobileNo))

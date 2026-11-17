from datetime import datetime

event_title = input("Enter event title: ")
year = int(input("Enter year: "))
month = int(input("Enter month: "))
day = int(input("Enter day: "))

formatted_event = event_title.upper()

print("\nOutput:")
print(f"Event: {formatted_event}")
print(f"Date: {month}/{day}/{year}")
print(f"Year: {year}")
print(f"Month: {month}")
print("Weekday: null (cannot be done without datetime functions)")
from datetime import datetime

event_title = input("Enter event title: ")
year = int(input("Enter year: "))
month = int(input("Enter month: "))
day = int(input("Enter day: "))

formatted_event = event_title.upper()

event_date = datetime(year, month, day)

print("\nFormatted Output:")
print(f"Event: {formatted_event}")
print(f"Date: {event_date.strftime("%B %d, %Y")}")
print(f"Year: {event_date.strftime("%Y")}")
print(f"Month: {event_date.strftime("%m")}")
print(f"Day: {event_date.strftime("%d")}")
print(f"Weekday: {event_date.strftime("%A")}")

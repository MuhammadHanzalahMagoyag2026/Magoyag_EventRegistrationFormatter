# Version 1: Basic input and output without formatting

first_name = input("Enter student first name: ")
last_name = input("Enter student last name: ")
section = input("Enter section: ")
event_name = input("Enter event name: ")
event_year = input("Enter event year: ")
event_month = input("Enter event month: ")
event_day = input("Enter event day: ")

full_name = first_name + " " + last_name
raw_date = event_year + "-" + event_month + "-" + event_day

print("\nStudent Event Registration Summary")
print("Name:", full_name)
print("Section:", section)
print("Event:", event_name)
print("Event Date:", raw_date)

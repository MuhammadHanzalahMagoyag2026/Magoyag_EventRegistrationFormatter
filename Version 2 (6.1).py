# Version 2: Added string formatting for name, section, and event title

first_name = input("Enter student first name: ").strip()
last_name = input("Enter student last name: ").strip()
section = input("Enter section: ").strip()
event_name = input("Enter event name: ").strip()
event_year = input("Enter event year: ").strip()
event_month = input("Enter event month: ").strip()
event_day = input("Enter event day: ").strip()

formatted_name = (first_name + " " + last_name).title()
name_code = formatted_name.upper()
formatted_section = section.upper()
formatted_event = event_name.title()
raw_date = event_year + "-" + event_month + "-" + event_day

print("\nStudent Event Registration Summary")
print("Name:", formatted_name)
print("Name Code:", name_code)
print("Section:", formatted_section)
print("Event:", formatted_event)
print("Event Date:", raw_date)
print("Language Used: Python")
print("String Feature Used: strip(), title(), upper()")

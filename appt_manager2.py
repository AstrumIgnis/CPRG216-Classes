from appointment import Appointment

def show_appointments_by_name(listOfAppt, client_search):
    for appt in listOfAppt:
        if client_search.lower() in appt.client_name.lower():
            print(appt)

def show_appointments_by_day(listOfAppt, day):
    for appt in listOfAppt:
        if appt.day_of_week == day:
            print(appt)

def change_appointment_by_day(listOfAppt):
    day = input("What day: ").title()
    startHour = input("Enter start hour (24 hour clock): ")
    for appt in listOfAppt:
        if day == appt.day_of_week and startHour == appt.start_time_hour:
            newDay = input("Enter a new day: ").title()
            newStartHour = input("Enter start hour (24 hour clock): ")
            appt.day_of_week = newDay
            appt.start_time_hour = newStartHour
            print(f"Appointment for {appt.client_name} has been changed to:\nDay = {appt.day_of_week}\nTime = {appt.start_time_hour}")
    print("That time slot hasn't been booked and doesn't need to be changed")
    return
    

def calculate_feed_per_day(listOfAppt):
    print("Fees calculation per day....")
    day = input("What day: ").title()
    totalFees = 0
    for appt in listOfAppt:
        if appt.day_of_week == day:
            # Mens cut
            if appt.appt_type == 1:
                totalFees += 40
            # Ladies cut
            if appt.appt_type == 2:
                totalFees += 60
            # Mens colouring
            if appt.appt_type == 3:
                totalFees += 40
            # Ladies colouring
            if appt.appt_type == 4:
                totalFees += 80
    print(f"Total fees for {day} is {totalFees}")

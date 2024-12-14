from appointment import Appointment
listOfDays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]   

def show_appointments_by_name(listOfAppt, client_search):
    print(f"Appointments for {client_search}")
    print("\n\n{:20s}{:15s}{:10s}{:10s}{:10s}{:20s}".format("Client Name",
        "Phone", "Day", "Start", "End", "Type"))
    print("---------------------------------------------------------------------------")
    for appt in listOfAppt:
        if appt.client_name != 0:
            if client_search.title() in appt.client_name:
                print(appt)
                return
    print("No appointments found.")

def show_appointments_by_day(listOfAppt, day):
    print("\n\n{:20s}{:15s}{:10s}{:10s}{:10s}{:20s}".format("Client Name",
        "Phone", "Day", "Start", "End", "Type"))
    print("---------------------------------------------------------------------------")
    if day in listOfDays:
        for appt in listOfAppt:
            if appt.day_of_week == day:
                print(appt)

def change_appointment_by_day(listOfAppt):
    day = input("What day: ").title()
    startHour = int(input("Enter start hour (24 hour clock): "))
    for appt in listOfAppt:
        if day == appt.day_of_week and startHour == appt.start_time_hour:
            if appt.appt_type == 0:
                print("That time slot hasn't been booked and doesn't need to be changed")
                return
            newDay = input("Enter a new day: ").title()
            newStartHour = int(input("Enter start hour (24 hour clock): "))
            print(appt.appt_type)
            for changedAppt in listOfAppt:
                if newDay == changedAppt.day_of_week and newStartHour == changedAppt.start_time_hour:
                    if changedAppt.appt_type != 0:
                        print("The new timeslot is already booked")
                        return
                    changedAppt.schedule(appt.client_name, appt.client_phone, appt.appt_type)
                    print(f"Appointment for {appt.client_name} has been changed to:\nDay = {changedAppt.day_of_week}\nTime = {changedAppt.start_time_hour}")
                    appt.schedule(0, 0, 0)
            return   
    

def calculate_fees_per_day(listOfAppt):
    print("Fees calculation per day....")
    day = input("What day: ").title()    
    if day not in listOfDays:
        print(f"{day} is invalid day or the salon is closed")
        return
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
    print(f"Total fees for {day} is ${totalFees}")

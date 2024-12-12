import os 
from appointment import Appointment

def create_weekly_calendar(appointments_list):
    """
    Purpose: Function will create a weekly calendar 
    Parameters: None
    Retunrs: Creates new Appointment object and adds it to the appointment list (i.e. calendar)
    """
    #This clears any previous appointments
    appointments_list.clear()  
    week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    # Add an Appointment object for each day and hour
    for days in week:
        for hour in range(9, 17):  # 9 AM to 4 PM
            appointments_list.append(Appointment(day_of_week=days, start_time_hour=str(hour)))

def load_scheduled_appointments(appointments_list):
    """
    Purpose: Will load scheduled appointments from a file into the appointment list.
    Parameters: Sorts the appointments by their day and time
    Returns: Number of scheduled appointments loaded
    """
    fileName = input("Enter the appointment filename: ").strip()

    if not os.path.exists(fileName):
        print("File not found")
        return 0

    with open(fileName, "r") as file:
        lines = file.readlines()

    count = 0
    for line in lines:
        data = line.strip().split(",")

        # Only proceed if there are the correct number of elements
        if len(data) == 5:  
            client_name, client_phone, appt_type, day_of_week, start_time_hour = data
            appt_type = int(appt_type)

            # Find the appointment by day and time
            found_appointment = find_appointment_by_time(appointments_list, day_of_week, start_time_hour)
            if found_appointment:
                found_appointment.schedule(client_name, client_phone, appt_type)
                count += 1

    return count

def print_menu():
    """
    Purpose: To display a menu for the user to select
    Parameters: None
    Returns: The function the user selects
    """
    print("\n==================================================")
    print("Hair Salon Appointment Manager")
    print("==================================================")
    print("1) Schedule an Appointment")
    print("2) Find Appointment by Name")
    print("3) Print Calendar for a Specfic Day")
    print("4) Cancel an Appointment")
    print("5) Change an Appointment")
    print("6) Calculate Total Fees for a Day")
    print("7) Calaulate Total Weekly Fees")
    print("9) Exit the System")

    user_option = {"1", "2", "3", "4", "5", "6", "7", "9"}
    choice = input("Enter your Selection: ").strip()
    while choice not in user_option:
        print("Invalid Option")
        choice = input("Enter your choice: ").strip()
    return choice

def find_appointment_by_time(appointments_list, day, start_hour):
    """
    Purpose: Will find an appointment by day and start hour fromt the list
    Parameters: None
    Returns: The appointment if possible
    """
    for appointment in appointments_list:
        if appointment.get_day_of_week() == day and appointment.get_start_time_hour() == start_hour:
            return appointment
    return None


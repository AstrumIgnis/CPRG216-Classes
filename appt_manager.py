import os 
from appointment import Appointment
import appt_manager1
import appt_manager2


appointment_list = []

appt_manager1.create_weekly_calendar(appointment_list)



def calculate_weekly_fees(appointment_list):
    totalFees = 0
    for appt in appointment_list:
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
    print(f"Total weekly fees is ${totalFees}")

def save_scheduled_appointments(appointment_list):
    saved_appointments = 0
    choice = input("Would you like to save all scheduled appointments to a file (Y/N)? ").upper()
    if choice == "Y":
        filename = input("Enter appointment filename: ")
        if os.path.isfile(filename):
            choice = input("File already exists, do you want to overwrite it (Y/N)? ").upper()
            if choice == "N":
                newFile = input("Enter appointment filename: ")
                with open(f"{newFile}", "x") as myfile:
                    for appointment in appointment_list:                 
                        if appointment.appt_type != 0:                     
                            myfile.write(appointment.format_record() + "\n")
                            saved_appointments += 1
                print("Good Bye!")
                return
        with open(filename, "a") as myfile:
            for appointment in appointment_list:                 
                if appointment.appt_type != 0:                     
                    if appointment.format_record() not in myfile.read():
                        myfile.write(appointment.format_record())
                        saved_appointments += 1
        print(f"{saved_appointments} scheduled appointments have been successfully saved")
    
    print("Good Bye!")
    

def main():
    appt_manager1.load_scheduled_appointments(appointment_list) 
    while True:
        getInput = appt_manager1.print_menu()
        if getInput == "1":

            print("** Schedule an appointment **")
            day = input("What day: ")
            start_hour = input("Enter start hour (24 hour clock): ")
            selected_appointment = None
            for appointment in appointment_list:
                if appointment.day_of_week == day and appointment.start_time_hour == int(start_hour):
                    selected_appointment = appointment
                    if appointment.appt_type != 0:
                        print("Sorry that time slot is booked already!")                      
                    else: 
                        client_name = input("Client Name: ")
                        client_phone = input("Client Phone: ")
                        print("1: Mens Cut $40, 2: Ladies Cut $60, 3: Men's Colouring $40, 4: Ladies Colouring $80")
                        appointment_type = int(input("Type of Appointment: "))
                        selected_appointment.schedule(client_name, client_phone, appointment_type)
                        print("OK,", client_name + "'s appointment is scheduled!")
                        break
            print("Sorry, that time slot is not in the weekly calendar!")
                    

        if getInput == "2":
            print("\n** Find appointment by name **")
            client_name = input("Enter client name: ")
            appt_manager2.show_appointments_by_name(appointment_list, client_name)

        if getInput == "3":
            print("")
            print("** Print calendar for a specific day **")
            day = input("Enter day of week: ")
            print(f"Appointments for {day}")
            appt_manager2.show_appointments_by_day(appointment_list, day)

        if getInput == "4":
            print("\n** Cancel an appointment **")
            day = input("What day: ")
            start = int(input("Enter start hour (24 hour clock): "))
            for appt in appointment_list:
                if day == appt.day_of_week and start == appt.start_time_hour:
                    if appt.appt_type == 0:
                        print("The timeslot isn't booked and doesn't need to be cancelled")
                        break
                    print(f"Appointment: {day} {start}:00 - {appt.get_end_time_hour()} for {appt.client_name}:00 has been cancelled!")
                    appt.cancel()
                    break
                    
            #Continue, unfinished

        if getInput == "5":
            print("")
            appt_manager2.change_appointment_by_day(appointment_list)

        if getInput == "6":
            appt_manager2.calculate_fees_per_day(appointment_list)
            
        if getInput == "7":
            print("")
            calculate_weekly_fees(appointment_list)

        if getInput == "9":
            save_scheduled_appointments(appointment_list)
            break     

                

main()




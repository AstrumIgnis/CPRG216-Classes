# import os 
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
    choice = input("Would you like to save all scheduled appointments to a file (Y/N)? ").upper()
    if choice == "Y":
        filename = input("Enter appointment filename: ")
        saved_appointments = 0
        with open(filename, "a") as myfile:
            for appointment in appointment_list:
                 
                if appointment.appt_type != 0:
                     
                    if appointment.format_record() not in myfile.read():
                        myfile.write(appointment.format_record())
                        saved_appointments += 1
        print(f"{saved_appointments} scheduled appointments have been successfully saved")
    
    print("Good Bye!")
    

def main():
    loop = True
    while loop == True:
        if appt_manager1.print_menu() == "1":

            print("** Schedule an appointment **")
            day = input("What day: ")
            start_hour = input("Enter start hour (24 hour clock): ")
            for appointment in appointment_list:
                if appointment.day_of_week == day and appointment.start_time_hour == start_hour:
                    selected_appointment = appointment
                    if appointment.appt_type != 0:
                      print("Sorry that time slot is booked already!")
                      return
                    else: break
            client_name = input("Client Name: ")
            client_phone = input("Client Phone: ")
            print("1: Mens Cut $40, 2: Ladies Cut $60, 3: Men's Colouring $40, 4: Ladies Colouring $80")
            appointment_type = input("Type of Appointment: ")
            selected_appointment.schedule(client_name, client_phone, appointment_type)
            print("OK,", client_name + "'s appointment is scheduled!")

        if appt_manager1.print_menu == "2":
                print("")
                print("** Find appointment by name **")
                client_name = input("Enter client name: ")
                appt_manager2.show_appointments_by_name(appointment_list, client_name)

        if appt_manager1.print_menu == "3":
            print("")
            print("** Print calendar for a specific day **")
            day = input("Enter day of week: ")
            print(f"Appointments for {day}")
            appt_manager2.show_appointments_by_day(appointment_list)

        if appt_manager1.print_menu == "4":
            pass
            print("** Cancel an appointment **")
            day = input("What day: ")
            start = input("Enter start hour (24 hour clock)")
            appointment.cancel(appointment_list, day, start)
            if day and start in appointment_list:
                 break
            #Continue, unfinished

        if appt_manager1.print_menu == "5":
            print("")
            print("Change an appointment for:")
            day = input("What day: ")
            start = input("Enter start hour (24 hour clock): ")
            appt_manager2.change_appointment_by_day()

            if appt_manager1.print_menu == "6":
                 print("")
                 print("Fee's calculation per day....")
                 day = input("What day: ")
            
            if appt_manager1.print_menu == "7":
                 print("")
                 calculate_weekly_fees(appointment_list)

            if appt_manager1.print_menu == "8":
                 pass     

                

main()




class Appointment:

    # Initializer
    def __init__(self, day_of_week="", start_time_hour="", client_name="", client_phone="", appt_type=0):
        self.__client_name = client_name
        self.__client_phone = client_phone
        self.__appt_type = appt_type
        self.__day_of_week = day_of_week
        self.__start_time_hour = start_time_hour


    #Getters

    def get_client_name(self):
        return self.__client_name

    def get_client_phone(self):
        return self.__client_phone

    def get_appt_type(self):
        return self.__appt_type

    def get_day_of_week(self):
        return self.__day_of_week

    def get_start_time_hour(self):
        return self.__start_time_hour
    
    #Setters

    def set_client_name(self, new_client_name):
        self.__client_name = new_client_name

    def set_client_phone(self, new_client_phone):
        self.__client_phone = new_client_phone

    def set_appt_type(self, new_appt_type):
        self.__appt_type = new_appt_type

    #Provides the appointment types descriptions
    def get_appt_type_description(self):
        descriptions = {
            0: "Available",
            1: "Mens Cut",
            2: "Ladies Cut",
            3: "Mens Colouring",
            4: "Ladies Colouring",
        }
        return descriptions

    
    def appt_type(self):
        if self.get_appt_type() == 0:
            result = "Available"
            return result

        if self.get_appt_type() == 1:
            result = "Mens Cut"
            return result
        
        if self.get_appt_type() == 2:
            result = "Ladies Cut"
            return result
        
        if self.get_appt_type() == 3:
            result = "Mens Colouring"
            return result
        
        if self.get_appt_type() == 4:
            result = "Ladies Colouring"
            return result
  
    #Gets the end appointments end time in hours
    def get_end_time_hour(self):
        end_time = int(self.get_start_time_hour()) + 1
        return end_time
    
    #Schedule a new appointment
    def schedule(self, new_client_name, new_client_phone, new_appt_type):
        self.__client_name = new_client_name
        self.__client_phone = new_client_phone
        self.__appt_type = new_appt_type
    
    #Cancel an appointment
    def cancel(self):
        self.set_client_name("")
        self.set_client_phone("")
        self.set_appt_type(0) 

    #Prints a string containing all of an appointments properties
    def format_record(self):
        return f"{self.get_client_name()} {self.get_client_phone()} {self.get_day_of_week()} {self.get_start_time_hour()}:00 - {self.get_end_time_hour()}:00 {self.appt_type()}"


    #Prints a string containing the appointments properties
    def __str__(self):
        return f"{self.get_client_name():20}{self.get_client_phone():15}{self.get_day_of_week():10}{self.get_start_time_hour()}:00 - {self.get_end_time_hour()}:00   {self.appt_type()}"

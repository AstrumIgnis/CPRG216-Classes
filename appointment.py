class Appointment:
    def __init__(self, day_of_week, start_time_hour):
        self.client_name = 0
        self.client_phone = 0
        self.appt_type = 0
        self.day_of_week = day_of_week
        self.start_time_hour = start_time_hour
        
        
    def get_client_name(self):
        return self.client_name
    
    def get_client_phone(self):
        return self.client_phone
    
    def get_appt_type(self):
        return self.appt_type
    
    def get_day_of_week(self):
        return self.day_of_week
    
    def get_start_time_hour(self):
        return self.start_time_hour

    def get_appt_type_desc(self):
        match self.appt_type:
            case 0:
                return "Available"
            case 1:
                return "Mens Cut"
            case 2: 
                return "Ladies Cut"
            case 3:
                return "Mens Colouring"
            case 4: 
                return "Ladies Colouring"
    
    def get_end_time_hour(self):
        return (self.start_time_hour + 1)
    
    def set_client_name(self, client_name):
        self.client_name = client_name
        
    def set_client_phone(self, client_phone):
        self.client_phone = client_phone
        
    def set_appt_type(self, appt_type):
        self.appt_type = appt_type
        
    def schedule(self, client_name, client_phone, appt_type):
        self.set_client_name(client_name)
        self.set_client_phone(client_phone)
        self.set_appt_type(0)
        
    def cancel(self):
        self.set_client_name(0)
        self.set_client_phone(0)
        self.set_appt_type(0)
        
    def format_record(self):
        return f"{self.client_name},{self.client_phone},{self.appt_type},{self.day_of_week},{self.start_time_hour}"
    
    def __str__(self):
        return f"{self.client_name:<20}{self.client_phone:<15}{self.day_of_week:<10}{self.start_time_hour:0>2}:00  -  {self.get_end_time_hour():0>2}:00     {self.get_appt_type_desc()}"

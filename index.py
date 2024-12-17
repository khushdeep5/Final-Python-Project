class Doctor:
    def __init__(self, doctor_id='', name='', specialization='', working_time='', qualification='', room_number=''):
        self._doctor_id = doctor_id
        self._name = name
        self._specialization = specialization
        self._working_time = working_time
        self._qualification = qualification
        self._room_number = room_number
    
    def get_doctor_id(self):
        return self._doctor_id
    
    def get_name(self):
        return self._name
    
    def get_specialization(self):
        return self._specialization
    
    def get_working_time(self):
        return self._working_time
    
    def get_qualification(self):
        return self._qualification
    
    def get_room_number(self):
        return self._room_number
    
    def set_doctor_id(self, new_id):
        self._doctor_id = new_id
    
    def set_name(self, new_name):
        self._name = new_name
    
    def set_specialization(self, new_specialization):
        self._specialization = new_specialization
    
    def set_working_time(self, new_working_time):
        self._working_time = new_working_time
    
    def set_qualification(self, new_qualification):
        self._qualification = new_qualification
    
    def set_room_number(self, new_room_number):
        self._room_number = new_room_number
    
    def __str__(self):
        return f"{self._doctor_id}_{self._name}_{self._specialization}_{self._working_time}_{self._qualification}_{self._room_number}"
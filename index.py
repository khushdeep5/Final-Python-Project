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
    
class DoctorManager():
    #contrusctor
    def __init__(self):
        self.doctors=[]
        self.read_doctor_file()

    #formatiing doctors info
    def format_dr_info(doctor):
       return f"{doctor.doctor_id}_{doctor.name}_{doctor.specialization}_{doctor.working_time}_{doctor.qualification}_{doctor.room_number}"

    #entering doctor info
    def enter_dr_info(self):
        doctor_id=int(input("Enter the doctor’s ID: "))
        name=input("Enter the doctor’s name: ")
        speciality=input("Enter the doctor’s specility: ")
        working_time=input("Enter the doctor’s timing (e.g., 7am-10pm): ")
        qualification=input("Enter the doctor’s qualification: ")
        room_number=int(input("Enter the doctor’s room number: "))

        doctor=Doctor(doctor_id,name,speciality,working_time,qualification,room_number)
        return doctor

    #reads doctors.txt
    def read_doctor_file(self):
        doctor=open('doctors.txt','r')
        lines=doctor.readlines()

        for line in lines:
            entry=line.split('_')
            doctor_id,name,speciality,working_time,qualification,room_number=entry

            doctor_entry=Doctor(doctor_id,name,speciality,working_time,qualification,room_number)

            self.doctors.append(doctor_entry)

        doctor.close()
    def search_doctor_by_id(self):
        doc_id=input('Enter the Doctor ID: ')
        for doctor in self.doctors:
            if doctor.get_doctor_id()==doc_id:
                self.display_doctor_info(doctor)
                break
                
        print(f"Can't find the doctor ...........")
    def search_doctor_by_name(self):
        doc_name=input('Enter the Doctor name: ')
        for doctor in self.doctors:
            if doctor.get_doctor_name()==doc_name:
                self.display_doctor_info(doctor)
                break
        print(f"Can't find the doctor ...........")
        
    def display_doctor_info(self,doctor):
        print(f'ID    Name                Speciality      Timings          Qualification    Room Number')
        print(f'{doctor.get_doctor_id():<6}{doctor.get_doctor_name():<20}{doctor.get_specialization():<16}{doctor.get_working_time():<16} {doctor.get_qualification():<16} {doctor.get_room_number()}')

    def edit_doctor_info(self):
        search_id = input("Please enter the id of the doctor that you want to edit their information: ")
        for doctor in self.doctors:
            if doctor.get_doctor_id() == search_id:
                doctor.set_name(input("Enter new Name: "))
                doctor.set_specialization(input("Enter new Specilist in: "))
                doctor.set_working_time(input("Enter new Timing: "))
                doctor.set_qualification(input("Enter new Qualification: "))
                doctor.set_room_number(input("Enter new Room number: "))
                
                self.write_list_of_doctors_to_file()
                print(f"\nDoctor whose ID is {search_id} has been edited")
                return
        print("Cannot find the doctor …...")

    def display_doctors_list(self):
        print(f'ID    Name                Speciality      Timings          Qualification    Room Number')
        for doctor in self.doctors:
            print(f'{doctor.get_doctor_id():<6}{doctor.get_doctor_name():<20}{doctor.get_specialization():<16}{doctor.get_working_time():<16} {doctor.get_qualification():<16} {doctor.get_room_number()}')

    def write_list_of_doctors_to_file(self):
        doctor=open('doctors.txt', 'w')
        for i in self.doctor:
            doctor.write(self.format_dr_info(doctor) + '\n')

    def add_dr_to_file(self):
        new_doc=self.enter_dr_info()
        self.doctors.append(new_doc)

        doctor=open('doctors.txt', 'a')
        doctor.write(self.format_dr_info(new_doc)+ '\n')
        print(f"\nDoctor whose ID is {new_doc.get_doctor_id()} has been added")










        

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


class Patient:
    def __init__(self, p_id='', name='', disease='', gender='', age=''):
        self.p_id = p_id
        self._name = name
        self._disease = disease
        self._gender = gender
        self._age = age
    
    def get_p_id(self):
        return self._pid
    
    def get_name(self):
        return self._name
    
    def get_disease(self):
        return self._disease
    
    def get_gender(self):
        return self._gender
    
    def get_age(self):
        return self._age
    
    def set_pid(self, new_pid):
        self.p_id = new_pid
    
    def set_name(self, new_name):
        self._name = new_name
    
    def set_disease(self, new_disease):
        self._disease = new_disease
    
    def set_gender(self, new_gender):
        self._gender = new_gender
    
    def set_age(self, new_age):
        self._age = new_age
    
    def __str__(self):
        return f"{self.p_id}_{self._name}_{self._disease}_{self._gender}_{self._age}"

class PatientManager:
    def __init__(self):
        self.patients = []
        self.read_patients_file()
    
    def format_patient_info_for_file(self, patient):
        return f"{patient.get_p_id()}_{patient.get_name()}_{patient.get_disease()}_{patient.get_gender()}_{patient.get_age()}"
    
    def enter_patient_info(self):
        p_id = input("Enter Patient id: ")
        name = input("Enter Patient name: ")
        disease = input("Enter Patient disease: ")
        gender = input("Enter Patient gender: ")
        age = input("Enter Patient age: ")
        
        return Patient(p_id, name, disease, gender, age)
    
    def read_patients_file(self):
        patient=open('doctors.txt','r')
        lines=patient.readlines()

        for line in lines:
            entry=line.split('_')
            p_id,name,disease,gender,age=entry

            p_entry=Patient(p_id,name,disease,gender,age)

            self.patients.append(p_entry)

        patient.close()

    def search_pateint_by_id(self):
        pat_id=input('Enter the Doctor ID: ')
        for patient in self.patients:
            if patient.get_p_id()==pat_id:
                self.display_patient_info(patient)
                break      
        print(f"Can't find the doctor ...........")
    
    def display_patient_info(self,patient):
        
        print(f'ID    Name                disease      Gender         Age')
        print(f'{patient.get_p_id():<6}{patient.get_name():<15}{patient.get_disease():<12}{patient.get_gender():<12} {patient.get_age():<12}')

    def edit_patient_info_by_id(self):
        pat_id=input('Enter the Doctor name: ')
        for patient in self.patients:
            if patient.get_p_id()==pat_id:
                self.display_patient_info(patient)
                break
        print(f"Can't find the doctor ...........")

    def display_patient_list(self):
        print(f'ID    Name                disease      Gender         Age')
        for patient in self.patients:
            print(f'{patient.get_p_id():<6}{patient.get_name():<15}{patient.get_disease():<12}{patient.get_gender():<12} {patient.get_age():<12}')

    def write_list_of_patients_to_file(self):
        patient=open('pateints.txt', 'w')
        for i in self.patients:
            patient.write(self.format_patient_info(patient) + '\n')

    def add_dr_to_file(self):
        new_pat=self.enter_patient_info()
        self.patients.append(new_pat)

        patient=open('patients.txt', 'a')
        patient.write(self.format_patient_info_for_file(new_pat)+ '\n')
        print(f"\nPatient whose ID is {new_pat.get_p_id()} has been added")





    



    








        

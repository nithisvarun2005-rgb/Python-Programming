from abc import ABC, abstractmethod
from enum import Enum


# 1.  Enum
class VisitType(Enum):
    OUTPATIENT = "OutPatient"
    INPATIENT = "InPatient"
    EMERGENCY = "Emergency"


# 2. Abstract  Class
class Visit(ABC):

    def __init__(self, patient, doctor, month, visit_type):
        self.patient = patient
        self.doctor = doctor
        self.month = month
        self.visit_type = visit_type


    @property
    def patient_id(self):
        return self.patient.patient_id

    @abstractmethod
    def calculate_bill(self):
        pass



class OutPatientVisit(Visit):

    def __init__(self, patient, doctor, month, consultation_fee):
        super().__init__(
            patient, doctor, month, VisitType.OUTPATIENT
        )
        self.consultation_fee = consultation_fee

    def calculate_bill(self):
        return self.consultation_fee


class InPatientVisit(Visit):

    def __init__(self, patient, doctor, month, days, daily_charge):
        super().__init__(
            patient, doctor, month, VisitType.INPATIENT
        )
        self.days = days
        self.daily_charge = daily_charge

    def calculate_bill(self):
        return self.days * self.daily_charge


class EmergencyVisit(Visit):

    def __init__(self, patient, doctor, month, base_fee, surcharge):
        super().__init__(
            patient, doctor, month, VisitType.EMERGENCY
        )
        self.base_fee = base_fee
        self.surcharge = surcharge

    def calculate_bill(self):
        return self.base_fee + self.surcharge



class Patient:

    def __init__(self, patient_id, patient_name):
        self.__patient_id = patient_id
        self.patient_name = patient_name

    @property
    def patient_id(self):
        return self.__patient_id


class Doctor:

    def __init__(self, doctor_id, doctor_name, department):
        self.doctor_id = doctor_id
        self.doctor_name = doctor_name
        self.department = department


patient1 = Patient("P101", "Harini")
patient2 = Patient("P102", "Priya")
patient3 = Patient("P103", "Raghu")
patient4 = Patient("P104", "Divya")
patient5 = Patient("P105", "Joshi")



doctor1 = Doctor("D101", "Dr. Raj", "Cardiology")
doctor2 = Doctor("D102", "Dr. Priya", "Orthopedics")
doctor3 = Doctor("D103", "Dr. Kumar", "Emergency")



visits = [
    OutPatientVisit(patient1, doctor1, "January", 500),
    InPatientVisit(patient2, doctor2, "January", 3, 2000),
    EmergencyVisit(patient3, doctor3, "February", 1000, 500),
    OutPatientVisit(patient4, doctor1, "February", 700),
    InPatientVisit(patient5, doctor2, "March", 2, 2500)
]



print("HOSPITAL BILL SUMMARY")

total_revenue = 0

departments = ["Cardiology", "Orthopedics", "Emergency"]
months = ["January", "February", "March"]

# Nested list
monthly_totals = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

for visit in visits:

    bill = visit.calculate_bill()
    total_revenue += bill

    print(f"Patient ID: {visit.patient_id}")
    print(f"Patient Name: {visit.patient.patient_name}")
    print(f"Doctor: {visit.doctor.doctor_name}")
    print(f"Department: {visit.doctor.department}")
    print(f"Visit Type: {visit.visit_type.value}")
    print(f"Bill Amount: Rs. {bill}")
    print("-------------------------")

    
    row = departments.index(visit.doctor.department)
    col = months.index(visit.month)

    monthly_totals[row][col] += bill


print(f"Total Hospital Revenue: Rs. {total_revenue}")


# Department-wise Monthly Collection
print("\nDEPARTMENT-WISE MONTHLY TOTALS")

for i in range(len(departments)):
    print(f"\nDepartment: {departments[i]}")

    for j in range(len(months)):
        print(f"{months[j]}: Rs. {monthly_totals[i][j]}")


# 5. Inheritance vs Composition Example

# Wrong approach: Inheritance
# A Doctor is not a type of Patient.
# Therefore, Doctor should not inherit from Patient.

# class Doctor(Patient):
#     pass


# Correct approach: Composition
# Visit HAS-A Patient and HAS-A Doctor.

# Example:
visit = OutPatientVisit(
    patient1, doctor1, "March", 600
)

print("\nCOMPOSITION EXAMPLE")
print(f"Patient: {visit.patient.patient_name}")
print(f"Doctor: {visit.doctor.doctor_name}")
print(f"Patient ID: {visit.patient_id}")


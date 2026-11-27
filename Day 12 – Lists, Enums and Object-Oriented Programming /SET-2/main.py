from abc import ABC, abstractmethod
from enum import Enum


# 1. Enum
class VehicleType(Enum):
    CAR = "Car"
    BIKE = "Bike"
    VAN = "Van"


# 2. Abstract  Class
class Vehicle(ABC):

    def __init__(self, registration_number, mileage, vehicle_type):
        self.registration_number = registration_number
        self.mileage = mileage
        self.vehicle_type = vehicle_type

    # Encapsulation 
    @property
    def registration_number(self):
        return self.__registration_number

    @registration_number.setter
    def registration_number(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Invalid registration number")
        self.__registration_number = value

    # Encapsulation 
    @property
    def mileage(self):
        return self.__mileage

    @mileage.setter
    def mileage(self, value):
        if value < 0:
            raise ValueError("Mileage cannot be negative")
        self.__mileage = value

    @abstractmethod
    def daily_rate(self):
        pass

    @abstractmethod
    def late_fee(self, days):
        pass


 
class Car(Vehicle):

    def __init__(self, registration_number, mileage):
        super().__init__(registration_number, mileage, VehicleType.CAR)

    def daily_rate(self):
        return 2000

    def late_fee(self, days):
        return days * 500



class Bike(Vehicle):

    def __init__(self, registration_number, mileage):
        super().__init__(registration_number, mileage, VehicleType.BIKE)

    def daily_rate(self):
        return 500

    def late_fee(self, days):
        return days * 100

class Van(Vehicle):

    def __init__(self, registration_number, mileage):
        super().__init__(registration_number, mileage, VehicleType.VAN)

    def daily_rate(self):
        return 3000

    def late_fee(self, days):
        return days * 800



class Customer:

    def __init__(self, customer_name, customer_id):
        self.customer_name = customer_name
        self.customer_id = customer_id


# Rental Class - HAS-A Relationship
class Rental:

    def __init__(self, vehicle, customer, days, late_days=0):
        self.vehicle = vehicle
        self.customer = customer
        self.days = days
        self.late_days = late_days

    def calculate_amount(self):
        rent = self.days * self.vehicle.daily_rate()
        penalty = self.vehicle.late_fee(self.late_days)

        return rent + penalty


# 4. Current Rentals
customer1 = Customer("Arun", "C101")
customer2 = Customer("Priya", "C102")
customer3 = Customer("Kumar", "C103")

car = Car("TN01AB1234", 15000)
bike = Bike("TN02CD5678", 8000)
van = Van("TN03EF9012", 20000)

rentals = [
    Rental(car, customer1, 3, 1),
    Rental(bike, customer2, 5, 2),
    Rental(van, customer3, 2, 1)
]

print("RENTAL REPORT")

total_revenue = 0

for rental in rentals:

    amount = rental.calculate_amount()
    total_revenue += amount

    print(f"Customer: {rental.customer.customer_name}")
    print(f"Vehicle: {rental.vehicle.vehicle_type.value}")
    print(f"Registration: {rental.vehicle.registration_number}")
    print(f"Rental Amount: Rs. {amount}")
    print("------------------------")

print(f"Total Revenue: Rs. {total_revenue}")


# 5. Refactoring God Class using SRP

# Rental Management Class
class RentalManager:

    def create_rental(self, vehicle, customer, days, late_days=0):
        return Rental(vehicle, customer, days, late_days)


# Billing Class
class BillingService:

    def generate_bill(self, rental):
        return rental.calculate_amount()


# Printing Class
class ReceiptPrinter:

    def print_receipt(self, rental, amount):
        print("\n----- RENTAL RECEIPT -----")
        print(f"Customer: {rental.customer.customer_name}")
        print(f"Vehicle: {rental.vehicle.vehicle_type.value}")
        print(f"Registration: {rental.vehicle.registration_number}")
        print(f"Total Amount: Rs. {amount}")
        print("--------------------------")


# Using separate classes
manager = RentalManager()
billing = BillingService()
printer = ReceiptPrinter()

new_rental = manager.create_rental(
    car, customer1, 4, 2
)

bill_amount = billing.generate_bill(new_rental)

printer.print_receipt(new_rental, bill_amount)


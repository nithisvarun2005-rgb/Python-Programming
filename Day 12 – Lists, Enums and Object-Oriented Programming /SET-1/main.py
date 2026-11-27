from abc import ABC, abstractmethod
from enum import Enum


# 1. PolicyStatus Enum
class PolicyStatus(Enum):
    DRAFT = "Draft"
    ACTIVE = "Active"
    LAPSED = "Lapsed"
    CANCELLED = "Cancelled"


# 2. Abstract Base Class
class Policy(ABC):

    def __init__(self, policy_number, status):
        self.policy_number = policy_number
        self.status = status

    @property
    def policy_number(self):
        return self.__policy_number

    @policy_number.setter
    def policy_number(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Policy number cannot be empty")

        self.__policy_number = value

    @abstractmethod
    def calculate_premium(self):
        pass


# Motor Policy
class MotorPolicy(Policy):

    def __init__(self, policy_number, vehicle_value, status):
        super().__init__(policy_number, status)
        self.vehicle_value = vehicle_value

    def calculate_premium(self):
        return self.vehicle_value * 0.05


# Health Policy
class HealthPolicy(Policy):

    def __init__(self, policy_number, age, status):
        super().__init__(policy_number, status)
        self.age = age

    def calculate_premium(self):
        return 5000 + (self.age * 100)


# Travel Policy
class TravelPolicy(Policy):

    def __init__(self, policy_number, travel_days, status):
        super().__init__(policy_number, status)
        self.travel_days = travel_days

    def calculate_premium(self):
        return self.travel_days * 500


# 3. Create 8 policies
policies = [
    MotorPolicy("M101", 500000, PolicyStatus.ACTIVE),
    MotorPolicy("M102", 300000, PolicyStatus.DRAFT),
    MotorPolicy("M103", 400000, PolicyStatus.ACTIVE),

    HealthPolicy("H101", 25, PolicyStatus.ACTIVE),
    HealthPolicy("H102", 40, PolicyStatus.LAPSED),
    HealthPolicy("H103", 30, PolicyStatus.ACTIVE),

    TravelPolicy("T101", 10, PolicyStatus.ACTIVE),
    TravelPolicy("T102", 15, PolicyStatus.CANCELLED)
]


# Runtime Polymorphism
print("POLICY PREMIUM REPORT")

for policy in policies:
    print(
        f"Policy Number: {policy.policy_number}, "
        f"Status: {policy.status.value}, "
        f"Premium: Rs. {policy.calculate_premium():.2f}"
    )


# 4. Monthly premium collection by region


collections = [
    [10000, 12000, 15000],  
    [20000, 18000, 22000],  
    [15000, 17000, 19000]   
]

regions = ["North", "South", "West"]
months = ["January", "February", "March"]

print("\nREGIONAL COLLECTION TOTALS")

# Row totals
for i in range(len(collections)):
    total = sum(collections[i])
    print(f"{regions[i]} Total: Rs. {total}")


# Column totals
print("\nMONTHLY COLLECTION TOTALS")

for j in range(len(months)):
    total = 0

    for i in range(len(collections)):
        total += collections[i][j]

    print(f"{months[j]} Total: Rs. {total}")


# 5. Add a new Home Policy
class HomePolicy(Policy):

    def __init__(self, policy_number, property_value, status):
        super().__init__(policy_number, status)
        self.property_value = property_value

    def calculate_premium(self):
        return self.property_value * 0.02


# Add Home Policy without modifying existing classes
home_policy = HomePolicy(
    "HM101",
    2500000,
    PolicyStatus.ACTIVE
)

policies.append(home_policy)

print("\nUPDATED POLICY REPORT")

for policy in policies:
    print(
        f"Policy Number: {policy.policy_number}, "
        f"Premium: Rs. {policy.calculate_premium():.2f}"
    )


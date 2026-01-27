# ---------------------------
# Car Rental Management System
# ---------------------------
 
# Parent Class
class Car:
    company = "ZoomCar"   # class variable
    GST = 18              # GST%
 
    def __init__(self, brand, model, price_per_hour):
        self.brand = brand
        self.model = model
        self._price_per_hour = price_per_hour  # encapsulation
 
    def show_details(self):
        print(f"{self.brand} {self.model} - ₹{self._price_per_hour}/hour")
 
    def calculate_cost(self, hours):
        # default implementation
        return self._price_per_hour * hours
 
    @classmethod
    def change_company(cls, name):
        cls.company = name
 
    @staticmethod
    def gst_amount(amount):
        return amount * Car.GST / 100
 
 
# Child Class 1
class ElectricCar(Car):
    def calculate_cost(self, hours):  # polymorphism
        base = self._price_per_hour * hours
        discount = 0.10 * base         # 10% discount for EV cars
        return base - discount
 
 
# Child Class 2
class PetrolCar(Car):
    def calculate_cost(self, hours):   # polymorphism
        base = self._price_per_hour * hours
        service_charge = 50
        return base + service_charge
 
 
# Duration Class (Operator Overloading Example)
class Duration:
    def __init__(self, hours):
        self.hours = hours
 
    def __add__(self, other):
        return Duration(self.hours + other.hours)
 
    def __str__(self):
        return f"{self.hours} hours"
 
 
# Customer Class
class Customer:
    def __init__(self, name, mobile):
        self.name = name
        self.mobile = mobile
 
    def show(self):
        print(f"Customer: {self.name} | Mobile: {self.mobile}")
 
 
# Rental Management
class Rental:
    def __init__(self, customer, car, duration):
        self.customer = customer
        self.car = car
        self.duration = duration
 
    def bill(self):
        base_cost = self.car.calculate_cost(self.duration.hours)
        gst = Car.gst_amount(base_cost)
        final_amount = base_cost + gst
 
        print("\n------ RENTAL BILL ------")
        print(f"Company: {Car.company}")
        self.customer.show()
        self.car.show_details()
        print(f"Rental Duration: {self.duration.hours} hours")
        print(f"Base Cost: ₹{base_cost}")
        print(f"GST (@18%): ₹{gst}")
        print(f"Total Amount: ₹{final_amount}")
        print("----------------------------\n")
 
 
# ---------------------------
# TESTING THE PROJECT
# ---------------------------
 
# Create cars
car1 = ElectricCar("Tata", "Nexon EV", 300)
car2 = PetrolCar("Hyundai", "Creta", 250)
 
# Customer
cust = Customer("Murali mohan", "9999988888")
 
# Duration (using operator overloading)
d1 = Duration(4)   # 4 hours
d2 = Duration(2)   # 2 hours
 
total_duration = d1 + d2   # Overloaded + operator
 
# Create rental
r = Rental(cust, car1, total_duration)
 
# Generate bill
r.bill()    
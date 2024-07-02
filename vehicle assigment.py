class Vehicle:
    def __init__(self, chassis_no, registration_no, max_speed, fuel_type):
        self.chassis_no = chassis_no
        self.registration_no = registration_no
        self.max_speed = max_speed
        self.fuel_type = fuel_type


class Car(Vehicle):
    def car_details(self, make, model, color, num_doors, transmission_type, num_airbags, price):
        self.make = make
        self.model = model
        self.color = color
        self.num_doors = num_doors
        self.transmission_type = transmission_type
        self.num_airbags = num_airbags
        self.price = price
        print(car1.make, car1.model, car1.color)

class Truck(Vehicle):
    def truck_details(self, payload_capacity, towing_capacity, wheelbase, num_wheels):
        self.payload_capacity = payload_capacity
        self.towing_capacity = towing_capacity
        self.wheelbase = wheelbase
        self.num_wheels = num_wheels
        print(truck1.payload_capacity, truck1.towing_capacity, truck1.num_wheels)

class Bike(Vehicle):
    def bike_details(self, seat_height, wheel_size, engine_size, acceleration):
        self.seat_height = seat_height
        self.wheel_size = wheel_size
        self.engine_size = engine_size
        self.acceleration = acceleration
        print(bike1.seat_height, bike1.engine_size, bike1.acceleration)

car1 = Car("1234", "ABC123", 200, "Petrol")
car1.car_details("Toyota", "Corolla", "Red", 4, "Automatic", 6, 25000)

truck1 = Truck("5678", "XYZ789", 150, "Diesel")
truck1.truck_details(5000, 10000, 200, 6)

bike1 = Bike("9012", "DEF456", 180, "Petrol")
bike1.bike_details(80, 26, "250cc", "High")





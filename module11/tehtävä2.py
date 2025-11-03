class Car:
    def __init__(self,license_plate,maximum_speed,current_speed=0,travelled_distance=0):
        self.license_plate=license_plate
        self.maximum_speed=maximum_speed
        self.current_speed=current_speed
        self.travelled_distance=travelled_distance
    def accelerate(self,speed):
        self.current_speed=self.current_speed + speed
        if self.current_speed<0:
            self.current_speed=0
        elif self.current_speed>self.maximum_speed:
            self.current_speed=self.maximum_speed
    def drive(self,time):
        self.travelled_distance += self.current_speed * time

class ElectricCar(Car):
    def __init__(self,license_plate,maximum_speed,battery_capacity):
        self.battery_capacity=battery_capacity
        super().__init__(license_plate,maximum_speed)

class GasolineCar(Car):
    def __init__(self,license_plate,maximum_speed,tank_volume):
        self.tank_volume=tank_volume
        super().__init__(license_plate, maximum_speed)

import random
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

class Race:
    def __init__(self,name,distance,cars):
        self.name=name
        self.distance=distance
        self.cars=cars

    def hour_passes(self):
        for car in self.cars:
            random_speeds = random.randint(-10,16)
            car.accelerate(random_speeds)
            car.drive(1)

    def print_status(self):
        print(f"{'License plate':<12} | {'Maximum speed':<14} | {'Current speed':<14} | {'Travelled distance':<14}")
        print("-" * 68)
        for car in self.cars:
            print(f"{car.license_plate:<13} | {car.maximum_speed:<14} | {car.current_speed:<14} | {car.travelled_distance:<14}")

    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance>=self.distance:
                return True
        return False

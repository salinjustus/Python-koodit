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
def race():
    cars = []
    random_maxspeeds = random.sample(range(100,201),10)
    for i in range(10):
        license_plate=f"ABC-{i+1}"
        car=Car(license_plate,random_maxspeeds[i])
        cars.append(car)
    while True:
        race_result = False
        for car in cars:
            random_speeds = random.sample(range(-10, 16), 10)
            car.accelerate(random_speeds[i])
            car.drive(1)
        for car in cars:
            if car.travelled_distance>=10000:
                race_result=True
        if race_result==True:
            break
    cars.sort(key=lambda car:car.travelled_distance,reverse=True)
    return cars





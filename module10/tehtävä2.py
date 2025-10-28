class Elevator:
    def __init__(self,bottom_floor,top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor
    def go_to_floor(self,level):
        if level>self.current_floor:
            while level>self.current_floor:
                self.floor_up()
        elif level<self.current_floor:
            while level<self.current_floor:
                self.floor_down()

    def floor_up(self):
        self.current_floor=self.current_floor + 1
        print(self.current_floor)

    def floor_down(self):
        self.current_floor = self.current_floor - 1
        print(self.current_floor)

class Building:
    def __init__(self,bottom_floor,top_floor,elevator_amount):
        self.elevators = []
        self.bottom_floor=bottom_floor
        self.top_floor=top_floor
        self.elevator_amount=elevator_amount
        for i in range(elevator_amount):
            self.elevators.append(Elevator(bottom_floor,top_floor))

    def run_elevator(self,elevator_number,destination_floor):
        self.elevators[elevator_number].go_to_floor(destination_floor)
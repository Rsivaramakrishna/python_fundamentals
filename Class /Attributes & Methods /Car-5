# Implement the Car class appropriately
class Car:
    is_engine_started = False
    current_speed = 0
    def __init__(self, color, max_speed, acceleration, tyre_friction):
        self.color = color
        self.max_speed = max_speed
        self.acceleration = acceleration
        self.tyre_friction = tyre_friction

    def start_engine(self):
        self.is_engine_started = True

    def stop_engine(self):
        self.is_engine_started = False

    def accelerate(self):
        if  self.is_engine_started == False:
            print("Car has not started yet")
        else:
            self.current_speed += self.acceleration
            
            if self.current_speed > self.max_speed:
                self.current_speed = self.max_speed

    def apply_brakes(self):
        if self.current_speed > 2:
            self.current_speed = self.current_speed - self.tyre_friction
        else:
            self.current_speed = 0

    def sound_horn(self):
        if self.is_engine_started == False:
            self.accelerate()
        else:
            print("Beep Beep")
        


# You need not change any code below.
# Do not call this function anywhere. It will automatically be called internally during tests.
def default_test():
 car = Car(color="Red", max_speed=250, acceleration=10, tyre_friction=3)
 car.sound_horn() # Calling sound_horn() method when the is_engine_started is False
 car.start_engine() # Starting the engine
 car.sound_horn() # Calling the accelerate method when the is_engine_started is True

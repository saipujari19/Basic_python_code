class Treadmill():
    def __init__(self):
        self.speed = 0.0
        self.incline = 0
        self.started = False
    def start(self):
        self.started = True
        print("treadmill started")

    def stop(self):
        self.started = False
        self.speed = 0.0
        self.incline = 0
        print("stop treadmill")

    def increase_speed(self):
        if self.started:
            self.speed = self.speed + 0.5
            print(f"speed is increased to {self.speed} mph")

    def decrease_speed(self):
        if self.started and self.speed >= 0.5:
            self.speed = self.speed - 0.5
            print(f"Speed is decreased to {self.speed} mph")

    def increase_incline(self):
        if self.started:
            self.incline = self.incline + 1
            print(f"incline is increased to {self.incline}")

    def decrease_incline(self):
        if self.started and self.incline >= 1:
            self.incline = self.incline - 1
            print(f"incline is decreased to {self.incline}")

    def set_speed_to_3(self, speed):
        self.set_speed_to_3(3)

    def set_speed_to_5(self, speed):
        self.set_speed_to_5()

    def set_speed_to_9(self, speed):
        self.set_speed_to_9(9)

    def set_incline_to_3(self, incline):
        self.set_incline(3)

    def set_incline_to_9(self, incline):
        self.set_incline()

    def set_incline_to_15(self, incline):
        self.set_incline()

    def set_speed(self, speed):
        if self.started:
            self.speed = speed
            print(f"speed is set to {self.speed} mph")
    def get_speed(self):
        return self.speed

    def set_incline(self, incline):
        if self.started:
            self.incline = incline
            print(f"incline is set to {self.incline}.")

    def get_incline(self):
        return self.incline


def main():
    treadmill = Treadmill()
    treadmill.start()
    treadmill.increase_speed()
    treadmill.set_speed_to_3()
    treadmill.set_speed_to_9()
    treadmill.increase_incline()
    treadmill.set_incline_to_3()
    print(f"current speed: {treadmill.get_speed()} mph")
    print(f"current incline: {treadmill.get_incline()}")
    treadmill.stop()
if __name__ == "__main__":
    main()


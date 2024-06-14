class car:
    def __init__(self, color, car_type, year):
        self.speed = 0
        self.color = color
        self.car_type = car_type
        self.year = year
        self.is_started = False
    def start(self):
        if self.is_started:
            print("it is already started")
            return
        self.is_started = True



     def acceleration(self, speed):
         if self.is_started:
             self.speed = self.speed + speed
         else:
             print("start the car")

     def main(self):
         car = Car(color:"silver", car_type: "suv", year: 2020)
         car.acceleration(30)
         car.start()
         print(car.speed)
     if __name__ == '__main__':

         
         main()


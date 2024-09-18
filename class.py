import os



class Car:
    def __init__(self, make,model,color):
        self.make  = make 
        self.model = model 
        self.color = color 
    
    def view_car(self):
        return f"{self.make} - {self.model} - ({self.color})"
        
os.system ('cls')

cars = []

cars.append (Car("lada", "Kalina", "Yellow"))

for car in cars:
    print (car.view_car())

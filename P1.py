import os
os.system('cls')


class Car:
    def __init__(self):
        self.car_details = {}  

    def add_car(self, make, model):
       
        self.car_details[make] = model
        print(f"{make} {model} har lagts till.")

    def list_cars(self):
        
        if self.car_details:
            print("Nuvarande bilar:")
            for index, (make, model) in enumerate(self.car_details.items(), start=1):
                print(f"{index}. {make} - {model}")
        else:
            print("Inga bilar finns tillgängliga.")

    def remove_car(self, make):
        
        if make in self.car_details:
            del self.car_details[make]
            print(f"{make} har tagits bort.")
        else:
            print(f"{make} finns inte i listan.")


cars = Car()


while True:
    print("\nVad vill du göra?")
    print("1. Lägg till en bil")
    print("2. Ta bort en bil")
    print("3. Avsluta")
    
    choice = input("Välj ett alternativ (1/2/3): ")

    if choice == '1':
        
        make = input("Ange bilmärke: ")
        model = input("Ange bilmodell: ")
        cars.add_car(make, model)
        cars.list_cars()
    
    elif choice == '2':
        
        make = input("Ange bilmärket på bilen du vill ta bort: ")
        cars.remove_car(make)
    
        
    elif choice == '3':
        
        print("Programmet avslutas.")
        break
    else:
        print("Ogiltigt val, försök igen.")

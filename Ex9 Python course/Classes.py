# Aviya Keisar _311515415

class CarStore:
    '''This class represents a car store. Its components are: name of the owner, incomes of the store and a list of cars
    that contains car objects'''

    def __init__(self, name):
        self.name = name
        self.income = 0
        self.cars_in_store = []

    def get_car_details(self):
        manufacturer = input("Manufacturer: ")
        model = input("Model: ")
        amount = int(input("Amount: "))
        return manufacturer, model, amount

    def append_car_to_list(self, manufacturer, model, amount):
        price = int(input("Price: "))
        new_car = Car(manufacturer, model, amount, price)
        self.cars_in_store.append(new_car)

    def add_cars(self):
        is_present = False
        print("New cars details")
        manufacturer, model, amount = self.get_car_details()
        if self.cars_in_store:  # ONLY if the list contains any car, go over it and check if the car already exists
            for car in self.cars_in_store:
                if car.manufacturer == manufacturer and car.model == model:
                    car.add(amount)
                    is_present = True
                    break
            if not is_present:
                self.append_car_to_list(manufacturer, model, amount)
        else:  # list is empty
            self.append_car_to_list(manufacturer, model, amount)

    def sell_car(self):
        is_present = False
        print("Sell cars details")
        manufacturer, model, amount = self.get_car_details()
        if self.cars_in_store:  # go over the car list ONLY if it's not empty.
            for car in self.cars_in_store:
                if car.manufacturer == manufacturer and car.model == model:
                    if car.amount < amount:
                        is_present = True
                        print("Not enough cars")
                    else:
                        deal_cost = amount * car.price
                        car.remove(amount)
                        self.income += deal_cost
                        print("Sell " + str(amount) + " cars in " + str(deal_cost) + "$")
                        is_present = True
                    if car.amount == 0:
                        self.cars_in_store.remove(car)
                    break
            if not is_present:
                print("Requested car doesn't exist")

    def print_cars(self):
        for car in self.cars_in_store:
            print(car.__repr__())

    def calc_total_amount_of_cars(self):
        counter = 0
        for car in self.cars_in_store:
            counter += car.amount
        return counter

    def __repr__(self):
        num_of_cars = self.calc_total_amount_of_cars()
        return self.name + "'s car store: holds " + str(num_of_cars) + " cars and " + str(self.income) + "$"


class Car:
    '''This class represents a car. It has the following attributes: manufacturer, model, amount and price'''

    def __init__(self, manufacturer, model, amount, price):
        self.manufacturer = manufacturer
        self.model = model
        self.amount = int(amount)
        self.price = int(price)

    def add(self, num):
        self.amount += int(num)

    def remove(self, num):
        if num > self.amount:
            raise ValueError
        else:
            self.amount -= int(num)

    def __repr__(self):
        return str(self.amount) + ' ' + self.manufacturer + ' ' + self.model + ": Price is: " + str(self.price) + "$"

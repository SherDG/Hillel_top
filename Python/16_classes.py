class MyCar:
    wheels = 4

    def my_car_details(self):
        print("Hello, I'm your new car")

    # def bip(self, brand):
        # if brand == 'BMW':
        #     print('Das bip!')
        # elif brand == 'Porshe':
        #     print('Der bip!')
        # else:
    def bip(self):
            print('Bip!')



# my_car = MyCar()
# my_old_car = MyCar()
# my_old_car_2 = MyCar()
# my_car.my_car_details()
# print(my_car.wheels)
# print(my_car.my_car_details())


class MyFirstCar(MyCar):
    def __init__(self):
        self.brand = "VW"
        self.wheels = 4

    def my_car_details(self):
        print(f'Hello, {self.brand}')
        print(f'I have, {self.wheels}')

vw = MyFirstCar()
vw.my_car_details()
# course link https://www.youtube.com/watch?v=H2EJuAcrZYU
#<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Start From Time 5:53:29 To 6:12:27 
# #<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


print("********* Classes & Objects *********")

class vehicle:
    def __init__(self,make,model):
        self.make = make
        self.model = model

    def moves(self):
        print(f'{self.make} {self.model} moves along...')

    def get_make(self):
        return self.make
    
    def get_model(self):
        return   self.model
    



my_car = vehicle("tesla","M3")



print(my_car.make)
print(my_car.model)
my_car.moves()


your_car = vehicle("Kia","Soul")

your_car.moves()

print('------------------------')
print('Inhaetince class')

class Airplane(vehicle):
    #Add Iem not in father class
    def __init__(self,make,model,f_id):
        super().__init__(make,model)
        self.f_id =   f_id

    def moves(self):
        print(f'{self.f_id} Flies along')



class Truck(vehicle):
    def moves(self):
        print('Rumbles along ....')





class GolfCart(vehicle):
    pass



class Train(vehicle):
    def moves(self):
        return super().moves()
    


cessna = Airplane("cessna","skyhowk","23547546468")
mack = Truck("Mack","Pinnacle")
golfwago = GolfCart("yamaha","Gc1111")
trainn = Train("AlAspany","MSR10")

cessna.moves()
mack.moves()
golfwago.moves()
trainn.moves()

print(trainn.get_model())



print('-----------------------------')
for v in (my_car,your_car,cessna,mack,golfwago,trainn):
    v.moves


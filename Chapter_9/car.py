""" Класс для представления автомобиля. """

class Car():
    """ Простая модель автомобиля """
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """ Вывод информации об автомобиле. """
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """ Чтение информации о пробеге. """
        print(f"This car has {self.odometer_reading} miles on it.")
        
    def update_odometer(self, mileage):
        """ Установка определенного пробега. """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
            
    def increment_odometer(self, miles):
        """ Добавление пробега на определенную величину. """
        self.odometer_reading += miles
        
        
class Battery():
    """ Простая модель аккумулятора электромобиля. """
    
    def __init__(self, battery_size=75):
        """ Инициализирует модель аккумулятора. """        
        self.battery_size = battery_size
        
    def describe_battery(self):
        """ Выводит информацию о мощности аккумулятора """               
        print(f"This car has a {self.battery_size}-kWh battery.")
        
    def get_range(self):
        """ Выводит приблизительный запас хода для аккумулятора. """                
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
            
        print(f"This car can go about {range} miles on a full charge.")
        
    def upgrade_battery(self):
        """ Устанавливает мощность аккумулятора = 100. """
        self.battery_size = 100
            

class ElectricCar(Car):
    """ Представляет аспекты машины, специфические для электромобилей. """
    
    def __init__(self, make, model, year):
        """ 
        Инициализирует атрибуты класса-родителя.
        Заттем инициализирует атрибуты, специфичекские для электромобиля.
        """        
        super().__init__(make, model, year)
        self.battery = Battery()
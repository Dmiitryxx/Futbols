import itertools
import datetime
from datetime import time

class TrainingProgram:
    training_category = ''
    training_name = ''
    training_price = ''
    id_iter = itertools.count()
    
    def __init__(self, category=None, name=None, discount=None, price=50):
        self.training_id = next(self.id_iter) + 1
        self.training_category = category
        self.training_name = name
        self.training_discount = discount
        self.training_price_per_hour = price
        self.time_available = True
        
    def training_info(self):
        return [
        self.training_category, self.training_name,
        self.training_discount, self.training_price_per_hour
        ]
   
    def training_info_print(self):
        print('Training category: ' + str(self.training_category))
        print('Training name: ' + str(self.training_name))
        print('Training discount: ' + str(self.training_discount))
        print('Price per hour: ' + str(self.training_price_per_hour))
        print('Time available: ' + str(self.time_available) + '\n')
class Coach:
     coach_first_name = ''
     coach_last_name = ''
     coach_phone_number = 0

     id_iter_coach = itertools.count()
     
def __init__(self, first_name, last_name, phone_number):
     self.coach_id = next(self.id_iter_coach) + 1
     self.coach_first_name = first_name
     self.coach_last_name = last_name
     self.coach_phone_number = phone_number
     
     def coach_info(self):
         return [
    self.coach_first_name, self.coach_last_name, self.coach_phone_number

    ]
     def coach_info_print(self):
         print('Coach first name: ' + self.coach_first_name)
         print('Coach last name: ' + self.coach_last_name)
         print('Phone number: ' + str(self.coach_phone_number) + '\n')
class Usage:
    training_start_time = 0
    training_end_time = 0
    training_date = 0
    training_price_per_hour = 50
    id_TrainingProgram = 0
    id_Coach = 0

id_iter_usage = itertools.count()

def total_price(self):
    total = self.training_price_per_hour * ((
        (self.training_end_time - self.training_start_time)
        ))
    return total_price
def usage_info_print(self):
    print("Training start time: " + str(self.training_start_time))
    print("Training end time: " + str(self.training_end_time))
    print("Training program ID: " + str(self.id_TrainingProgram))
    print("Coach ID: " + str(self.id_Coach))
    print("Price per hour: " + str(self.training_price_per_hour) + "\n")
    
train1 = TrainingProgram("Physical Conditioning", "Endurance Training", "10%", 40)
train2 = TrainingProgram("Technical Skills", "Ball Control", "15%", 50)
train3 = TrainingProgram("Tactical Skills", "Game Strategy", "20%", 60)

print(train1.training_id)
train1.training_info()
train1.training_info_print()
print(train2.training_id)
train2.training_info()
train2.training_info_print()
print(train3.training_id)
train3.training_info()
train3.training_info_print()

coach1 = Coach('Arsens', 'Smirnovs', '136700-23563', 25762341)
coach2 = Coach('Lauris', 'Nizinskis','300779-24675', 23870955)
coach3 = Coach('Jurijs', 'Molostovs', '121203-23464',25678321)

print(coach1.coach_id)
coach1.coach_info()
coach1.coach_info_print()
print(coach2.coach_id)
coach2.coach_info()
coach2.coach_info_print()
print(coach3.coach_id)
coach3.coach_info()
coach3.coach_info_print()






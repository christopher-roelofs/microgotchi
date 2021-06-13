import math
import save
import json
import names
import random

class Pet:
    def __init__(self):
        self.name = names.get_random_name()
        self.age = 0
        self.happiness = 100
        self.hunger = 0
        self.health = 100
        self.avatar = 0

    def get_name(self):
        return self.name

    def get_avatar(self):
        return self.avatar

    def update_age(self,value):
        self.age += value
    
    def get_age(self):
        return int(self.age)
    
    def update_happiness(self,value):
        self.happiness += value
    
    def get_happiness(self):
        return int(self.happiness)

    def update_hunger(self,value):
        self.hunger += value

    def get_hunger(self):
        return int(self.hunger)

    def update_health(self,value):
        self.health += value

    def get_health(self):
        return int(self.health)

    def get_pet_data(self):
        data = {}
        data['name'] = self.name
        data['age'] = self.age
        data['happiness'] = self.happiness
        data['hunger'] = self.hunger
        data['health'] = self.health
        data['avatar'] = self.avatar
        return data

    def load_pet_data(self,data):
        self.name = data['name']
        self.age = data['age']
        self.happiness = data['happiness']
        self.hunger = data['hunger']
        self.health = data['health']
        self.avatar = data['avatar']
    
    def reset(self):
        self.__init__()
        save.save_state(json.dumps(self.get_pet_data()))

    def evaluate_age(self):
        if self.age < 1:
            self.avatar = 0
        if self.age >= 1:
            self.avatar = 1
        if self.age >= 5:
            self.avatar = 2
        if self.age >= 15 :
            self.avatar = 3
        if self.age > 30:
            self.avatar = 4

    def tick(self):
        self.update_age(.01)
        self.update_hunger(.01)
        self.update_happiness(-.001)
        self.update_health(-.001)
        self.evaluate_age()
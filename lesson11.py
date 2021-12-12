class Person():
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def talk(self):
        prt = f'Hi, my name is{self.name}{self.surname},and i have a {self.age} years'
        return prt


my_first_class = Person('Karl', 'Jonson', 26)
print(my_first_class.talk())

class Dog():
    age_factor = 7

    def __init__(self, age_dog=0):
        self.age_dog = age_dog

    def human_age(self, enter_age):
        self.age_dog = enter_age * self.age_factor
        return self.age_dog


dog = Dog()
print(dog.human_age(10))


class TvController():
    def __init__(self, channels):
        self.channels = channels
        self.current_channel = 0

    def first_channels(self):
        return self.channels[0]

    def last_channels(self):
        return self.channels[-1]

    def turn_channels(self, enter):
        if enter <= len(self.channels) and enter >= 1:
            return self.channels[enter - 1]

    def next_channels(self):
        if self.current_channel == len(self.channels) - 1:
            self.current_channel = 0
            return self.channels[self.current_channel]
        self.current_channel += 1
        return self.channels[self.current_channel]

    def previous_channel(self):
        if self.current_channel == 0:
            self.current_channel = - 1
            return self.channels[self.current_channel]
        else:
            self.current_channel -= 1
            return self.channels[self.current_channel]

    def current_channels(self):
        return self.channels[self.current_channel]

    def is_exist(self, enter):
        if type(enter) == int:
            if enter <= len(self.channels) and enter >= 1:
                return 'Yes'
            else:
                return 'No'
        elif type(enter) == str:
            if enter in set(self.channels):
                return 'Yes'
            else:
                return 'No'
        else:
            return 'No'


channels_list = ["BBC", "Discovery", "TV1000"]
controller = TvController(channels_list)
print(controller.first_channels())  # == "BBC"
print(controller.last_channels())  # == "TV1000"
print(controller.turn_channels(1))  # == "BBC"
print(controller.next_channels())  # == "Открытие"
print(controller.previous_channel())  # == "BBC"
print(controller.current_channels())  # == "BBC"
print(controller.is_exist(4))  # == "No"
print(controller.is_exist("BBC"))  # == "Yes"

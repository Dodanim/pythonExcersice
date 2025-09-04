class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def greeting(self):
        print(f'My name is: {self.name} I am a:  {self.breed}')

dog1= Dog('Killer', 'Doberman')

dog1.greeting()
class Animal:

    def __init__(self,animals='animal', language='make sounds'):
        self.pets = animals
        self.lng = language

    def setpecies(self, animals):
        self.pets = animals

    def setLanguage(self,language):
        self.lng = language

    def speak(self):
        print('I amd a {} and I {}'. format(self.pets, self.lng ))

snoopy=Animal()
snoopy.setpecies('dog')
snoopy.setLanguage('bark')
snoopy.speak()

snoopy = Animal('dog', 'bark')
snoopy.speak()

snoopy = Animal('canary')
snoopy.speak()

snoopy = Animal()
snoopy.speak()
class Animal:

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
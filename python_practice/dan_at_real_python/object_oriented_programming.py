#!/usr/bin/env python3

class Dog:
  # Class attribute
  species = "Canis familiaris"

  #def __init__(self, name, age):
  #  self.name = name
  #  self.age = age

  def __init__(self, name, age, breed):
    self.name = name
    self.age = age
    self.breed = breed

  # Instance method
  #def description(self):
  #  return f"{self.name} is {self.age} years old"

  # Replace .description() with __str__()
  def __str__(self):
    return f"{self.name} is {self.age} years old"

  # Another instance method
  def speak(self, sound):
    return f"{self.name} says {sound}"


#buddy = Dog("Buddy", 9)
#miles = Dog("Miles", 4)

#buddy.name
#'Buddy'
#buddy.age
#9

#miles.name
#'Miles'
#miles.age
#4

#buddy.species
#'Canis familiaris'


#miles = Dog("Miles", 4)

#miles.description()
#'Miles is 4 years old'

#print(miles)
#'Miles is 4 years old'

#miles.speak("Woof Woof")
#'Miles says Woof Woof'

#miles.speak("Bow Wow")
#'Miles says Bow Wow'


miles = Dog("Miles", 4, "Jack Russell Terrier")
buddy = Dog("Buddy", 9, "Dachshund")
jack = Dog("Jack", 3, "Bulldog")
jim = Dog("Jim", 5, "Bulldog")

buddy.speak("Yap")
#'Buddy says Yap'

jim.speak("Woof")
#'Jim says Woof'

jack.speak("Woof")
#'Jack says Woof'




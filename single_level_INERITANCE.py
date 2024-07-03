#                                                 INHERITANCE

# In inheritance, the child class acquires the properties 
# and can access all the data members and functions 
# defined in the parent class.

# ------------------------------------------------------------------------------------------------------------------------------


#                                            SINGLE LEVEL INHERITANCE  - EXAMPLES

# parent class -> Animal
class Animal:  

    def speak(self):  
        print("Animal Speaking") 

# child class -> Dog inherits from the base class -> Animal  
class Dog(Animal): 

    def bark(self):  
        print("dog barking")  

d = Dog()

d.speak()
d.bark()

# ------------------------------------------------------------------------------------------------------------------------------


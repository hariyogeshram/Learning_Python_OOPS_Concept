#                                                    Static Members

#  It is a Class Variable

# That is, Common to all class members

# In static method(@staticmethod), we cannot use non-static/Instance methods & members/variables

# But, In Non-static Method, We can use both static members and non-static members

# ----------------------------------------------------------------------------------------------------------------------------------


#                                                EXAMPLES

class Person:

    # static members => common to all class members/variables

    sleeping_time = 8
    working_time = 9
    eating_numbers_per_day = 3

    def __init__(self, name, age):

        self.name = name
        self.age = age
    
    # Static Method
    @staticmethod
    def sleep():

        print(" --------------------------------------------------------------------------------------------")

        print("Person should sleep atleast", Person.sleeping_time, "hours per day.")

        print(" --------------------------------------------------------------------------------------------")

    

    # class Method  => cls.static_member  
    @classmethod
    def work(cls):

        print(" --------------------------------------------------------------------------------------------")

        print("Person should work for mininum", cls.working_time, "hours per day.")

        print(" --------------------------------------------------------------------------------------------")

    
    # Non Static Method / Instance 
    def eat(self):

        print(" --------------------------------------------------------------------------------------------")

        print("Person should Eat atleast", Person.eating_numbers_per_day, "hours per day.")

        print(" --------------------------------------------------------------------------------------------")


Person.sleep()
Person.work()
Person.eat()

# --------------------------------------------------------------------------------------------------------------------------


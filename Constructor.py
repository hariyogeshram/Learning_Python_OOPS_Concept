#                                              Constructor

# Special type of Function(Method)
# Used to initialize the instance members of the class
# "Constructor Name" => SAME AS => "Class Name"
# Two Types : DEFAULT & PARAMETERIZED Constructor
# Constructor definition is executed when we create the object of this class


#                                               __init__(self)

#   __init__()  => constructor , used in Python Classes
#  It is called automatically when an object is created from a class 
#  Allows us to initialize the attributes of the object


#                                                      'self' parameter

#  reference to " current instance of the class"
#  used to access variables , that belongs to class.



# -----------------------------------------------------------------------------------------------------------------------------------

#                                                   EXAMPLE   CODE  (example - 1)

# -----------------------------------------------------------------------------------------------------------------------------------


class Students:

    def __init__(self):

        print("constructor-1 is called")



stud_1 = Students()

# -----------------------------------------------------------------------------------------------------------------------------------

#                                                   EXAMPLE   CODE  (example - 2)

# -----------------------------------------------------------------------------------------------------------------------------------


class Humans:

    def __init__(self, name, age, gender, country):

        self.Name = name
        self.Age = age
        self.Gender = gender
        self.Country = country

    def get_human_info(self):

        print("My Name is ", self.Name, "From ", self.Country, ". I am ",+self.Age,"years old - ", self.Gender, ".")


human_1 = Humans("Hari", 24, 'Male', 'India')
human_1.get_human_info()

human_2 = Humans("Kavya", 21, 'Female', 'Australia')
human_2.get_human_info()


# -----------------------------------------------------------------------------------------------------------------------------------

#                                                   EXAMPLE   CODE  (example - 3)  => Constructor Overloading

# -----------------------------------------------------------------------------------------------------------------------------------

class Humans_info:

    def __init__(self, name, age, gender, country):

        self.Name = name
        self.Age = age
        self.Gender = gender
        self.Country = country

    def get_human_info(self):

        print("My Name is ", self.Name, "From ", self.Country, ". I am ",+self.Age,"years old - ", self.Gender, ".")


    # Constructor Overloading 

    def __init__(self, name, country):

        self.Name = name
        # self.Age = age
        # self.Gender = gender
        self.Country = country

    def get_human_info(self):

        print("My Name is ", self.Name, "From ", self.Country, ".")



human_1 = Humans_info("Hari", 'India')
human_1.get_human_info()

# I am facing this error : 

# TypeError: Humans_info.__init__() takes 3 positional arguments but 5 were given


human_2 = Humans_info("Kavya", 'Australia')
human_2.get_human_info()

# ------------------------------------------------------------------------------------------------------------------
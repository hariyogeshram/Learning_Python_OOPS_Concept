#  Class :

#         It's like a "Blueprint or Template" characteristics
#         Logical Entity
#         Collection of Objects
#         It has some specific "Attributes" and "Methods"


#  Object :

#           Physical Entity
#           It has its own "state" and "behaviour"
#           It may be any "real world objects"  -> like CAR, TABLE, CHAIR,.....


#  Coding Part ( Using CLASS & OBJECTS) 

class Human:

    # Attributes / states

    Name = None
    Age  = None
    Gender = None
    Country = None
    Height = None
    Weight = None

    # Now, Creating the methods and inside , we gonna print all the details

    def get_human_details(self):

        print("A Person ", self.Name, ". Age is ", self.Age, ". Gender is ", self.Gender, "From ", self.Country, ". Height is ", self.Height,"cm.", "Weight is ", self.Weight,"Kg.")


#--------------------------------------------------------------------------------------------------------------------------------------

# Object Creation for person_1

person_1 = Human()

# invoking the variables using objects and assigning variable name

person_1.Name = "Hari"
person_1.Age = 20
person_1.Gender = "Male"
person_1.Country = "India"
person_1.Height = 180
person_1.Weight = 60

# Object Creation for person_1

person_2 = Human()

# invoking the variables using objects and assigning variable name

person_2.Name = "Kanagavalli"
person_2.Age = 55
person_2.Gender = "Female"
person_2.Country = "India"
person_2.Height = 170
person_2.Weight = 65


# Now , calling the methods using object name

person_1.get_human_details()
person_2.get_human_details()

# --------------------------------------------------------------------------------------------------------------------------------------



# Exercise - 1 :

# Problem statement :

#                                Printing the total marks of any 5 subjects for List of 10 students 

#--------------------------------------------------------------------------------------------------------------------------------------

# class Students:

#     Name = None

#     Tamil = None
#     English = None
#     Maths = None
#     Science = None
#     Social = None

#     # print the details using methods

#     def get_total_marks(self):

#         total = self.Tamil + self.English + self.Maths + self.Science + self.Social

#         return total

#     # printing the name with total marks

#     def get_student_details(self, total):

#         print("Name : ", self.Name, " ---> Total_Marks = ",self.total)


# # ---------------------------------------------------------------------------------------------------------------------------------

# # object creation

# student_1 = Students()

# student_1.Name = "Hari"

# student_1.Tamil = 90
# student_1.English = 78
# student_1.Maths = 95
# student_1.Science = 92
# student_1.Social = 97

# # calling the methods

# student_1.get_total_marks()
# student_1.get_student_details(total)



        


    


    


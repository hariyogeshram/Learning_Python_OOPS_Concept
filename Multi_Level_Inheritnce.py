#                                                 MULTI LEVEL INHERITANCE


#  Multi-level inheritance is archived "when a derived class inherits another derived class".
#  There is "no limit on the number of levels up to" which, the multi-level inheritance is archived in python.

# ------------------------------------------------------------------------------------------------------------------------

# Examples :

# Parent class - > grand_parents
class grand_parent:

    def sing(self):

        print("Grand_Parent has Singing Talent")


# Child class : Parent 
class parent(grand_parent):

    def dance(self):

        print("Parent has Dancing Talent")



# child class : child ->
class child(parent):

    def swim(self):

        print("Child has Swimming Talent")



# ------------------------------------------------------------------------------------------------------------------------

c = child()

print("\n -----------------------------------------------------------------------------------------------------")


c.sing()
c.dance()
c.swim()

# ------------------------------------------------------------------------------------------------------------------------

c1 = parent()

print("\n -----------------------------------------------------------------------------------------------------")

c1.sing()
c1.dance()

# ------------------------------------------------------------------------------------------------------------------------

c2 = grand_parent()

print("\n -----------------------------------------------------------------------------------------------------")


c2.sing()

print("\n -----------------------------------------------------------------------------------------------------")


# ------------------------------------------------------------------------------------------------------------------------






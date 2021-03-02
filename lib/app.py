# Write your code here!

#PSEUDOCODE
    # * create a Member class with attributes:
        # * properties:
            # * full_name
        # * methods:
            # * introduce
    # * create childClass Student
        # * properties:
            # * reason
    # * create childClass Instructor
        # * properties:
            # * bio
            # * skills
        #methods:
            #add_skill
#Part II: Workshops
    # create a Workshop class
        #properties:
            #date
            #subject
            #instructors
            #students
        #methods:
            #add_participant
            #print_details
    
class Member:
    def __init__(self, full_name):
        self.name = full_name
    def introduce(self):
        return f"Hi, my name is {self.name}!"

class Student(Member):
    def __init__(self, full_name, reason):
        super().__init__(full_name)
        self.reason = reason

class Instructor(Member):
    def __init__(self, full_name, bio, skills = [None]):
        super().__init__(full_name)
        self.bio = bio
        self.skills = []
    def add_skill(self, skill):
        self.skills.append(skill)

# workshop = Workshop("12/03/2014", "Shutl")

jane = Student("Jane Doe", "I am trying to learn programming and need some help")
lena = Student("Lena Smith", "I am really excited about learning to program!")

print(jane.introduce())
print(jane.reason)

print(lena.introduce())

vicky = Instructor("Vicky Python", "I want to help people learn coding.")
vicky.add_skill("HTML")
vicky.add_skill("JavaScript")

print(vicky.introduce())
print(vicky.skills)

nicole = Instructor("Nicole McMillan", "I have been programming for 5 years in Python and want to spread the love")
nicole.add_skill("Python")

print(nicole.introduce())
print(nicole.skills)

# workshop.add_participant(jane)
# workshop.add_participant(lena)
# workshop.add_participant(vicky)
# workshop.add_participant(nicole)


# workshop.print_details()


# =>
# Workshop - 12/03/2014 - Shutl
#
# Students
# 1. Jane Doe - I am trying to learn programming and need some help
# 2. Lena Smith - I am really excited about learning to program!
#
# Instructors
# 1. Vicky Ruby - HTML, JavaScript
#    I want to help people learn coding.
# 2. Nicole McMillan - Ruby
#    I have been programming for 5 years in Ruby and want to spread the love
#
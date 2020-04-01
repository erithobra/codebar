class Member:
    def __init__(self, full_name):
        self.full_name = full_name
    def introduce(self):
        print(f"Hi, my name is {self.full_name}")
class Student(Member):
    def __init__(self, full_name, reason):
        super().__init__(full_name)
        self.reason = reason
    def __str__(self):
        return f"{self.reason}"
class Instructor(Member):
    def __init__(self, full_name, bio):
        super().__init__(full_name)
        self.bio = bio
        self.skills = []
    def add_skill(self, skill):
        self.skills.append(skill)
        return self.skills
    def __str__(self):
        return f"{self.bio}"
class Workshop:
    def __init__(self, date, subject):
        self.date = date
        self.subject = subject
        self.instructors = []
        self.students = []
    def add_participant(self, member):
        # https://stackoverflow.com/questions/510972/getting-the-class-name-of-an-instance
        if type(member).__name__ == 'Instructor':
            return self.instructors.append(member)
        if type(member).__name__ == 'Student':
            return self.students.append(member)
    def print_students(self):
        if len(self.students) > 0:
            print("Students:")
            i = 1
            for student in self.students:
                print(f"{i}.\t {student.full_name} - {student.reason}")
                i += 1
            print()
    def print_instructors(self):
         if len(self.instructors) > 0:
            print("Instructors:")
            i = 1
            for instructor in self.instructors:
                print(str(i) + "." + "\t" + instructor.full_name + " - " + ", ".join(instructor.skills))
                print("\t" + instructor.bio)
                i += 1
    def print_details(self):
        print(f"Workshop - {self.date} - {self.subject}\n")
        self.print_students()
        self.print_instructors()
workshop = Workshop("12/03/2014", "Shutl")
jane = Student("Jane Doe", "I am trying to learn programming and need some help")
lena = Student("Lena Smith", "I am really excited about learning to program!")
vicky = Instructor("Vicky Python", "I want to help people learn coding.")
vicky.add_skill("HTML")
vicky.add_skill("JavaScript")
nicole = Instructor("Nicole McMillan", "I have been programming for 5 years in Python and want to spread the love")
nicole.add_skill("Python")
workshop.add_participant(jane)
workshop.add_participant(lena)
workshop.add_participant(vicky)
workshop.add_participant(nicole)
workshop.print_details()

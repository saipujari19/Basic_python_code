#saiprasad pujari
# the program holds information about a course including teacher name, credits, and course name.
class Course:
    # class to store,manage information about a course.
    def __init__(self, course_name):
        # Initialize the course with a name and default values for teacher and credits.
        self.course_name = course_name
        self.teacher_name = ""
        self.credits = 0
    def set_teacher_name(self):
        #user to enter the teacher's name.
        self.teacher_name = input(f"Enter the teacher's name: ")
    def set_credits(self):
        #the user to enter the number of credits,  and ensuring it is an integer.
        while True:
            try:
                self.credits = int(input(f"Enter the number of credits: "))
                break
            except ValueError:
                print("Invalid input: Please enter a valid integer for credits.")
    def report(self):
        # returning a formatted string reporting the course details.
        return f"\nCourse Name: {self.course_name}\nTeacher Name: {self.teacher_name}\nCredits: {self.credits}"
def main():
# creating at least two instances of course
    course1 = Course("Network Communications")
    course2 = Course("Graduate and Professional skill development")
 # entering the  data for each course
    course1.set_teacher_name()
    course1.set_credits()
    course2.set_teacher_name()
    course2.set_credits()
# printing the  data using the report method
    print(course1.report())
    print(course2.report())
if __name__ == "__main__":
    main()
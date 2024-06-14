# # # # # # for i in range(6):
# # # # # #     for j in range(i):
# # # # # #         print("*", end="")
# # # # # #     print()
# # # # # class Course:
# # # # #     def __init__(self, teacher_name="", credits=0, course_name=""):
# # # # #         self.teacher_name = teacher_name
# # # # #         self.credits = credits
# # # # #         self.course_name = course_name
# # # # #
# # # # #     def set_teacher_name(self, name):
# # # # #         self.teacher_name = name
# # # # #
# # # # #     def set_credits(self, credits):
# # # # #         try:
# # # # #             self.credits = int(credits)
# # # # #         except ValueError:
# # # # #             print("Invalid input: Credits must be an integer.")
# # # # #
# # # # #     def report(self):
# # # # #         return f"Course Name: {self.course_name}\nTeacher Name: {self.teacher_name}\nCredits: {self.credits}"
# # # # #
# # # # #
# # # # # def main():
# # # # #     # Create the first instance
# # # # #     course1 = Course(course_name="Math 101")
# # # # #     course1.set_teacher_name("Dr. Smith")
# # # # #     course1.set_credits(3)
# # # # #
# # # # #     # Create the second instance
# # # # #     course2 = Course(course_name="History 202")
# # # # #     course2.set_teacher_name("Prof. Johnson")
# # # # #     course2.set_credits("four")  # This will trigger the ValueError
# # # # #
# # # # #     # Print the course information
# # # # #     print("Course 1 Info:")
# # # # #     print(course1.report())
# # # # #     print("\nCourse 2 Info:")
# # # # #     print(course2.report())
# # # # #
# # # # #
# # # # # if __name__ == "__main__":
# # # # #     main()
# # # # #
# # # # class Course:
# # # #     def __init__(self, course_name):
# # # #         self.course_name = course_name
# # # #         self.teacher_name = None
# # # #         self.credits = None
# # # #
# # # #     def enter_teacher_name(self, teacher_name):
# # # #         self.teacher_name = teacher_name
# # # #
# # # #     def enter_credits(self, credits):
# # # #         try:
# # # #             self.credits = int(credits)
# # # #         except ValueError:
# # # #             print("Error: Credits must be an integer.")
# # # #
# # # #     def report(self):
# # # #         return f"Course Name: {self.course_name}, Teacher Name: {self.teacher_name}, Credits: {self.credits}"
# # # #
# # # # def main():
# # # #     # Create two instances of the Course class
# # # #     course1 = Course("Mathematics")
# # # #     course2 = Course("Physics")
# # # #
# # # #     # Add data to the instances
# # # #     course1.enter_teacher_name("Dr. Smith")
# # # #     course1.enter_credits(3)
# # # #
# # # #     course2.enter_teacher_name("Prof. Johnson")
# # # #     course2.enter_credits(4)
# # # #
# # # #     # Print the data using the report method
# # # #     print(course1.report())
# # # #     print(course2.report())
# # # #
# # # # # Start the program
# # # # if __name__ == "__main__":
# # # #     main()
# # # def main ():
# # #     try:
# # #         age = int(input("Please enter your age: "))
# # #         if age < 1 or age > 120:
# # #             print("Invalid age. Age must be between 1 and 120.")
# # #         else:
# # #             print("Your age is", age)
# # #     except ValueError:
# # #         print("Invalid input. Please enter a number.")
# # #     finally:
# # #         print("your rubbish")
# # #
# # #
# # # if __name__ == "__main__":
# # #     main()
# # try:
# #     num_days = int(input("Enter the number of days: "))
# #     if num_days < 1:
# #         print("Invalid input. Number of days must be greater than 0.")
# #     else:
# #         total_pennies = 0
# #         print("Day\tSalary($)")
# #         for day in range(1, num_days + 1):
# #             pennies = 2 ** (day - 1)
# #             total_pennies += pennies
# #             print(f"{day}\t{pennies / 100:.2f}")
# #         print(f"Total salary for {num_days} days is ${total_pennies / 100:.2f}")
# # except ValueError:
# #     print("Invalid input. Please enter a valid integer.")
# #
# def calculate_earnings():
#     while True:
#         try:
#             days = int(input("Please enter the number of days: "))
#             if days < 1:
#                 print("Error: Number of days must be at least 1.")
#                 continue
#             break
#         except ValueError:
#             print("Error: Please enter a valid integer.")
#
#     print("\nDay\tSalary (in pennies)\tSalary (in dollars)")
#     print("------------------------------------------------")
#
#     total_pennies = 0
#     salary = 1  # Salary in pennies for the first day
#
#     day = 1
#     while day <= days:
#         total_pennies += salary
#         print(f"{day}\t{salary}\t\t\t{salary / 100:.2f}")
#         salary *= 2
#         day += 1
#
#     total_dollars = total_pennies / 100
#     print("------------------------------------------------")
#     print(f"Total pay after {days} days is ${total_dollars:.2f}")
#
#
# # Call the function to run the program
# calculate_earnings()

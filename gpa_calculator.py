"""
    Name: gpa_Calculator.py
    Author: Triumph Ogbonnia
    Created: 4/4/24
    Purpose: Calculate GPA
"""

class GPACalculator:
    def __init__(self):
        # Define a dictionary to map letter grades to their corresponding GPA values
        self.grades = {'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0, 'F': 0.0}

    def calculate_gpa(self, courses):
        # Initialize variables to keep track of total credit hours and total quality points
        total_credit_hours = 0
        total_quality_points = 0

        # Iterate through each course
        for course, grade, credit_hours in courses:
            # Check if the entered grade is valid
            if grade.upper() in self.grades:
                # Increment total credit hours and calculate quality points for the course
                total_credit_hours += credit_hours
                total_quality_points += self.grades[grade.upper()] * credit_hours

        # Calculate GPA if total credit hours are greater than 0, else return 0
        if total_credit_hours > 0:
            gpa = total_quality_points / total_credit_hours
            return gpa
        else:
            return 0.0

def main():
    # Create an instance of the GPACalculator class
    calculator = GPACalculator()

    # Initialize a list to store information about courses
    courses = []

    # Prompt the user to enter the number of courses
    num_courses = int(input("Enter the number of courses: "))

    # Iterate through each course to get information from the user
    for i in range(1, num_courses + 1):
        course = input(f"\nEnter the name of course {i}: ")
        grade = input(f"Enter the grade obtained in course {i} (A, B, C, D, F): ")
        credit_hours = float(input(f"Enter the credit hours for course {i}: "))
        courses.append((course, grade, credit_hours))  # Append course information to the list

    # Call the calculate_gpa method of the GPACalculator instance and display the GPA
    gpa = calculator.calculate_gpa(courses)
    print(f"\nYour GPA is: {gpa:.2f}")

if __name__ == "__main__":
    main()
"""
* This program reads a file with a list of university applicants where each student occupies a single line and
 information about them is in the following format:
 | FirstName LastName PhysicsExamScore ChemistryExamScore MathExamScore CompScienceExamScore SpecialExamScore FirstPriority SecondPriority ThirdPriority |

* The admissions procedure happens in three stages, with each student choosing three departments(1st, 2nd, 3rd priority) at the start
* Departments available are: Physics, Chemistry, Mathematics, Biotech and Engineering
* The points needed for a department are calculated as follows:
  1. Physics - mean value of the math and physics exam scores
  2. Chemistry - chemistry exam score
  3. Mathematics - math exam score
  4. Biotech - mean value of the chemistry and physics exam scores
  5. Engineering - mean value of the math and computer science exam scores
* Students also have a special exam that will be taken into account instead of the values points above if it is higher
 than the previous amount of points
* If two students have the exact amount of points for the same department, the one whose name comes before in the alphabet has the advantage

"""


class Student:
    def __init__(self, student_info):
        self.name = student_info[0]
        self.physics = float(student_info[1])
        self.chemistry = float(student_info[2])
        self.math = float(student_info[3])
        self.computer_science = float(student_info[4])
        self.special_exam_score = float(student_info[5])
        self.priorities = student_info[6:9]

    def __str__(self):
        return f"{self.name} {self.priorities[2]}"

    def get_points(self, department):
        points_per_department = {'Physics': round((self.physics + self.math) / 2, 1),
                                 'Chemistry': self.chemistry,
                                 'Biotech': round((self.physics + self.chemistry) / 2, 1),
                                 'Mathematics': self.math,
                                 'Engineering': round((self.computer_science + self.math) / 2, 1)
                                 }

        # use the special exam score if it benefits the student
        if self.special_exam_score > points_per_department[department]:
            return self.special_exam_score
        else:
            return points_per_department[department]


# applicants information is read from a file, returns a list of lists to be turned into objects of the Student class
def get_student_info(file_name):
    with open(file_name, 'r') as text_file:
        content = text_file.readlines()

    students = [Student(line.rstrip('\n').rsplit(" ", 8)) for line in content]
    return students


"""
The first approach to the problem was to limit the amount of sorting the program has to do by admitting every student into
their desired department at the start of every admission cycle and then removing the ones that didn't make the cut, back to the 
admissions list but this design has a major flaw:
  If a student is admitted into his first choice and stays in there during the second admission cycle (hence out of the admissions list as well),
  and during that second cycle another student "pushes" him/her out of their desired department, that student would have missed
  their second priority department completely.
  
For this reason it was necessary to sort the students for every department during each admissions procedure even though it is not optimal.
"""


def admissions_procedure(applicants, departments_dict, department_limit, priority_num):
    for department in departments_dict:
        # sort the applicants list in terms of points for the current department in question
        applicants_sorted = sorted(applicants, key=(lambda student: (-student.get_points(department), student.name)))
        for applicant in applicants_sorted:
            if applicant.priorities[priority_num] == department and len(departments_dict[department]) < department_limit:
                departments_dict[department].append(applicant)
                applicants.remove(applicant)
    sort_departments_dicts(departments_dict)  # sorts the departments once again once this round of admission is over


# sorts a dictionary of all the departments by rules stated above
def sort_departments_dicts(departments_dict):
    for department, student_list in departments_dict.items():
        departments_dict[department] = sorted(student_list, key=lambda student: (-student.get_points(department), student.name))


# creates a separate file for each department and writes the final version of the accepted students to it
def write_to_department_files(departments_dicts):
    for department, student_list in departments_dicts.items():
        with open(department.lower() + ".txt", 'w') as department_file:
            for student in departments_dicts[department]:
                department_file.write(f"{student.name} {student.get_points(department)}\n")


def output_to_console(departments_dict):
    for department, student_list in departments_dict.items():
        print(department)
        for student in student_list:
            print(student.name, student.get_points(department))
        print()


def main():
    max_accepted_students = int(input("Enter the maximum amount of students for each department: "))  # total number of applications

    students = get_student_info('applicant_list_5.txt')

    # dictionary that stores accepted applicant, all throughout the programs life-cycle
    departments = {'Biotech': [], 'Chemistry': [], 'Engineering': [], 'Mathematics': [], 'Physics': []}

    for i in range(3):  # three admission cycles
        admissions_procedure(students, departments, max_accepted_students, i)

    output_to_console(departments)
    write_to_department_files(departments)


if __name__ == '__main__':
    main()

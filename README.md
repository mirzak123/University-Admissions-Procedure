# University-Admissions-Procedure
Reads student application information from a file and automatically accepts students into prefered departments, taking into account the department limit and different exam scores
* This program reads a file with a list of university applicants where each student occupies a single line and
 information about them is in the following format:  
FirstName LastName PhysicsExamScore ChemistryExamScore MathExamScore CompScienceExamScore SpecialExamScore FirstPriority SecondPriority ThirdPriority

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

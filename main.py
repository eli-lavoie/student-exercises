from cohort import Cohort
from exercise import Exercise
from instructor import Instructor
from student import Student

#Create 4 Exercises
student_exercises = Exercise("Student Exercises", "Python")
react_nutshell = Exercise("React Nutshell", "React")
celeb_tribute = Exercise("Celebrity Tribute", "HTML")
petting_zoo = Exercise("Critters and Croquettes", "Python")

#Create 3 Cohorts
c40 = Cohort("Cohort 40")
c50 = Cohort("Cohort 50")
c9001 = Cohort("Cohort 9001")

#Create 4 students
eli_lavoie = Student("Eli", "Lavoie", "elijah-lavoie", "Cohort 40")
ryuji = Student("Ryuji", "Sakamoto", "for-realsies", "Cohort 40")
samo = Student("Sam", "Thomas", "sam-tha-wize", "Cohort 50")
goku = Student("Son", "Goku", "over9k", "Cohort 9001")

#Assign students to cohorts
c40.students.append(eli_lavoie)
c40.students.append(ryuji)
c50.students.append(samo)
c9001.students.append(goku)

#Create 3 instructors
igor = Instructor("Igor", "???", "velvetroom", "Cohort 40", "rehabilitation")
bobby = Instructor("Robert", "Pierson", "warped-thinker", "Cohort 50", "good music")
aug = Instructor("Augusto", "Iverson", "doctor-lifehacks", "Cohort 9001", "being toxic")

#Assign instructors to cohorts
c40.instructors.append(igor)
c50.instructors.append(bobby)
c9001.instructors.append(aug)

#Assign exercises to students
igor.assign_exercise(eli_lavoie, student_exercises)
igor.assign_exercise(ryuji, student_exercises)
igor.assign_exercise(eli_lavoie, petting_zoo)
igor.assign_exercise(ryuji, petting_zoo)

bobby.assign_exercise(samo, celeb_tribute)
bobby.assign_exercise(samo, react_nutshell)

aug.assign_exercise(goku, celeb_tribute)
aug.assign_exercise(goku, react_nutshell)

cohorts = list()
cohorts.append(c40)
cohorts.append(c50)
cohorts.append(c9001)

for cohort in cohorts:
    for student in cohort.students:
        string = ""
        string += f"{student.first_name} is working on "

        if len(student.exercises) == 1:
            string+= f"{student.exercises[0].exercise_name}."

        elif len(student.exercises) == 2:
            string += f"{student.exercises[0].exercise_name} "
            string += f"and {student.exercises[-1].exercise_name}."

        else:
            for exercise in student.exercises[:-1]:
                string += f"{exercise.exercise_name}, "
            string += f"and {student.exercises[-1].exercise_name}."

        print(string)

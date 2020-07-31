from nss_person import NSS_Person

class Instructor(NSS_Person):
    def __init__(self, f_name, l_name, slack, cohort, specialty):
        super().__init__(f_name, l_name, slack, cohort)
        self.specialty = specialty

    def assign_exercise (self, student, exercise):
        student.exercises.append(exercise)
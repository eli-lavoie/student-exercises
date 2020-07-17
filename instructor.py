class Instructor:
    def __init__(self, f_name, l_name, slack, cohort, specialty):
        self.first_name = f_name
        self.last_name = l_name
        self.slack_handle = slack
        self.cohort = cohort
        self.specialty = specialty

    def assign_exercise (self, student, exercise):
        student.exercises.append(exercise)
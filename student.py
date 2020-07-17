class Student:
    def __init__(self, f_name, l_name, slack, cohort):
        self.first_name = f_name
        self.last_name = l_name
        self.slack_handle = slack
        self.cohort = cohort
        self.exercises = []
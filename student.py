from nss_person import NSS_Person

class Student(NSS_Person):
    def __init__(self, f_name, l_name, slack, cohort):
        super().__init__(f_name, l_name, slack, cohort)
        self.exercises = []
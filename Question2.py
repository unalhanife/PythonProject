class School:


    def __repr__(self):
        return f"School({self.name}, {self.foundation_year})"


    def __init__(self, name, foundation_year):
        self.name = name
        self.foundation_year = foundation_year
        self.students = []
        self.teachers = {}

    def add_new_student(self, student_name, student_class):
        self.students.append((student_name, student_class))
        print(f"The student named {student_name} has been added to the {student_class} class.")


    def add_new_teacher(self, teacher_name, branch):
        self.teachers[teacher_name] = branch
        print(f"The teacher named {teacher_name} was added with the branch {branch}.")

    def view_student_list(self):
        print("Student List:")
        for student_name, student_class in self.students:
            print(f"- {student_name} ({student_class})")

    def view_teacher_list(self):
        print("Teacher List:")
        for teacher_name, branch in self.teachers.items():
            print(f"- {teacher_name} ({branch})")
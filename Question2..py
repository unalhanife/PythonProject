class School:

    def __init__(self, name, foundation_year):
        self.name = name
        self.foundation_year = foundation_year
        self.students = []
        self.teachers = {}
#Aynı isimli öğrenciler olabileceği için liste daha esnek bir yapı sunar. bu yuzden liste yapisi kullaniyorum.

#Hızlı Erişim (Key-Value): Öğretmenlerin branşıyla birlikte kaydedilmesi gerektiği için,
# bir öğretmen adına hızlıca erişmek adına sözlük daha uygundur.
# Sözlüklerde anahtar (key) olarak öğretmen adı, değer (value) olarak da branşıni kaydediyorum.

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

    def __str__(self):
        return f"School Name: {self.name}, Founded in: {self.foundation_year}, Students: {len(self.students)}, Teachers: {len(self.teachers)}"


# Kullanıcıdan okul bilgilerini almak icin input kullaniyorum.
school_name = input("Enter the school name: ")
foundation_year = int(input("Enter the foundation year: "))
my_school = School(school_name, foundation_year)

# Öğrenci eklemek icin while dongusu kullaniyorum.
while True:
    add_student = input("Do you want to add a student? (yes/no): ").lower()
    if add_student == "yes":
        student_name = input("Enter the student's name: ")
        student_class = input("Enter the student's class: ")
        my_school.add_new_student(student_name, student_class)
    elif add_student == "no":
        break
    else:
        print("Please type 'yes' or 'no'.")


while True:
    add_teacher = input("Do you want to add a teacher? (yes/no): ").lower()
    if add_teacher == "yes":
        teacher_name = input("Enter the teacher's name: ")
        branch = input("Enter the teacher's branch: ")
        my_school.add_new_teacher(teacher_name, branch)
    elif add_teacher == "no":
        break
    else:
        print("Please type 'yes' or 'no'.")

# Okul ve listeleri ekrana yazdırmak icin print kullaniyorum.
print("\nSchool Information:")
print(my_school)

print("\nStudent List:")
my_school.view_student_list()

print("\nTeacher List:")
my_school.view_teacher_list()
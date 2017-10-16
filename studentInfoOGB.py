import random

firstName = ["jay", "jim", "roy", "axel", "billy", "charlie", "jax", "gina", "paul",
"ringo", "ally", "nicky", "cam", "ari", "trudie", "cal", "carl", "lady", "lauren",
"ichabod", "arthur", "ashley", "drake", "kim", "julio", "lorraine", "floyd", "janet",
"lydia", "charles", "pedro", "bradley"]

lastName = ["blake", "holt", "meilijson", "brannon", "fieser", "line", "hellman",
"lyndon", "wendell", "corr", "fricano", "carrigan", "giddings", "piesse", "charlwood",
"thaler", "ambrose", "hamer", "schweig", "geiger", "kinder", "rogantin", "chevallier"
"wang", "tiedemann", "cohn", "digel", "reheem", "dzieciololowski", "callanan",
"lie", "oden"]

def main():
  students = [
    Student("Larsson", 37),
    Student("BonJovi", 55),
  ]

  printHeader()
  selection = int(getUserSelection())
  if selection == 0:
    printStudentsByAge(students)
  elif selection == 1:
    printStudentsByLName(students)
  elif selection == 2:
    printStudentsByFName(students)
  else:
    print ("SELECTION NOT RECOGNIZED")


class Student:
  def __init__(self, lastName, age):
    self.lastName = random.choice (lastName)
    self.age = self.assignRandomAge()
    self.firstName = random.choice(firstName)

  def assignRandomName(self):
    pass

  def assignRandomAge(self):
    self.age = random.randint(0,100)

  def assignRandomWeight(self):
    self.weight = random.randint(0,300)

  def assignRandomHeight(self):
    self.height = random.randint(0,84)

inputQuestions = [
  "For STUDENTS BY AGE, type 0",
  "For STUDENTS BY LAST NAME, type 1",
  "For STUDENTS BY FIRST NAME, type 3",
  "For SUM of STUDENT AGES type 4",
  "For AVERAGE of STUDENT AGES type 5",
]

def getUserSelection():
  print (inputQuestions[0])
  print (inputQuestions[1])
  print (inputQuestions[2])
  return input("Type selection and press enter:")

def printHeader():
    print("HEADER TEXT HERE")

def printStudentsByAge(students):
  print ("----Students By Age-----")
  sortStudents = sorted(students, key=lambda student: student.age)
  for student in students:
    print (student.lastName + ", " + student.firstName + ", " + str(student.age))

def printStudentsByLName(students):
  print ("----Students By Last Name -----")
  sortStudentsLName = sorted(students, key=lambda student: student.lastName)
  for student in students:
    print  (student.lastName + ", " + student.firstName + ", " + str(student.age))

def printStudentsByFName(students):
  print ("----Students By First Name ----")
  sortStudentsFName = sorted(students, key=lambda student: student.firstName)
  for student in students:
    print (student.lastName + ", " + student.firstName + ", " + str(student.age))


def printSumAge(students):
  print ("Answer:")

def printAvgAge(students):
  print ("Answer:")

def ageRange(studentA, studentB):
  return math.abs(studentA.age - studentB.age)


main()

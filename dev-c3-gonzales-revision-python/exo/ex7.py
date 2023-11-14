import re


def findStudentWithBestNote(students):
    bestNote = 0
    bestStudents = []
    for key, value in students.items():
        value = float(value)
        if value > bestNote:
            bestStudents = [key]
            bestNote = value
        elif value == bestNote:
            bestStudents.append(key)
    return sorted(bestStudents)[0]

students = {}

def enterValidNote(value):
    if not re.match(r'^\d+(\.\d{0,1})?$', value):
        print("Valeur invalide pour une node d'étudiant")
        value = input('Entrez sa note: ')
        enterValidNote(value)
    return value

def enterValidName(value):
    if value in students:
        print("Cet étudiant à déjà été renseigné.")
        value = input("Entrez le nom de l'étudiant: ")
        enterValidName(value)
    return value

    

while True:
    studentName = enterValidName(input("Entrez le nom de l'étudiant: "))
    studentNote = enterValidNote(input('Entrez sa note: '))

    print(studentName, studentNote)

    students[studentName] = studentNote
    addAnotherEntry = input("Ajouter un autre étudiant (y/n): ")
    if addAnotherEntry == 'n':
        break
    

print(findStudentWithBestNote(students))

import re


def findStudentWithBestNote(students):
    bestNote = 0
    bestStudents = []
    for key, value in students.items():
        if value > bestNote:
            bestStudents = [key]
            bestNote = value
        elif value == bestNote:
            bestStudents.append(key)
    return sorted(bestStudents)[0]

students = {}

def enterValidNote(value):
    if not re.match(r'^[0-9.]+$', value):
        print("Valeur invalide pour une node d'étudiant")
        enterValidNote(input('Entrez sa note: '))
    return value
    

while True:
    studentName = input("Entrez le nom de l'étudiant: ")
    studentNote = enterValidNote(input('Entrez sa note: '))

    students[studentName] = studentNote
    addAnotherEntry = input("Ajouter un autre étudiant (y/n): ")
    if addAnotherEntry == 'n':
        break
    

print(students)

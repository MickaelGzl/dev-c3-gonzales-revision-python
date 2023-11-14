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


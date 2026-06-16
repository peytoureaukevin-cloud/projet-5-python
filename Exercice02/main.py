students = {
    "Alice": {
        "Mathematiques": 90,
        "Francais": 80,
        "Histoire": 95
    },
    "Bob": {
        "Mathematiques": 75,
        "Francais": 85,
        "Histoire": 70
    },
    "Charlie": {
        "Mathematiques": 88,
        "Francais": 92,
        "Histoire": 78
    }
}

student_name = input("Entrez le nom de l’étudiant : ")

if student_name in students:
    grades = students[student_name]

    print(f"Notes de {student_name} :")

    for subject, grade in grades.items():
        print(f"{subject} : {grade}")

    average = sum(grades.values()) / len(grades)
    print(f"Moyenne de {student_name} : {average}")
else:
    print(f"L'étudiant {student_name} n'existe pas dans la liste.")
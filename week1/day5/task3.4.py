students = [
    {
        "name": 'Gaylord',
        "academic_year": 2022,
        "units": [
            {
                "name": "Web Development",
                "credits": 90,
                "grade": "A"
            },
            {
                "name": "Network and System Administration",
                "credits": 90,
                "grade": "B"
            },
            {
                "name": "Java",
                "credits": 90,
                "grade": "A"
            },
        ]
    },
    {
        "name": 'Michel',
        "academic_year": 2022,
        "units": [
            {
                "name": "Web Development",
                "credits": 90,
                "grade": "C"
            },
            {
                "name": "Network and System Administration",
                "credits": 90,
                "grade": "B"
            },
            {
                "name": "Java",
                "credits": 90,
                "grade": "D"
            },
        ]
    },
    {
        "name": 'Jaques',
        "academic_year": 2022,
        "units": [
            {
                "name": "Web Development",
                "credits": 90,
                "grade": "A"
            },
            {
                "name": "Network and System Administration",
                "credits": 90,
                "grade": "A"
            },
            {
                "name": "Java",
                "credits": 90,
                "grade": "A"
            },
        ]
    }
]

grade_weight_mapping = {
    "A": 4,
    "B": 3,
    "C": 2,
    "D": 1,
    "E": 0
}

def setTotalCredits(student): 
    student["total_credits"] = 0
    for unit in student["units"]:
        student["total_credits"] += unit["credits"]

def setGPA(student):
    average = 0
    for unit in student["units"]:
        average += grade_weight_mapping[unit["grade"]]
    student["GPA"] = average / len(student["units"])
    

for student in students:
    setTotalCredits(student)
    setGPA(student)






print(sorted(students, key=lambda student: student["name"]))
print(sorted(students, key=lambda student: student["GPA"], reverse=True))
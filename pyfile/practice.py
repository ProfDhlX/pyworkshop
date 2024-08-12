students = [
    ("salam",98),
    ("sajaki",69),
    ("cyam",88),   
    ("maljol",100),
]

with open('lala.txt', 'w') as file:
    for student in students:
        file.write(f"name: {student[0]}, Marks: {student[1]}\n")
# maximum value
student_score = input("Input a list of students scores ").split()
for n in range(0, len(student_score)):
    student_score[n] = int(student_score[n])
print(student_score)

heighest_score = 0
for score in student_score:
    if score > heighest_score:
        heighest_score = score
print(f"The highest score in the class is: {heighest_score}")

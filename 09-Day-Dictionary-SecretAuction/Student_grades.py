student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}


#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

for names in student_scores:
  mark = student_scores[names]
  if mark > 90:
    student_grades[names] = "O"
  elif mark<90 and mark>80:
    student_grades[names] = 'A+'
  elif mark<80 and mark>70:
    student_grades[names] = 'A'
  elif mark<70 and mark>60:
    student_grades[names] = 'B+'
  elif mark<60 and mark>50:
    student_grades[names] = 'B'
  elif mark<50:
    student_grades[names] = 'E'
  
print(student_grades)






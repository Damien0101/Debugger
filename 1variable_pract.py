import pandas as pd

student_grades = {
    "Names": ["John", "Doe", "Alice", "Bob"],
    "Grades": [85, 90, 88, 93],
}



average_grade = student_grades['Grades'].mean() 
print(f"Average grade: {average_grade}")

# if you need help 'https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html'
#                   ctrl + click
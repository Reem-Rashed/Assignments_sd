#This program takes letter grades 
grades = list(map(int, input("Enter grades (separated by commas): ").split(',')))
#split(',')-> ex->90,80,79 retern[90,80,79]

letter_grades = list(map(lambda x:
    'A' if x >= 90 else
    'B' if x >= 80 else
    'C' if x >= 70 else
    'D' if x >= 60 else
    'F', grades))

#lambda small function 

print(f"Grades: {grades}") # print grandes
print(f"Letter grades: {letter_grades}") #print letter grades
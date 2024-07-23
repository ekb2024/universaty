students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
average_ball = {}

for i in range(len(students)):
    average_ball[sorted(list(students))[i]] = sum(grades[i]) / len(grades[i])
print(average_ball)

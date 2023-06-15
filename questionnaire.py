import matplotlib.pyplot as plt
students = [40,55,100,80,25]
grade = ['A','B','C','D','E']
exp = [0,0,0.2,0,0]
cl = ['red','green','blue','brown','yellow']
plt.pie(students, labels = grade, explode = exp, autopct = '%2.1f%%', colors = cl)
plt.show

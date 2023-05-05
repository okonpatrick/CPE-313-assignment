"""
#cpe 311 assignment

import cProfile

def myFunc():
    for i in range(1, 31):
        if i % 2 == 0:
            print(i, end=' ')

    print([i for i in range(1, 31) if i % 2 == 0])

    print([i for i in reversed(range(1, 11))])

    print([n for n in range(10, 0, -1)])

cProfile.run('myFunc()')
"""

Blockchain_tech = {"Akpan", "Victor", "Chris", "Greg"}
Data_analysis = {"Chris", "Uwem", "Fred"}
Robotics = {"chris", "Fred", "Kings", "Victor"}
Mobile_app = {"Fred", "Akpan", "Victor", "Unyime"}


#use for the first condition
Project_A = Robotics.intersection(Mobile_app)
print("People who Roboticists but neither a Data Analyst nor aBlockchain expert include:\n", Project_A)

#use for the second condition
Project_B = Mobile_app.intersection(Data_analysis)
print("Sets of data analysts who are also good in mobile app development include\n", Project_B)


Project_C = Blockchain_tech.union(Mobile_app)
print("Everyone who is skilled in Blockchain and/or Mobile app development but not a roboticist include:\n", Project_C)
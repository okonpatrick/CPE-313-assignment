Blockchain_tech = {"Akpan", "Victor", "Chris", "Greg"}
Data_analysis = {"Chris", "Uwem", "Fred"}
Robotics = {"Chris", "Fred", "Kings", "Victor"}
Mobile_app = {"Fred", "Akpan", "Victor", "Unyime"}

# For the first condition(Project_A)
R1 = Robotics.difference(Data_analysis)
R2 = Robotics.difference(Blockchain_tech)
ConditionR = "People who Roboticists but neither a Data Analyst nor a Blockchain expert include:\n"
print("\n", ConditionR, {Project_A for Project_A in R1.intersection(R2)}, "\n")

# For the second condition(Project_B)
Project_B = Mobile_app.intersection(Data_analysis)
print("Sets of Data analysts who are also good in mobile app development include:\n", Project_B, "\n")

# For the third condition(Project_C)
B1 = Blockchain_tech.union(Mobile_app)
ConditionC = "Everyone who is skilled in Blockchain and/or Mobile app development but not a roboticist include:\n"
print(ConditionC, {Project_C for Project_C in B1.difference(Robotics)})

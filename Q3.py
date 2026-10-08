Employees=[]
for i in range(1,4):
    name=input("Enter employee name: ")
    age=int(input("Enter your age: "))
    salary=int(input("Enter your salary: "))
    
    employee=(name,age,salary)
    Employees.append(employee)

print(Employees)
    
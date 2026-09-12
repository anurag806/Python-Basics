# Sets
anu={10,10,305,3,50,67};
print(anu);
anu.add(34);
anu.discard(10)
print(anu);
# dictionary
employee={
    'name':"anurag",
    'age':24,
    'salary':63000,
    'department':"IT"
}
print(employee.values());
employee['name']="ram";
print(employee);


employees = [
    {
        "id": 101,
        "name": "Anurag",
        "department": "IT",
        "salary": 62000
    },
    {
        "id": 102,
        "name": "Rahul",
        "department": "HR",
        "salary": 45000
    },
    {
        "id": 103,
        "name": "Arya",
        "department": "Finance",
        "salary": 72000
    },
    {
        "id": 104,
        "name": "Amit",
        "department": "IT",
        "salary": 85000
    }
]
print(employees);
employees[0]['name']="Ram";
print(employees);
employees.pop(0);
print(employees);
employees[1].pop('salary');
print(employees);

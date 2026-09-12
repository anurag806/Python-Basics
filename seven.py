import datetime
import mysql.connector

now=datetime.datetime.now();
print(now.year);
print(now.month);
print(now.time());
print(now)
class student:
    def __init__(self,name,age):
        self.name=name;
        self.age=age;
e1=student("James",23);
print(e1.name);
print(e1.age);


connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_PASSWORD",
    database="YOUR_DATABASE"
)

cursor = connection.cursor()

cursor.execute("SELECT * FROM employees")

data = cursor.fetchall()

for row in data:
    print(row)

cursor.close()
connection.close()
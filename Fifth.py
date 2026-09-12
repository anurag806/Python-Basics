#functions
def arm(a, b):
    return a+b;
print(arm(1,2));
def bonus(salay):
    return salay*2;
res=bonus(5);
print(res);
# default parameters
def salary(amount,percent=10):
    return (amount*percent);
print(salary(5000,30))
numbers = [10, 15, 20, 25, 30, 35, 40]
even=[]
for num in numbers:
    if num%2==0:
        even.append(num)
print(even);

#Exception handlings

try:
    a=int(input("Enter a number:"))
    print(100/a);
except:
    print("errors")

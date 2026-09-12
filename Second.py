marks=int(input("Enter your marks:"))
if marks>=90:
    print("Grade A")
elif marks>=75 and marks<=89:
    print("Grade B")
elif marks>=50 and marks<=74:
    print("Grade C")
else:
    print("Fail")
#loops
for i in range(0,5):
    print("i am anurag")
for i in range(0,20,5):
    print(i);
for j in range(10,0,-1):
    print(j)

#while loops
i=10;
while i <=20:
    print(i);
    i+=1;
i=0
while i<=20:
    print(i)
    i+=5;
    #break
i=0;
while i<=20:
    print(i);
    if i==10:
        break;
    i+=1;
#continue
i=0;
while i<=5:
    i+=1
    if i==3:
        continue;
    print(i);

for i in range(10):
    if i%2==0:
        continue;
    print(i);


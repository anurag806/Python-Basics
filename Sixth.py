import csv
# file handlings
file=open("employees.txt","w")
file.write("anurag,pandey,5000")
#file.close();
file=open("employees.txt","r")
data=file.read();
print(data);
file=open("sam.txt","w");
file.write("Anurag,IT,63000\nRahul,HR,45000\nArya,Finance,72000")
file=open("sam.txt","r")
data=file.read();
print(data);
file=open("Sam.txt","a");
file.write("\nAmit,IT,86000")
file.close();
file=open("Sam.txt","r")
datas=file.read();
print(datas);
# csv data

file=open("emple.csv","r");
data=csv.DictReader(file);
for das in data:
    print(das);
file.close();
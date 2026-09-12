name=["anu","rahul","ram","lax"]
print(name[0])
print(len(name))
salary = [45000, 62000, 30000, 80000, 55000];
for sal in salary:
    if sal > 50000:
        print(sal)
cities = ["Kanpur", "Lucknow", "Delhi"]
cities.append("Unnao");
cities.insert(1,"Mumbai");
cities.remove("Delhi");
print(cities)
print(len(cities));
numbers = [40, 10, 50, 20, 30]
numbers.pop(2);
numbers.append(45);
numbers.sort();
print(numbers);
print(numbers[1:4]);
print(numbers[0:5:2])
print(numbers[::-1]);
#tuples

tup=(10,20,30,40,50);
print(tup.count(10));
print(tup.index(10)+1);
print(tup);
lst=list(tup);
print(lst);

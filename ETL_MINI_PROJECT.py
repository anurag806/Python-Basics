import requests
import logging
import csv
logging.basicConfig(level=logging.INFO)

url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url);
if response.status_code == 200:
    logging.info("Got 200");
    data=response.json();
filter_data=[];
for user in data:
    if user["id"]>5:
        filter_data.append(user);
print(filter_data);

File=open("data.csv","w")
writer = csv.writer(File);
writer.writerow(["id", "name", "email"])

for user in filter_data:
    writer.writerow([
        user["id"],
        user["name"],
        user["email"]
    ])
File.close();
file=open("data.csv","r")
for line in file:
    print(line);
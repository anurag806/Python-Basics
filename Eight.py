import requests
import csv
url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)
res=response.json()
print(res)
print(response.status_code)
for user in res:
    if user["id"]>5:
        print(user["username"]);

# csv file creation for this data
url = "https://jsonplaceholder.typicode.com/users";
response=requests.get(url);
res=response.json();
print(res)

file=open("anu.csv","w");
writer = csv.writer(file)

writer.writerow(["id", "name", "username", "email"])

for user in res:
    writer.writerow([
        user["id"],
        user["name"],
        user["username"],
        user["email"]
    ])

file.close()

print("Data saved successfully");

file=open("anu.csv","r")
reader = csv.reader(file)
print(list(reader));

#Logging
import logging
import requests

logging.basicConfig(level=logging.INFO)

try:
    logging.info("API request started")

    response = requests.get(
        "https://jsonplaceholder.typicode.com/users"
    )

    response.raise_for_status()

    data = response.json()

    logging.info("Data received successfully")

except Exception as e:
    logging.error("Job failed: %s", e)
from pymongo import MongoClient
import datetime
import uuid
import random
import array

lastnames = []
with open("USA-most-common-lastnames.txt", "r") as lastnames_info_file:
    lastnames_info = lastnames_info_file.readlines()
    for line in lastnames_info:
        lastname = line.split('\t')[0]
        lastnames.append(lastname)

print(f"Lastnames: {len(lastnames)} ")       

firstnames = [] 
with open("USA-most-common-firstnames.txt", "r") as firstnames_info_file:
    firstnames_info = firstnames_info_file.readlines()
    for line in firstnames_info:
        firstname = line.split('\t')[0]
        firstnames.append(firstname)

print(f"Firstnames: {len(firstnames)} ")

cities = []
with open("USA-cities-by-population.txt", "r") as cities_info_file:
    cities_info = cities_info_file.readlines()
    for line in cities_info:
        line = line.strip()
        (city, state, population) = line.split('\t')
        full_city = f"{city}, {state}"
        representation = [full_city for _ in range(int(population))]
        cities.extend(representation)       


print(f"Cities: {len(cities)} ")

#client = MongoClient("mongodb://10.227.242.242:27017/")
client = MongoClient("mongodb://localhost:27017/")

now = datetime.datetime.now(tz=datetime.timezone.utc).replace(microsecond=0).isoformat().replace(":", "")
db = client[f"test"]
collection = db[f"test-jp-{now}"]

print("Inserting documents...")
for i in range(10000):
    document = {
        "Firstname": firstnames[random.randint(0, len(firstnames)-1)],
        "MiddleInitial": firstnames[random.randint(0, len(firstnames)-1)][0],
        "Lastname": lastnames[random.randint(0, len(lastnames)-1)],	
        "DOB": datetime.datetime.fromtimestamp(random.random() * datetime.datetime.now(tz=datetime.timezone.utc).timestamp()),
        "NationalID": uuid.uuid4().hex,
        "location": cities[random.randint(0, len(cities)-1)],
        "date": datetime.datetime.now(tz=datetime.timezone.utc),
    }

    document_id = collection.insert_one(document).inserted_id
    print(f"{i:8d}", end="\r")

print()
print("done!")

client.close()


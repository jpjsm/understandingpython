from random import triangular

import mysql.connector

cnx = mysql.connector.connect(
    user="scott", password="tiger", host="W10F2TYYD3", database="icecream"
)

cursor = cnx.cursor()

truncate_stmt = "TRUNCATE TABLE icecream"

cursor.execute(truncate_stmt)

truncate_stmt = "TRUNCATE TABLE flavors_reference"

cursor.execute(truncate_stmt)

Initial_flavors = [
    "Mint Chocolate Chip",
    "Vanilla",
    "Avocado",
    "Mango",
    "Blueberry",
    "Chocolate",
    "Cookies Cream",
    "Pistachio",
    "Coconut",
    "Lemon",
    "Cookie Dough",
    "Birthday Cake",
    "Moose Tracks",
    "Strawberry",
    "Cotton Candy",
    "S'mores",
    "Superman",
    "Sweet Cream",
    "Peanut Butter",
    "Butter Pecan",
    "Cherry",
    "Green Tea",
    "Neapolitan",
    "Coffee",
    "Banana",
    "Salted Caramel",
    "Raspberry",
    "Eskimo",
    "Horchata",
    "Banana Nut",
    "Root Beer Float",
    "Almond Joy",
    "Orange Cream",
    "Peach",
    "Ube",
    "Huckleberry",
    "Bourbon",
    "Praline Pecan",
    "Maryland Mud",
    "Maple",
    "Butter Brickle",
    "Dark Chocolate",
    "Butterscotch",
    "Pumpkin",
    "Watermelon",
    "Mexican Chocolate",
    "Berries and Cream",
    "Brownie",
    "Teaberry",
    "Rocky Road",
]

mixed_flavors = [f for f in Initial_flavors if " " in f]
single_flavors = [f for f in Initial_flavors if " " not in f]
total_single_flavors = len(single_flavors)
print(f"Total single flavors: {total_single_flavors}")
print(f"Total mixed flavors: {len(mixed_flavors)}")

MAX_FINAL_FLAVORS = 200_000

prefix_index = 0
count = 0
total_flavors_to_generate = MAX_FINAL_FLAVORS - len(mixed_flavors)

new_flavors = [""]
exponential_print = 64
name_max_len = 0
while count < total_flavors_to_generate:
    for i in range(total_single_flavors):
        if single_flavors[i] in new_flavors[prefix_index]:
            continue

        new_flavor = f"{new_flavors[prefix_index]} {single_flavors[i]}".strip()
        new_flavors += [new_flavor]
        name_len = len(new_flavor)
        if name_len > name_max_len:
            name_max_len = name_len

        count += 1
        if count >= total_flavors_to_generate:
            break

    prefix_index += 1
    if count > exponential_print:
        print(f"{count}: {new_flavors[-1]}")
        exponential_print <<= 1

flavors = mixed_flavors + new_flavors[1:]
print(f"{len(flavors)}: {flavors[-1]}")
print(f"{name_max_len=}")

Id = 1
for flavor in flavors:
    insert_stmt = (
        "INSERT INTO icecream.icecream"
        "(Id, Name,Price, Quantity, Description)"
        "VALUES (%s, %s, %s, %s, %s);"
    )
    insert_data = (
        Id,
        flavor,
        triangular(4.0, 9.5, 5.5),
        int(triangular(0, 50, 5)),
        f"The great and unique '{flavor}'",
    )

    cursor.execute(insert_stmt, insert_data)

    insert_stmt = (
        "INSERT INTO icecream.flavors_reference" "(Name, Id)" "VALUES (%s, %s);"
    )

    for simple in flavor.split():
        insert_data = (simple, Id)

        cursor.execute(insert_stmt, insert_data)

    cnx.commit()
    Id += 1

cnx.close()

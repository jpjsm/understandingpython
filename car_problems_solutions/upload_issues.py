import psycopg
import csv
import hashlib

# Environment
DB_HOST = "localhost"
DB_PORT = 5432
DB_NAME = "car_problems_solutions"
DB_USER = "postgres"
DB_PASS = "ABCdef123!"

with open("./car_problems_solution.csv", "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        problem = row["PROBLEM"].lower().strip()
        solution = row["SOLUTION"].lower().strip()
        id = hashlib.sha256(str.encode(f"{problem}{solution}")).hexdigest()
        with psycopg.connect(
            dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT
        ) as conn:
            try:
                result = conn.execute(
                    "INSERT INTO issues (id, problem, solution) VALUES(%s, %s, %s)",
                    (id, problem, solution),
                )
                conn.commit()
                print(
                    f"Inserted: (id, problem, solution) -> ('{id}','{problem}', '{solution}')"
                )
            except psycopg.Error as ex:
                print(
                    f"{ex.diag.severity}:{ex.sqlstate} |  {ex.diag.message_primary} -> {ex.diag.message_detail}"
                )
print("Inserts applied")

import json
from MongodbJsonEncoder import MongdbJsonEncoder
from pymongo import MongoClient
from TraverseDictionary import Traverse

client = MongoClient("mongodb://localhost:27017/")

jira_db = client["jira"]
jira_col = jira_db["jira"]

tickets = jira_col.find()
for ticket in tickets[:10]:
    text_data = Traverse(
        ticket, ["description", "displayName", "emailAddress", "name", "summary"]
    )
    with open(
        f"/mnt/c/tmp/learn-mongodb-data/{ticket['key'].lower()}.json", "w"
    ) as out_ticket:
        out_ticket.write(
            json.dumps(text_data, cls=MongdbJsonEncoder, indent=4, sort_keys=True)
        )
        # out_ticket.write(str(ticket))

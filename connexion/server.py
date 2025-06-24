import connexion


def GetProducts():
    return """ [
{
    "id": 23,
    "name": "product name 世界",
    "cost": 234.56,
    "stock": 8
},
{
    "id": 7,
    "name": "персик",
    "cost": 11.93,
    "stock": 3
}
]
"""


app = connexion.App(__name__, specification_dir="openapi/")
app.add_api("product.json")


if __name__ == "__main__":
    app.run(port=8080)

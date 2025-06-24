import json


def text2json(filename):

    with open(filename, 'r', encoding="utf-8") as input:
        lines = input.readlines()

    quotes = []
    i = 1
    for line in lines:
        print(i)
        _, q, a = line.split("\t")
        i+=1
        quotes.append({
            "quote": q.strip(),
            "author": a.strip()
        })

    return json.dumps(quotes, indent=2)

if __name__ == "__main__":
    with open("C:\\learning\\python\\Text2Json\\Quotes.json", 'w') as output:
        output.write(text2json("C:\\learning\\python\\Text2Json\\Quotes.txt"))

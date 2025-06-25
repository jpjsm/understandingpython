grouping = 8
for i in range(12):
    p = 10**i
    b = f"{p:037b}"
    result = ""
    for j in range(len(b) - 1, 0, -grouping):
        result = b[j - grouping if (j - grouping) > 0 else 0 : j + 1] + " " + result

    print(f"{i: >2} {p: >17,} {b} {result}")

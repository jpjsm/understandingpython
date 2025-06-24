import sys
import math
import json

def array2d(rows, columns):
    a = []
    for i in range(rows):
        a.append([None] * columns)
        for j in range(columns):
            a[i][j] = None

    return a

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(f"Argument mismatch {sys.argv}")

    rows = int(sys.argv[1])
    columns = int(sys.argv[2])
    twoDarray = array2d(rows, columns)

    columnDivisor = 10 ** math.ceil(math.log10(columns))

    for i in range(rows):
        for j in range(columns):
            twoDarray[i][j] = i + (j/columnDivisor)

    print(json.dumps(twoDarray, indent=2))

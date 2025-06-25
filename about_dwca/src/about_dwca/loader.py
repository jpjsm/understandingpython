import csv
from pathlib import Path
import pickle


source_folder = Path("/sample-data/latest_dwca")

tsv_files = [
    "Distribution.tsv",
    "MeasurementOrFact.tsv",
    "SpeciesProfile.tsv",
    "Taxon.tsv",
    "VernacularName.tsv",
]
db = {}
distinct_values = {}
for filename in tsv_files:
    tsv_file_path = source_folder.joinpath(filename)
    tsv_filename = str(tsv_file_path)
    tsv_base = tsv_file_path.stem
    db[tsv_base] = {}
    with open(tsv_filename, "r", encoding="utf-8") as infile:
        lines = infile.readlines()
    header_line = lines[0].rstrip()
    headers = [h.split(":")[1] for h in header_line.split("\t")]
    headers2column_map = {h: i for i, h in enumerate(headers)}
    print(f"{tsv_base: <24}: {len(lines[1:]): >12,} rows, {headers2column_map}")
    for h in headers:
        if h not in distinct_values:
            distinct_values[h] = set()

    rows = []
    for i, l in enumerate(lines[1:]):
        row = l.rstrip("\n").split("\t")
        if len(row) != len(headers):
            raise ValueError(
                f"Number of columns '{len(row): >4,}' in row {i+2: >12,} is "
                f"{'longer' if len(l.split('\t')) > len(headers) else 'shorter'} "
                f"than Header count {len(headers): >4,}."
            )
        rows.append([c if c else "" for c in row])
        db[tsv_base][row[headers2column_map["taxonID"]]] = {
            h: row[headers2column_map[h]] for h in headers if h != "taxonID"
        }

        for h in headers:
            distinct_values[h].add(row[headers2column_map[h]])

    with open(source_folder.joinpath(f"{tsv_base}.csv"), "w", newline="") as csvfile:
        csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_NONNUMERIC)
        csvwriter.writerow(headers)
        csvwriter.writerows(rows)

print(f"{'-'*40}  Distinct Values Count  {'-'*40}")
for k in sorted(distinct_values.keys()):
    print(f"{k: <24} -->  {len(distinct_values[k]): >12,}")

with open(source_folder.joinpath("db.pkl"), "wb") as pkl_file:
    pickle.dump(db, pkl_file)

with open(source_folder.joinpath("distinct_values.pkl"), "wb") as pkl_file:
    pickle.dump(distinct_values, pkl_file)

print(f"{'*'*40}  DONE  {'*'*40}")

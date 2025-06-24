"""
Replaces template variables in files.

- Reads files from an folder, 
- replaces templates, 
- and saves them in the output folder.
"""

import sys
import json
from pathlib import Path


def updatetemplates(config: dict) -> int:
    infolder = Path(config["infolder"])
    file_list = []
    for filename in infolder.iterdir():
        file_list.append(str(filename))

    templates = config["templates"]

    for filename in file_list:
        outputText = None
        with open(filename, "r") as inputFile:
            inputText = inputFile.read()

        if filename.find("main.py") >= 0:
            print("Found 'main.py' doing replacements")

        outputText = inputText
        for k in templates.keys():
            tkey = "{{" f"{k}" "}}"
            if outputText.find(tkey) != -1:
                print(f"[{filename}] Replacing '{tkey}' --> {templates[k]}")
                outputText = outputText.replace("{{" f"{k}" "}}", templates[k])

            print()

        print(outputText)

        outfilename = Path(config["outfolder"]).joinpath(Path(filename).name)
        with open(outfilename, "w") as savedFile:
            savedFile.write(outputText)

    return 0


if __name__ == "__main__":

    config = None
    with open("app.json", "r") as inputfile:
        config = json.load(inputfile)

    if config is None:
        print("'app.json' file not found.")
        sys.exit(-1)

    sys.exit(updatetemplates(config))

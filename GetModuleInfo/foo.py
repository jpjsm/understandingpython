from pathlib import Path
from inspect import currentframe

parent = Path(__file__).parent
file_no_ext = Path(__file__).stem
module = f"{parent.name}.{file_no_ext}"
print(f"Module: {module}")

def MyFunction():
    print(f"{currentframe().f_code.co_name=}")

MyFunction()    
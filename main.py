from csv import DictReader
from json import dumps
from typing import List

def from_csv_to_json(csv: str) -> str:
    reader: DictReader = DictReader(csv.split("\n"))
    return dumps(list(reader))

if __name__ == "__main__":
    from sys import stdin, stdout
    stdout.write(from_csv_to_json(stdin.read()))

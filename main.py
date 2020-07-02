from csv import DictReader, Dialect, QUOTE_MINIMAL
from json import dumps

class MyDialect(Dialect):
    quoting = QUOTE_MINIMAL
    delimiter = ","
    quotechar = '"'
    lineterminator = "\n"
    skipinitialspace = True

def from_csv_to_json(csv: str) -> str:
    reader: DictReader = DictReader(csv.split("\n"), dialect=MyDialect)
    return dumps(list(reader))

if __name__ == "__main__":
    from sys import stdin, stdout
    stdout.write(from_csv_to_json(stdin.read()))

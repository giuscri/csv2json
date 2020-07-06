from csv import DictReader, Dialect, QUOTE_MINIMAL
from json import dumps
from typing import Type

def from_csv_to_json(csv: str, separator: str = ",") -> str:
    class MyDialect(Dialect):
        quoting = QUOTE_MINIMAL
        delimiter = separator
        quotechar = '"'
        lineterminator = "\n"
        skipinitialspace = True

    reader: DictReader = DictReader(csv.split("\n"), dialect=MyDialect)
    return dumps(list(reader))

if __name__ == "__main__":
    from sys import stdin, stdout, argv, exit

    separator = ","
    if len(argv) > 1 and argv[1] == "-s":
        separator = argv[2]

    stdout.write(from_csv_to_json(stdin.read(), separator))

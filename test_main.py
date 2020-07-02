from main import from_csv_to_json
from json import loads

def test_common_case():
    csv = """first_name,last_name
otis,redding
sonny,moore
"""
    json_encoded = from_csv_to_json(csv)

    assert loads(json_encoded) == [
        {
            "first_name": "otis",
            "last_name": "redding"
        },
        {
            "first_name": "sonny",
            "last_name": "moore"
        }
    ]

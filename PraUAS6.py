import json

json_string = """
[
    {"1": "one", "2": "two", "3": "three"},
    {"1": "un", "2": "deux", "3": "trois"},
    {"1": "eins", "2": "zwei", "3": "drei"}
]
"""

data = json.loads(json_string)
result_6 = data[1]["2"]
print('6. json.loads(json_string)[1][2]:', result_6)

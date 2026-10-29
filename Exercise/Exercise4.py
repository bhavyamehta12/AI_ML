# a=[1,2,3,4]
# y = reduce(lambda x:x*8,a)

# print(list(y))
import json

raw_data = '''
{
    "readings": [
        {"id": 1, "value": 82, "tags": ["temp", "sensor"]},
        {"id": 2, "value": 95, "tags": ["sensor", "alert"]},
        {"id": 3, "value": 82, "tags": ["temp", "sensor"]},
        {"id": 4, "value": 70, "tags": ["humidity"]},
        {"id": 5, "value": 95, "tags": ["alert", "sensor"]}
    ]
}
'''

data = json.loads(raw_data)
# print(data)
readings = data["readings"]
print(readings)
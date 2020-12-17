from schema import Schema, And, Use, Optional, SchemaError

class GraphData():

    def check_data_type(self, graphData):
        schema = Schema([{'data': {
            'id': (str),
            Optional('label'): (str),
            Optional('source'): (str),
            Optional('target'): (str),
            },
            Optional('position'): {
                'x': (float),
                'y': (float)
            }
        }])
        if not schema.validate(graphData):
            return schema.validate(graphData)
    
    def  check_if_the_id_is_unique(self, graphData):
        list_of_ids = []
        for data in graphData:
            list_of_ids.append(data["data"]["id"])

        if len(list_of_ids) > len(set(list_of_ids)):
            print("ID should be unique")
            return False

uploaded_data = [
    {"data": {"id": "254126",
                "label": "254126"
            },
            "position": {
                "x": -269.9039611816406,
                "y": 420.89410400390625
            }
    },{"data": {"source": "244521", "target": "280038", "id": '280038'}},
    {"data": {"source": "244521", "target": "280038", "id": "244521:d"}},
    {"data": {"source": "244521", "target": "280038", "id": "244521:d"}}
]

example = GraphData()
if example.check_data_type(uploaded_data):
    print(example.check_data_type(uploaded_data))

if example.check_if_the_id_is_unique(uploaded_data):
    print(example.check_if_the_id_is_unique(uploaded_data))


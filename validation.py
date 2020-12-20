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

    def check_if_source_target_are_valid(self, graphData):

        def get_node_list(graphData):
            node_list = []
            for data in graphData:
                try:
                    if data["position"]:
                        node_list.append(data["data"]["id"])
                except KeyError:
                    continue
                except Exception as e:
                    raise e

            return node_list

        def if_the_edge_is_valid(graphData, nodeList):
            for data in graphData:
                try:
                    if data["data"]["source"] and data["data"]["target"]:
                        edge_id = data["data"]["id"]
                        source = data["data"]["source"]
                        target = data["data"]["target"]
                
                        if not source in nodeList:
                            raise Exception("Can not create edge {} with nonexistant source {}".format(edge_id, source))
                        if not target in nodeList:
                            raise Exception("Can not create edge {} with nonexistant target {}".format(edge_id, target))
                except KeyError:
                    continue
                except Exception as e:
                    raise e
        
        if_the_edge_is_valid(graphData, get_node_list(graphData))

uploaded_data = [
    {"data": {"id": "254126",
                "label": "254126"
            },
            "position": {
                "x": -269.9039611816406,
                "y": 420.89410400390625
            }
    },{"data": {"source": "244521", "target": "280038", "id": '280038'}},
    {
        "data": {
            "id": "280038",
            "label": "280038"
        },
        "position": {
            "x": -459,
            "y": 234
        }
    },
    {"data": {"source": "244521", "target": "280038", "id": "244521:d"}},
    {"data": {"source": "244521", "target": "280038", "id": "244521:d"}}
]
correct_data = [
    {
        "data": {
            "id": "254126",
            "label": "254126"
        },
        "position": {
            "x": -269.32,
            "y": 420.33
        }
    },
    {
        "data": {
            "id": "280038",
            "label": "280038"
        },
        "position": {
            "x": -459.32,
            "y": 234.3
        }
    },
    {
        "data": {
            "source": "254126",
            "target": "254126",
            "id": "254126:280038"
        }
    }
]

example = GraphData()
if example.check_data_type(correct_data):
    print(example.check_data_type(correct_data))

if example.check_if_the_id_is_unique(uploaded_data):
    print(example.check_if_the_id_is_unique(uploaded_data))

if example.check_if_source_target_are_valid(uploaded_data):
    print(example.check_if_source_target_are_valid(uploaded_data))


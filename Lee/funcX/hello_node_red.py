from typing import Collection
from funcx.sdk.client import FuncXClient
fxc = FuncXClient()

def hello_node_red():
    return "Hello Node-RED!"

func_uuid = fxc.register_function(hello_node_red)
tutorial_endpoint = '4b116d3c-1703-4f8f-9f6f-39921e5864df'  # Public tutorial endpoint
                                                            # private endpoint(default): d09a2eea-07b2-4572-beb4-4c3270fa2ee7

result = fxc.run(endpoint_id=tutorial_endpoint, function_id=func_uuid)

print(fxc.get_result(result))

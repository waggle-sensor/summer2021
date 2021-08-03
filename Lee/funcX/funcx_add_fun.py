from funcx.sdk.client import FuncXClient

fxc = FuncXClient()

def add_func(a, b):
    return a + b

func_uuid = fxc.register_function(add_func)
tutorial_endpoint = '4b116d3c-1703-4f8f-9f6f-39921e5864df' # Public tutorial endpoint
                                                           # private endpoint(default): d09a2eea-07b2-4572-beb4-4c3270fa2ee7

res = fxc.run(5, 10, function_id=func_uuid, endpoint_id=tutorial_endpoint)

print(fxc.get_result(res))

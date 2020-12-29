from config.application import endpoint


@endpoint("/")
def route():
    return {"response": "hello!"}, 200


@endpoint("/", "post")
def route_post(req):
    return {"response": "hello!", "args": req}, 200

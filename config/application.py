from flask import Flask, request, jsonify

app = Flask(__name__)


def endpoint(route, method="GET"):
    def decorator(f):
        app.add_url_rule(route, route.replace("/", "-") + "-" + method, lambda: __worker(f), methods=[method])

    return decorator


def __worker(f):
    if f.__code__.co_argcount == 1:
        req = request.get_json()
        return_tuple = f(req)
    else:
        return_tuple = f()
    if type(return_tuple) == dict:
        return jsonify(return_tuple)
    if type(return_tuple) == tuple:
        if len(return_tuple) != 2:
            raise RuntimeError("Cannot infer return style.")
        left, right = return_tuple
        if type(left) == int:
            return right, left
        elif type(right) == int:
            return left, right
    raise RuntimeError("Cannot infer return style.")

